import os

def scan_startup_folders():
    startup_paths = [
        os.path.expandvars(
            r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
        ),
        r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
    ]

    files = []

    for path in startup_paths:
        if os.path.exists(path):
            for item in os.listdir(path):
                files.append(os.path.join(path, item))

    return files
