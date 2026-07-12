# AGENTS.md

This project is a small Flask-based waste-to-wealth web app.

## Project map
- app.py: Flask entrypoint and routes.
- predict.py: model loading and prediction logic.
- templates/: HTML pages for the UI.
- static/: CSS and other frontend assets.
- ml/data/Model/: trained model artifacts and related files.
- uploads/: uploaded images created at runtime.

## Working conventions
- Keep changes compact and focused; avoid introducing extra folders or layers unless needed.
- Keep Flask route handling in app.py and prediction/model logic in predict.py.
- Preserve the existing simple template/static structure when editing the UI.
- If new Python packages are required, add them to requirements.txt.
- If the model file is missing or renamed, make the app fail gracefully and surface a clear message.

## Common commands
- Activate the virtual environment: .\venv\Scripts\Activate.ps1
- Run the app locally: python app.py
- Or use Flask directly: flask run
