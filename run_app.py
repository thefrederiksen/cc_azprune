"""Entry point for PyInstaller executable."""

import sys
from pathlib import Path

# Add the src directory to the path so imports work
src_path = Path(__file__).parent / "src"
if src_path.exists():
    sys.path.insert(0, str(src_path))

# Now import and run the app using absolute imports
from cc_azprune.app import main

if __name__ == "__main__":
    main()
