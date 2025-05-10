# Password Strength Checker API

## Description

(TO BE COMPLETED BY STUDENTS: Briefly describe the project - e.g., an API that analyzes a given password and returns its estimated strength and suggestions for improvement.)

## Prerequisites

(TO BE COMPLETED BY STUDENTS: List what is needed to run this project locally, e.g., Python 3.8+ and pip.)

## Installation

1.  Clone this repository:
    ```bash
    # git clone <repository_url>
    # cd <repository_name>
    ```
2.  Create and activate a Python virtual environment:
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows (PowerShell/cmd):
    # venv\Scripts\activate
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the FastAPI application locally using Uvicorn:
```bash
uvicorn main:app --reload
```
The application will typically be available at http://127.0.0.1:8000. The interactive API documentation (Swagger UI) can be found at http://127.0.0.1:8000/docs.

## API Endpoints

(TO BE COMPLETED BY STUDENTS: Describe each API endpoint, its purpose, request body/path parameters, and an example of the expected JSON response or behavior.)

* POST /check_password_strength
  * Description: (Students to describe: e.g., Analyzes the provided password.)
  * Request Body: {"password": "yourPassword123"}
  * Example Response (200 OK):
  ```json
    {
        "password": "yourPassword123", 
        "strength": "medium", 
        "score": 3,
        "suggestions": ["Add symbols (e.g., !@#$%)"]
    }
  ```

* GET /health_strength_checker
  * Description: (Students to describe: Health check for this API.)
  * Response: {"status_strength_checker": "ok"}

## Project Structure

(Optional: Students can briefly describe the main files if they wish)

* main.py: Contains the FastAPI application logic for the password strength checker.
* requirements.txt: Lists the Python dependencies.
* tests/: Contains the automated tests.
* .gitlab-ci.yml: Defines the GitLab CI/CD pipeline.
* README.md: This file.