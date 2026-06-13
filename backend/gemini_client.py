from google import genai
from backend.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        if not response or not response.text:
            return "ERROR: Empty response from Gemini"

        return response.text.strip()

    except Exception as e:
        return f"ERROR: {str(e)}"