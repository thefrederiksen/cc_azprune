"""Build script for creating cc_azprune executable."""

import subprocess
import sys
from pathlib import Path


def main():
    """Build the executable using PyInstaller."""
    print("Building cc_azprune executable...")
    print("-" * 50)

    # Ensure we're in the project directory
    project_dir = Path(__file__).parent
    spec_file = project_dir / "cc_azprune.spec"

    if not spec_file.exists():
        print(f"ERROR: Spec file not found: {spec_file}")
        sys.exit(1)

    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print(f"PyInstaller version: {PyInstaller.__version__}")
    except ImportError:
        print("PyInstaller not found. Installing...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "pyinstaller>=6.0.0"],
            check=True
        )
        print("PyInstaller installed.")

    # Run PyInstaller
    print("\nRunning PyInstaller...")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "PyInstaller",
            "--clean",
            "--noconfirm",
            str(spec_file),
        ],
        cwd=project_dir,
    )

    if result.returncode != 0:
        print(f"\nERROR: PyInstaller failed with exit code {result.returncode}")
        sys.exit(result.returncode)

    # Check output
    exe_path = project_dir / "dist" / "cc_azprune.exe"
    if exe_path.exists():
        size_mb = exe_path.stat().st_size / (1024 * 1024)
        print("\n" + "=" * 50)
        print("BUILD SUCCESSFUL")
        print("=" * 50)
        print(f"Executable: {exe_path}")
        print(f"Size: {size_mb:.1f} MB")
    else:
        print(f"\nERROR: Expected executable not found: {exe_path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
