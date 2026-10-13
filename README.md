# AI File Scanner

An ongoing learning project for building an AI file-scanning experience and the supporting data workflow. The work is organized as iterations in this same repository.

## Project iterations

### Iteration 1 — Scanner interface

The first version is a front-end prototype with “New Upload” and “Existing Upload” navigation. Selecting an option changes which one appears active. File uploading, document scanning, and a backend are not implemented in this version.

- `document_scanner_ui.html` — first-version page structure and navigation behavior
- `document_scanner_ui.css` — first-version navigation styling

### Iteration 2 — Review data collection (in progress)

The next iteration adds a customer review form as a learning step toward collecting client feedback for the AI File Scanner project. It uses Flask to serve the form and receive the customer name, product, and review. Flask currently prints submitted answers in the terminal.

Google Sheets saving is not connected yet; that is the next planned step. See the [Iteration 2 README](project%202/README.md) and [Iteration 2 changelog](project%202/CHANGELOG.md).

## Run Iteration 1

Open `document_scanner_ui.html` in a web browser.

## Run Iteration 2

From the `project 2` folder, activate the `googlesheet.venv` virtual environment and run:

```sh
flask --app app run --debug
```

Then open `http://127.0.0.1:5000/` while the Flask server is running.
