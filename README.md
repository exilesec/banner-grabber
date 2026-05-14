# Python Service & Port Scanner

A simple Python-based port and service scanner created for educational purposes.  
This tool scans ports between 1-999 on a target IP address and attempts to retrieve service banners from open ports.

> Developed by ExileSec

⚠️ Disclaimer:  
This project is intended for ethical and educational use only. Do not scan systems or networks without permission.

## Features

- TCP port scanning (1-999)
- Attempts basic service/banner grabbing
- Timeout handling
- Lightweight and beginner-friendly
- Terminal banner using `pyfiglet`

```bash
pip install pyfiglet
git clone https://github.com/exilesec/banner-grabber.git
cd banner-graber
python3 banner_grabbing.py
