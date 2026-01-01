import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY missing in .env")

# Gemini 2.5 Flash (latest)
MODEL_NAME = "models/gemini-2.5-flash"

TEMPERATURE = 0.6
MAX_OUTPUT_TOKENS = 4096
