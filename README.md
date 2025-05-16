# 🌍 Google Agent Development Kit (ADK) Demo - Travel Planner

<div align="center">

![ADK Travel Planner Banner](https://via.placeholder.com/800x200/4285F4/FFFFFF?text=Google+ADK+Travel+Planner)

[![Travel Planner](https://img.shields.io/badge/Travel-Planner-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://github.com/AashiDutt/Google-Agent-Development-Kit-Demo)
[![Gemini API](https://img.shields.io/badge/Powered%20by-Gemini%20API-fbbc05?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Running the Application](#-running-the-application)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

---

## 🔍 Overview

This project demonstrates an intelligent travel planning system built with **Google Agent Development Kit (ADK)**. It showcases a multi-agent architecture where specialized AI agents collaborate to create comprehensive travel recommendations for users.

The system leverages **Gemini 2.0 Flash** for intelligent decision-making across multiple specialized agents, all coordinated through a host agent and presented through an intuitive Streamlit interface.

---

## 🚀 Features

<table>
  <tr>
    <td width="50%">
      <h3>🤖 Multi-agent Architecture</h3>
      <p>Specialized AI agents working together to create comprehensive travel plans</p>
    </td>
    <td width="50%">
      <h3>🧠 Gemini-powered Recommendations</h3>
      <p>Leveraging Gemini 2.0 Flash model for intelligent travel suggestions</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>🖥️ Interactive UI</h3>
      <p>Simple Streamlit interface for travel planning inputs</p>
    </td>
    <td width="50%">
      <h3>🔄 Agent-to-Agent Communication</h3>
      <p>Coordinated planning through API calls between specialized agents</p>
    </td>
  </tr>
</table>

---

## 🏗️ Architecture

The project consists of the following components:

### Agent System

<div align="center">
  <img src="https://via.placeholder.com/800x400/E8F0FE/000000?text=Agent+Architecture+Diagram" alt="Agent Architecture" />
</div>

<table>
  <tr>
    <th>Agent</th>
    <th>Port</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><b>🎮 Host Agent</b></td>
    <td>8000</td>
    <td>Acts as the coordinator, distributes requests to specialized agents, and aggregates responses into a unified travel plan</td>
  </tr>
  <tr>
    <td><b>✈️ Flight Agent</b></td>
    <td>8001</td>
    <td>Recommends flight options based on origin, destination, dates, and budget, providing airline, price, and timing details</td>
  </tr>
  <tr>
    <td><b>🏨 Stay Agent</b></td>
    <td>8002</td>
    <td>Suggests accommodations at the destination with hotel names, pricing, and locations</td>
  </tr>
  <tr>
    <td><b>🎭 Activities Agent</b></td>
    <td>8003</td>
    <td>Recommends tourist and cultural activities with descriptions, prices, and durations</td>
  </tr>
</table>

### User Interface

The frontend is built with **Streamlit**, providing an intuitive interface for users to input their travel details and view the comprehensive recommendations.

---

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- Git
- OpenAI/Gemini API key

### Step-by-Step Setup

<details>
<summary><b>1. Clone the Repository</b></summary>

```bash
git@github.com:bright-arparwut/traveling-planer-agents-A2A.git
cd traveling-planer-agents-A2A
```
</details>

<details>
<summary><b>2. Set up Python Environment</b></summary>

```bash
# Create and activate virtual environment
python3 -m venv adk_demo
source adk_demo/bin/activate  # On Windows: adk_demo\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
</details>

<details>
<summary><b>3. Configure API Key</b></summary>

```bash
# Linux/Mac
export OPENAI_API_KEY="your-api-key"

# Windows
set OPENAI_API_KEY=your-api-key
```
</details>

---

## 🚀 Running the Application

<div align="center">
  <img src="https://via.placeholder.com/800x250/F6F6F6/000000?text=Launch+Sequence+Diagram" alt="Launch Sequence" />
</div>

Start each component in separate terminal windows:

<details open>
<summary><b>Launch All Components</b></summary>

```bash
# 1. Start Host Agent
uvicorn agents.host_agent.__main__:app --port 8000 &

# 2. Start Flight Agent
uvicorn agents.flight_agent.__main__:app --port 8001 &

# 3. Start Stay Agent
uvicorn agents.stay_agent.__main__:app --port 8002 &

# 4. Start Activities Agent
uvicorn agents.activities_agent.__main__:app --port 8003 &

# 5. Launch Streamlit UI
streamlit run travel_ui.py
```
</details>

The Streamlit interface will automatically open in your browser at `http://localhost:8501`.

---

## 📋 Usage

<div align="center">
  <img src="https://via.placeholder.com/800x400/F9F9F9/000000?text=Streamlit+UI+Screenshot" alt="Streamlit UI" />
</div>

1. **Enter Travel Details:**
   - Origin city (e.g., "Bangkok")
   - Destination city (e.g., "Paris")
   - Start date
   - End date
   - Budget in USD

2. **Click "Plan My Trip!"**

3. **View Results:**
   - Flight recommendations
   - Accommodation options
   - Suggested activities
   - All within your specified budget!

---

## 🧠 How It Works

<div align="center">
  <img src="https://via.placeholder.com/800x300/F0F8FF/000000?text=System+Flow+Diagram" alt="System Flow" />
</div>

1. User submits travel details through the **Streamlit UI**
2. Request is sent to the **Host Agent** (port 8000)
3. Host Agent distributes the request to specialized agents:
   - **Flight Agent** (port 8001)
   - **Stay Agent** (port 8002)
   - **Activities Agent** (port 8003)
4. Each specialized agent uses the **Gemini API** to generate relevant suggestions
5. Host Agent aggregates all responses
6. UI displays the complete travel plan to the user

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin new-feature`
5. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgements

- **Google Agent Development Kit (ADK)** for the agent framework
- **Gemini AI** for the powerful language model capabilities
- **Streamlit** for the user interface components

---

<div align="center">
  <p>Built with ❤️ using Google Agent Development Kit</p>
</div>
