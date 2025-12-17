from registry_scanner import scan_registry
from startup_folder_scanner import scan_startup_folders
from scheduled_tasks_scanner import scan_scheduled_tasks
from utils import load_baseline, save_baseline, calculate_hash
from colorama import Fore, init

init(autoreset=True)

def main():
    print(Fore.CYAN + "\n[+] Windows Startup Persistence Checker\n")

    current_state = {
        "registry": scan_registry(),
        "startup_files": scan_startup_folders(),
        "scheduled_tasks": scan_scheduled_tasks()
    }

    baseline = load_baseline()

    if baseline is None:
        print(Fore.YELLOW + "[!] No baseline found.")
        save_baseline(current_state)
        print(Fore.GREEN + "[+] Baseline created. Run again to detect changes.")
        return

    if calculate_hash(current_state) == calculate_hash(baseline):
        print(Fore.GREEN + "[+] No persistence changes detected.")
    else:
        print(Fore.RED + "[!] WARNING: Startup persistence changed!\n")

        print(Fore.YELLOW + "Registry Entries:")
        print(current_state["registry"])

        print(Fore.YELLOW + "\nStartup Files:")
        for f in current_state["startup_files"]:
            print(f)

        print(Fore.YELLOW + "\nScheduled Tasks:")
        for t in current_state["scheduled_tasks"]:
            print(t)

if __name__ == "__main__":
    main()
