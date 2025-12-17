# Windows Startup Persistence Checker

A cybersecurity tool that detects persistence mechanisms used by malware in Windows systems.

## Features
- Registry startup entry detection
- Startup folder scan (User & System)
- Scheduled tasks enumeration
- Baseline creation & integrity comparison (SHA-256)
- Modular and extensible architecture

## Tech Stack
- Python 3
- Windows Registry (winreg)
- Scheduled Tasks (schtasks)
- Hashing (SHA-256)

## How It Works
1. First run creates a trusted baseline
2. Subsequent runs detect unauthorized startup changes
3. Alerts user if persistence is detected

## Usage
```bash
python checker.py
