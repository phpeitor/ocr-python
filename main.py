"""Legacy-compatible entry point for the TextLens Streamlit app."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from textlens.app import main


main()
