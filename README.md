# Python REST API with Flask

This project is a simple example of a REST API created with Python using the Flask framework. The API has two endpoints:
- `GET /api/greet`: Returns a general greeting message.
- `POST /api/greet`: Returns a personalized greeting based on the name provided in the request.

## Prerequisites
- Python 3.12 installed.
- `pip` for managing packages.

## Installation

1. Clone this repository or download the files.
2. Navigate to the project directory:
   ```sh
   cd PYTHONAPIREST
   ```
3. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On MacOS/Linux:
     ```sh
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```sh
   pip install Flask
   ```

## Running the Application

1. With the virtual environment activated, set the `FLASK_APP` environment variable:
   ```sh
   set FLASK_APP=main
   ```
2. Run the Flask server:
   ```sh
   flask run
   ```
   Alternatively, you can run the application directly with Python:
   ```sh
   python main.py
   ```
3. The server will be available at `http://127.0.0.1:5000`.

## Using the API

### `GET /api/greet`
- Make a GET request to `/api/greet` to receive a general greeting.
- Example response:
  ```json
  {
    "message": "Hello, welcome to the REST API!"
  }
  ```

### `POST /api/greet`
- Make a POST request to `/api/greet` with a JSON body containing a `name` field to receive a personalized greeting.
- Example request body:
  ```json
  {
    "name": "Alice"
  }
  ```
- Example response:
  ```json
  {
    "message": "Hello, Alice!"
  }
  ```

## Deactivating the Virtual Environment

When you are done working, you can deactivate the virtual environment with:
```sh
deactivate
```

## License
This project is distributed under the MIT license.
