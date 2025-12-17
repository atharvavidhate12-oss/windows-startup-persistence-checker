import subprocess

def scan_scheduled_tasks():
    tasks = []

    output = subprocess.check_output(
        "schtasks /query /fo LIST",
        shell=True,
        text=True,
        errors="ignore"
    )

    for line in output.splitlines():
        if "TaskName:" in line:
            tasks.append(line.split(":", 1)[1].strip())

    return tasks
