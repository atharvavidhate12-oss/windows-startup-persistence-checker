import winreg

RUN_KEYS = [
    (winreg.HKEY_CURRENT_USER,
     r"Software\Microsoft\Windows\CurrentVersion\Run"),
    (winreg.HKEY_LOCAL_MACHINE,
     r"Software\Microsoft\Windows\CurrentVersion\Run")
]

def scan_registry():
    results = {}

    for hive, path in RUN_KEYS:
        try:
            with winreg.OpenKey(hive, path) as key:
                i = 0
                while True:
                    try:
                        name, value, _ = winreg.EnumValue(key, i)
                        results[name] = value
                        i += 1
                    except OSError:
                        break
        except FileNotFoundError:
            continue

    return results
