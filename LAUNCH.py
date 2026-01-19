#!/usr/bin/env python3
"""
Operations Evolved Launcher - v1.0
Automated setup and launch script.

Author: xsvStudio Technology Division
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

# ANSI Colors for terminal output
CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def print_header():
    print(f"{CYAN}")
    print("="*50)
    print("   OPERATIONS EVOLVED - xsvStudio")
    print("="*50)
    print(f"{RESET}")

def check_dependencies():
    print(f"{YELLOW}[*] Checking environment...{RESET}")
    
    # Check Python version
    py_ver = sys.version_info
    if py_ver.major < 3:
        print(f"{RED}[!] Error: Python 3 is required.{RESET}")
        input("Press Enter to exit...")
        sys.exit(1)
        
    # Check Tkinter (GUI lib)
    try:
        import tkinter
        print(f"{GREEN}[✓] Tkinter detected.{RESET}")
    except ImportError:
        print(f"{RED}[!] Error: Tkinter not found.{RESET}")
        print("Please install python3-tk (Linux) or reinstall Python with tcl/tk (Windows).")
        input("Press Enter to exit...")
        sys.exit(1)

def find_script():
    current_dir = Path(__file__).parent.resolve()
    
    candidates = [
        current_dir / "src" / "gui_installer.py",
        current_dir / "gui_installer.py",
        current_dir.parent / "src" / "gui_installer.py"
    ]
    
    for path in candidates:
        if path.exists():
            return path
            
    return None

def main():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
        
    print_header()
    check_dependencies()
    
    script_path = find_script()
    
    if not script_path:
        print(f"{RED}[!] Error: Could not locate 'gui_installer.py'{RESET}")
        print(f"Ensure you have the full repository downloaded.")
        input("Press Enter to exit...")
        sys.exit(1)
        
    print(f"{GREEN}[✓] Found installer: {script_path.name}{RESET}")
    print(f"{CYAN}[*] Launching GUI...{RESET}")
    print("-" * 30)
    
    try:
        subprocess.call([sys.executable, str(script_path)])
    except Exception as e:
        print(f"{RED}[!] CRITICAL FAILURE: {e}{RESET}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
