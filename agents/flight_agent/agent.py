from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from datetime import datetime
from dotenv import load_dotenv
import requests
import os
import logging

load_dotenv()


def search_flights(departure_id:str, arrival_id:str, outbound_date:str, return_date:str):
    """
    searching a flight using google flight api
    Search Query:
    
    departure_id : Parameter defines the departure airport code or location kgmid.
    An airport code is an uppercase 3-letter code.
    
    arrival_id : Parameter defines the arrival airport code or location kgmid.
    An airport code is an uppercase 3-letter code.
    
    outbound_date : Parameter defines the outbound date.
    
    return_date : Parameter defines the return date.
    
    """
    try:
        logging.info(f"Searching flights from {departure_id} to {arrival_id} for dates {outbound_date} to {return_date}")
        api_url = f"https://serpapi.com/search?engine=google_flights&departure_id={departure_id}&arrival_id={arrival_id}&gl=us&hl=en&currency=USD&outbound_date={outbound_date}&return_date={return_date}&api_key={os.getenv('SERPAPI_API_KEY')}"
        flights = requests.get(api_url, timeout=30)
        
        # Log the status code and response content for debugging
        logging.info(f"SerpAPI response status: {flights.status_code}")
        if flights.status_code != 200:
            logging.error(f"SerpAPI error response: {flights.text}")
            return {"error": f"API returned status code {flights.status_code}", "message": "Unable to fetch flight data"}
            
        # Try to parse JSON
        try:
            return flights.json()
        except requests.exceptions.JSONDecodeError as e:
            logging.error(f"JSON parsing failed: {str(e)}")
            logging.error(f"Response content: {flights.text[:500]}")  # Log first 500 chars of response
            return {"error": "Invalid JSON response", "message": "Unable to parse flight data"}
    except Exception as e:
        logging.error(f"Error fetching flight data: {str(e)}")
        return {"error": "Request failed", "message": str(e)}

flight_searching_tool = FunctionTool(func=search_flights)

flight_agent = Agent(
    name = "flight_agent",
    model = "gemini-2.0-flash",
    description="Suggests flight options for a destination.",
    instruction=(
    "Given a destination, travel dates, and budget, suggest 1-2 realistic flight options from search_flights tool by provinding departure_id, arrival_id, outbound_date, and return_date. "
    "Include airline name, price, and departure time. Ensure flights fit within the budget."
    ),
    tools=[flight_searching_tool]   
)

session_service = InMemorySessionService()
runner = Runner(
    agent = flight_agent,
    app_name="flight_app",
    session_service = session_service
)

USER_ID = "user_1"
SESSION_ID = "session_001"

async def execute(request):
    session_service.create_session(
        app_name = "flight_app",
        user_id = USER_ID,
        session_id=SESSION_ID
    )
    prompt = (
    f"User is flying from {request['origin']} to {request['destination']} "
    f"from {request['start_date']} to {request['end_date']}, with a budget of {request['budget']}. "
    "Suggest 2-3 realistic flight options. For each option, include airline, departure time, return time, "
    "price, and mention if it's direct or has layovers."
    )

    message = types.Content(role="user", parts=[types.Part(text=prompt)])
    
    logging.info(f"Executing flight search for: {request['origin']} to {request['destination']}")
    try:
        async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=message):
            if event.is_final_response():
                return {"flights": event.content.parts[0].text}
    except Exception as e:
        logging.error(f"Error in flight agent execution: {str(e)}")
        return {"flights": f"An error occurred while searching for flights: {str(e)}"}
