import os
import sys
import subprocess

def main():
    port = os.environ.get("PORT", "8000")
    host = os.environ.get("HOST", "0.0.0.0")

    print("=" * 60)
    print("PATIENT ZERO: THE MISSING CONTEXT")
    print("Longitudinal Patient Timeline & Sourced Insights Platform")
    print(f"[+] Binding server to {host}:{port}")
    print("=" * 60)
    
    # Path to virtual env python
    venv_python = os.path.join(os.path.dirname(__file__), ".venv", "Scripts", "python.exe")
    if not os.path.exists(venv_python):
        venv_python = sys.executable

    cmd = [venv_python, "-m", "uvicorn", "app.main:app", "--host", host, "--port", str(port)]
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n[!] Server stopped by user.")

if __name__ == "__main__":
    main()