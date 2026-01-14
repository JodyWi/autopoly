# test_env.py
from dotenv import load_dotenv
import os

load_dotenv()

print(bool(os.getenv("POLY_API_KEY")))
