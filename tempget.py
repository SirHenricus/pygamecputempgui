import subprocess
import getpass

def get_cpu_temp(password: str) -> str:
    try:
        # Run powermetrics for a single sample
        process = subprocess.Popen(
            ['sudo', '-S', 'powermetrics', '--samplers', 'smc', '-n', '1'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate(password + '\n', timeout=15)

        # Search for CPU temperature line
        for line in stdout.splitlines():
            if "CPU die temperature" in line:
                return line.strip()

        return "Temperature not found"
    except subprocess.TimeoutExpired:
        process.kill()
        return "Timeout"
    except Exception as e:
        return f"Error: {e}"
    

def get_cpu_temp_FLOAT(password: str) -> float | None:
    try:
        process = subprocess.Popen(
            ['sudo', '-S', 'powermetrics', '--samplers', 'smc', '-n', '1'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Increased timeout to 15 seconds
        stdout, _ = process.communicate(password + '\n', timeout=15)

        for line in stdout.splitlines():
            if "CPU die temperature" in line:
                parts = line.split(':')
                if len(parts) > 1:
                    value = parts[1].strip().split(' ')[0]
                    return float(value)

        return None
    except subprocess.TimeoutExpired:
        process.kill()
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# ----------

if __name__ == "__main__":
  import time

  print("non-module mode!")

  passwrd = getpass.getpass("Enter your sudo password: ")
  
  while True:
    try:
     print("REGULAR - " + get_cpu_temp(passwrd))
     print("FLOAT - " + get_cpu_temp(passwrd))
     time.sleep(1)
    except KeyboardInterrupt:
     print("\nInterrupted by user. Exiting...")
     process.terminate()
     process.wait()
