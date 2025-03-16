# Bookmark Manager

A simple bookmark manager application built with Flask.

## Description

This application allows you to store and manage your bookmarks in a simple and user-friendly way. You can add, edit, delete, and search bookmarks.

## Setup

1.  Create a new directory for the project:

    ```bash
    mkdir bookmark_manager
    cd bookmark_manager
    ```

2.  Create templates and static directories:

    ```bash
    mkdir templates
    mkdir static
    ```

3.  Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS and Linux
    ```

4.  Install Flask:

    ```bash
    pip install flask
    ```

## Running the project

1.  Set the FLASK_APP environment variable:

    ```bash
    set FLASK_APP=app.py  # On Windows
    export FLASK_APP=app.py  # On macOS and Linux
    ```

2.  Run the Flask application:

    ```bash
    flask run
    ```

3.  Open the application in a web browser and navigate to `http://127.0.0.1:5000/`.

## Using the bookmark manager

- **Adding a bookmark:** Fill in the form at the bottom of the main page and click "Add".
- **Editing a bookmark:** Click the "Edit" link next to the bookmark you want to edit.
- **Deleting a bookmark:** Click the "Delete" link next to the bookmark you want to delete.
- **Searching for a bookmark:** Enter your search query in the search bar at the top of the main page and click "Search". You can search by title, description, or document ID.

## Project structure

```
bookmark_manager/
├── app.py          # Main application file
├── templates/      # HTML templates
│   ├── index.html  # Main page
│   └── edit.html   # Edit bookmark page
├── static/         # Static files
│   └── style.css   # CSS stylesheet
└── bookmarks.json  # JSON file storing the bookmarks
```

## Technologies used

- Flask: A micro web framework written in Python.
- Jinja2: A template engine for Python.
- HTML: A markup language for creating web pages.
- CSS: A stylesheet language used to describe the presentation of a document written in HTML.
- JSON: A lightweight data-interchange format.

## Compiling to EXE file (Optional)

`pyinstaller --onefile --add-data "bookmark_manager/templates;templates" --add-data "bookmark_manager/static;static" bookmark_manager/app.py`
