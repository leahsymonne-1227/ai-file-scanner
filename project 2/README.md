# AI File Scanner — Iteration 2: Review Data Collection

This folder contains the second iteration of the AI File Scanner learning project. It continues the work in the repository’s first version by adding a customer review form and a Flask backend as a step toward collecting client feedback. It is part of the same project and GitHub repository, not a separate project.

## Current progress

- Flask serves the form from `templates/` and its stylesheet from `static/`.
- The form collects a customer name, purchased product, and review.
- Submitting the form sends those answers to Flask, which currently prints them in the terminal.
- Google Sheets saving is the next planned step and is not connected yet.

## Run locally

From this folder, activate the `googlesheet.venv` virtual environment, then start Flask:

```sh
flask --app app run --debug
```

Open `http://127.0.0.1:5000/` in a browser while the Flask server is running.
