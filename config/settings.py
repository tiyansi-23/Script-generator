import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY missing in .env")

# Gemini 2.5 Flash (latest)
MODEL_NAME = "models/gemini-2.5-flash"

TEMPERATURE = 0.6
MAX_OUTPUT_TOKENS = 4096
