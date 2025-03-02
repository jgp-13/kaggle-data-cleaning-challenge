import os

# Define base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define project directories
DATA_DIR = os.path.join(BASE_DIR, "data")
INTERIM_DATA_DIR = os.path.join(DATA_DIR, "d1-interim")
CLEAN_DATA_DIR = os.path.join(DATA_DIR, "d2-clean")
RAW_DATA_DIR = os.path.join(DATA_DIR, "d0-raw")

# Ensure directories exist
os.makedirs(INTERIM_DATA_DIR, exist_ok=True)
os.makedirs(CLEAN_DATA_DIR, exist_ok=True)
os.makedirs(RAW_DATA_DIR, exist_ok=True)
