import re
from fastapi import FastAPI, Body, status
from pydantic import BaseModel, Field

app = FastAPI()

# --- Pydantic Models ---


class PasswordInput(BaseModel):
    password: str = Field(..., min_length=1, description="Password to check")


class PasswordStrengthResponse(BaseModel):

    password: str
    strength: str
    score: int  # A score from 0 to 4 or 5, for example
    suggestions: list[str] = []

# --- Business Logic ---


def check_password_strength_logic(password: str) -> PasswordStrengthResponse:
    """
    Analyzes the password and returns its strength and suggestions.
    STUDENTS TO COMPLETE THIS FUNCTION.
    """
    strength_levels = {
        0: "very_weak",
        1: "weak",
        2: "medium",
        3: "strong",
        4: "very_strong"
        # You can adjust the number of levels and their names
    }
    score = 0
    suggestions = []
    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long.")
    elif len(password) < 12:
        score += 1
    else:
        score += 2
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")
    # TODO 4: Digit check
    # - Use regex (re.search(r"[0-9]", password)) to check for digits.
    # - If present, increment score by 1.
    # - Else, add "Add digits." to suggestions.
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add symbols (e.g., !@#$%).")
    final_score = min(score, max(strength_levels.keys()))
    if len(password) < 8 and final_score > 1:
        final_score = 1
        if not any("at least 8 characters" in s for s in suggestions):
            suggestions.append("Password should be at least 8 char long")
    strength_category = strength_levels.get(
        final_score,
        "unknown")
    return PasswordStrengthResponse(
        password=password,
        strength=strength_category,
        score=final_score,
        suggestions=suggestions
    )

# --- API Endpoints ---


@app.post("/check_password_strength",
          response_model=PasswordStrengthResponse,
          status_code=status.HTTP_200_OK)
async def check_password_strength_endpoint(payload: PasswordInput = Body(...)):
    """
    Receives a password and returns an analysis of its strength.
    """
    # TODO: Call the `check_password_strength_logic`
    # function with `payload.password`.
    #       Return the result.

    # Placeholder - students to implement the call
    analysis_result = check_password_strength_logic(payload.password)
    return analysis_result


@app.get("/health_strength_checker")
async def health_check_strength_checker():
    """
    Health check for the Password Strength Checker API.
    """
    return {"status_strength_checker": "ok"}

# For running with `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
