from fastapi.testclient import TestClient
from fastapi import status
from main import app # Assuming main.py is in the parent directory

client = TestClient(app)


def test_health_check_strength_checker():
    response = client.get("/health_strength_checker")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status_strength_checker": "ok"}


def test_check_password_strength_very_weak_short():
    # Test with a very short password
    password_to_check = "abc"
    response = client.post("/check_password_strength", json={"password": password_to_check})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    
    assert data["password"] == password_to_check # Or masked if you implement that
    # TODO: Assert that `data["strength"]` is "very_weak" or similar based on your logic.
    # TODO: Assert that `data["score"]` is low (e.g., 0 or 1).
    # TODO: Assert that `data["suggestions"]` contains "Password should be at least 8 characters long."
    # Example:
    # assert data["strength"] == "very_weak"
    # assert data["score"] <= 1
    # assert "Password should be at least 8 characters long." in data["suggestions"]
    pass # Remove when assertions are added


def test_check_password_strength_medium_only_lowercase_and_long():
    password_to_check = "thisisalongpassword" # Long, but only lowercase
    response = client.post("/check_password_strength", json={"password": password_to_check})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # TODO: Assert the strength category (e.g., "medium" or "weak" depending on scoring).
    # TODO: Assert that suggestions include adding uppercase, digits, and symbols.
    # Example:
    # assert data["strength"] in ["weak", "medium"] 
    # assert "Add uppercase letters." in data["suggestions"]
    # assert "Add digits." in data["suggestions"]
    # assert "Add symbols (e.g., !@#$%)." in data["suggestions"]
    pass # Remove when assertions are added


def test_check_password_strength_strong_all_criteria():
    password_to_check = "Str0ngP@sswOrd123!" # Meets all criteria
    response = client.post("/check_password_strength", json={"password": password_to_check})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # TODO: Assert that `data["strength"]` is "strong" or "very_strong".
    # TODO: Assert that `data["score"]` is high.
    # TODO: Assert that `data["suggestions"]`
    # is empty or contains minimal/no suggestions.
    # Example:
    # assert data["strength"] in ["strong", "very_strong"]
    # assert data["score"] >= 4
    # assert len(data["suggestions"]) == 0
    pass  # Remove when assertions are added


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
