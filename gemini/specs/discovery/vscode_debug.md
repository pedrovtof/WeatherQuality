# VS Code Debug Configuration Discovery

- Entry point: `src/app/main.py`
- App variable: `app`
- Interpreter: Virtual environment in `env/`
- Goal: Create `launch.json` for VS Code debugging.

FastAPI debugging typically uses the `uvicorn` module directly or a python script that runs uvicorn. Using the module is cleaner for VS Code.
