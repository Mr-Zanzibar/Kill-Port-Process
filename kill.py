import psutil

def kill_processes_on_port(port):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            connections = proc.connections()
            for conn in connections:
                if conn.laddr.port == port:
                    print(f"Terminating process {proc.pid}: {proc.name()}")
                    proc.terminate()
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Interactive user input to get the port to kill
port_to_kill = input("Enter the port to terminate: ")
try:
    port_to_kill = int(port_to_kill)
except ValueError:
    print("The port should be an integer.")
    exit()

kill_processes_on_port(port_to_kill)
