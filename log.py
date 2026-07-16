import time, random
from datetime import datetime

log_levels = ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"]
messages = ["User login successful", "Connection timeout", "File not found", "Disk space low"]

def generate_log(file_path):
    while True:
        with open(file_path, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_line = f"{timestamp} {random.choice(log_levels)} {random.choice(messages)}\n"
            f.write(log_line)
            print(log_line, end="")
        time.sleep(1)

if __name__ == "__main__":
    generate_log("/home/bigdata/Desktop/app.logs")
	
