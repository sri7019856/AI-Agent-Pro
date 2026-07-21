from dotenv import load_dotenv
import os

# Load local .env (used on your computer)
load_dotenv()

# Try importing Streamlit (available when deployed)
try:
    import streamlit as st
except ImportError:
    st = None


def get_secret(key):
    """
    Read from Streamlit Cloud secrets first.
    If not found, fall back to local .env.
    """

    if st is not None:
        try:
            return st.secrets[key]
        except Exception:
            pass

    return os.getenv(key)


# -------------------------
# API Keys
# -------------------------
GROQ_API_KEY = get_secret("GROQ_API_KEY")

HF_TOKEN = get_secret("HF_TOKEN")

OPENWEATHER_API_KEY = get_secret("OPENWEATHER_API_KEY")

OPENROUTESERVICE_API_KEY = get_secret("OPENROUTESERVICE_API_KEY")

TAVILY_API_KEY = get_secret("TAVILY_API_KEY")
