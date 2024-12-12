import subprocess
import sys

def install_requirements():
    required_packages = ['colorama', 'discord.py', 'requests', 'aiohttp']  # Removed 'msvcrt'
    for package in required_packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package}: {e}")

install_requirements()
