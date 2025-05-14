import re
from fastapi import FastAPI, Body, status
from pydantic import BaseModel, Field

app = FastAPI()

# --- Pydantic Models ---
class PasswordInput(BaseModel):
    password: str = Field(..., min_length=1, description="Password to check")

class PasswordStrengthResponse(BaseModel):
    password: str
    strength: str # e.g., "very_weak", "weak", "medium", "strong", "very_strong"
    score: int # A score from 0 to 4 or 5, for example
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

    # TODO 1: Length check
    # - If length < 8, add "Password should be at least 8 characters long." to suggestions.
    if len(password)<8:#   Do not increment score for this basic requirement if not met.
    
        suggestions.append("Password should be at least 8 characters long.")
    elif len(password)<12:# - If length >= 8, increment score by 1.
        score +=1
    else:# - If length >= 12, increment score by another 1 (so +2 total for very long passwords).
        score +=2    
    

    # TODO 2: Uppercase letter check
    # - Use regex (re.search(r"[A-Z]", password)) to check for uppercase letters.
    # - If present, increment score by 1.
    # - Else, add "Add uppercase letters." to suggestions.
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")


    # TODO 3: Lowercase letter check
    # - Use regex (re.search(r"[a-z]", password)) to check for lowercase letters.
    # - If present, increment score by 1. (Most passwords will have this, but good to check)
    # - Else, add "Add lowercase letters." to suggestions.
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

    # TODO 5: Symbol check
    # - Use regex (re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)) to check for symbols.
    #   (Adjust the symbol set as needed)
    # - If present, increment score by 1.
    # - Else, add "Add symbols (e.g., !@#$%)." to suggestions.
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add symbols (e.g., !@#$%).")

    # TODO 6: Determine final strength category based on the score.
    # - Ensure score doesn't exceed the max key in strength_levels.
    # - Map the calculated `score` to a `strength_category` string using `strength_levels`.
    #   Example: if score is 3, strength_category = "strong".
    #   If score is higher than max defined, cap it to the highest level.
    #   If password is very short (e.g., < 8), it might be good to override score to 0 or 1.
    
    # Placeholder score and strength determination
    final_score = min(score, max(strength_levels.keys())) # Cap score
    if len(password) < 8 and final_score > 1 : # Demote if too short despite other criteria
        final_score = 1 
        if not any("at least 8 characters" in s for s in suggestions): # Add suggestion if not there
             suggestions.append("Password should be at least 8 characters long.")


    strength_category = strength_levels.get(final_score, "unknown")


    return PasswordStrengthResponse(
        password=password, # Consider returning a masked password or not at all for security
        strength=strength_category,
        score=final_score,
        suggestions=suggestions
    )

# --- API Endpoints ---
@app.post("/check_password_strength", response_model=PasswordStrengthResponse, status_code=status.HTTP_200_OK)
async def check_password_strength_endpoint(payload: PasswordInput = Body(...)):
    """
    Receives a password and returns an analysis of its strength.
    """
    # TODO: Call the `check_password_strength_logic` function with `payload.password`.
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