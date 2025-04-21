from common.a2a_server import create_app
from .task_manager import run

app = create_app(agent=type("Agent", (), {"execute":run}))

if __name__ == "__main__":
    import unicorn
    uvicorn.run(app, port=8002)