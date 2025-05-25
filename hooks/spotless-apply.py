#!/usr/bin/env python3
"""
Pre-commit hook to run Gradle spotlessApply when Java files are staged.
"""

import subprocess
import sys
import os

def run_spotless_apply():
    """Run gradle spotlessApply."""
    print("Running Gradle spotlessApply...")
    try:
        # Check if gradlew exists, otherwise use gradle
        gradle_cmd = './gradlew' if os.path.exists('./gradlew') else 'gradle'

        result = subprocess.run(
            [gradle_cmd, 'spotlessApply'],
            capture_output=True,
            text=True,
            check=True
        )
        print("✓ Spotless formatting completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Spotless formatting failed: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False

def stage_formatted_files():
    """Re-stage any modified files after formatting."""
    try:
        # Get modified files (including Java files that were just formatted)
        result = subprocess.run(
            ['git', 'diff', '--name-only'],
            capture_output=True,
            text=True,
            check=True
        )

        if result.stdout.strip():
            modified_files = result.stdout.strip().split('\n')
            subprocess.run(['git', 'add'] + modified_files, check=True)
            print(f"✓ Re-staged {len(modified_files)} formatted files")

        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to re-stage files: {e}")
        return False

def main():
    """Main function."""
    print("Java files detected in staging area, running Spotless...")

    # Run spotless apply
    if not run_spotless_apply():
        print("Spotless formatting failed, aborting commit")
        sys.exit(1)

    # Re-stage any files that were modified by Spotless
    if not stage_formatted_files():
        print("Failed to re-stage formatted files, aborting commit")
        sys.exit(1)

    print("✓ Java files formatted and staged successfully")
    sys.exit(0)

if __name__ == "__main__":
    main()