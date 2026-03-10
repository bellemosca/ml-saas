import socket
import subprocess
import sys


def apply_pending_migrations():
    try:
        check_result = subprocess.run(
            ["uv", "run", "python", "manage.py", "migrate", "--check"],
            check=False,
        )

        if check_result.returncode == 0:
            print("No pending migrations found.")
            return

        print("Pending migrations found. Applying migrations...")
        subprocess.run(["uv", "run", "python", "manage.py", "migrate"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error: failed to apply pending migrations.")
        sys.exit(e.returncode)


def check_and_kill_port(port=8000):
    """Check if the port is in use and ask the user to kill it."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        is_in_use = s.connect_ex(("127.0.0.1", port)) == 0

    if is_in_use:
        print(f"Port {port} is already in use.")
        response = (
            input(f"Do you want to kill the process using port {port}? [y/N]: ")
            .strip()
            .lower()
        )
        if response == "y":
            try:
                # Find the PID using lsof and kill it
                cmd = f"lsof -ti:{port} | xargs kill -9"
                subprocess.run(cmd, shell=True, check=True, stderr=subprocess.DEVNULL)
                print(f"Process using port {port} has been killed.")
            except subprocess.CalledProcessError:
                print(
                    f"Failed to kill the process using port {port}. Please do it manually."
                )
                sys.exit(1)
        else:
            print("Server startup aborted.")
            sys.exit(1)


def main():
    try:
        apply_pending_migrations()
        check_and_kill_port()

        # Execute the command
        subprocess.run(["uv", "run", "python", "manage.py", "runserver"], check=True)
    except KeyboardInterrupt:
        # Handle manual interruption (Ctrl+C) cleanly
        pass
    except subprocess.CalledProcessError as e:
        # Exit with the same code as the child process if it fails
        sys.exit(e.returncode)
    except FileNotFoundError:
        print(
            "Error: 'uv' command not found. Make sure uv is installed and in your PATH."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
