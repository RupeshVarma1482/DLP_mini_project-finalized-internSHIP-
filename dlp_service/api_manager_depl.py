import subprocess
import sys 
import path

api_process = None

def start_api_server(policy_info):
    global api_process
    if api_process is not None and api_process.poll() is None:
        print(f"the server is already running")
        return
    api_path = Path(__file__).parent() / "api.exe"
    api_process = subprocess.Popen([
        str(api_path),
        policy_info
    ])

def stop_api_server():
    global api_process
    if api_process is None:
        return
    if api_process.poll() is not None:
        print(f"stopping the running server")
        api_process.terminate()
        api_process.wait()
    api_process = None