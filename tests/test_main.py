from fastapi.testclient import TestClient
from fastapi import status
from main import app  # Assuming main.py is in the parent directory

client = TestClient(app)


def test_health_check_strength_checker():
    response = client.get("/health_strength_checker")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status_strength_checker": "ok"}


def test_check_password_strength_very_weak_short():
    # Test with a very short password
    password_to_check = "abc"
    response = client.post("/check_password_strength",
                           json={"password": password_to_check})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["password"] == password_to_check
    assert data["strength"] in ["weak", "veryweak"]
    assert data["score"] <= 1
    assert "Password should be at "
    "least 8 characters long." in data["suggestions"]


def test_check_password_strength_medium_only_lowercase_and_long():
    password_to_check = "thisisalongpassword"  # Long, but only lowercase
    response = client.post("/check_password_strength",
                           json={"password": password_to_check})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["strength"] in ["weak", "medium", "strong"]
    assert "Add uppercase letters." in data["suggestions"]
    assert "Add digits." in data["suggestions"]
    assert "Add symbols (e.g., !@#$%)." in data["suggestions"]


def test_check_password_strength_strong_all_criteria():
    password_to_check = "Str0ngP@sswOrd123!"  # Meets all criteria
    response = client.post("/check_password_strength",
                           json={"password": password_to_check})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["strength"] in ["strong", "very_strong"]
    assert data["score"] >= 4
    assert len(data["suggestions"]) == 0


def test_check_password_strength_missing_payload():
    response = client.post("/check_password_strength", json={})  # Empty JSON
    # FastAPI / Pydantic should automatically handle missing required fields.
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_check_password_strength_empty_password():
    response = client.post("/check_password_strength", json={"password": ""})
    # Pydantic model has min_length=1 for password field
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

# TODO: (Optional Bonus) Add more test cases:
# - Password with only uppercase and symbols.
# - Password with only digits.
# - Password that is exactly 8 characters long but meets all other criteria.
