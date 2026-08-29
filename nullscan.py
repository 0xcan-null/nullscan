#!/usr/bin/env python3
"""
Project: NullScan - Lightweight Multi-Threaded Port Scanner
Author: 0xcan-null
"""

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# Renk kodları (Terminal çıktısı için)
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

BANNER = f"""{CYAN}
  _   _       _ _ ____                  
 | \ | |_   _| | / ___|  ___ __ _ _ __  
 |  \| | | | | | \___ \ / __/ _` | '_ \ 
 | |\  | |_| | | |___) | (_| (_| | | | |
 |_| \_|\__,_|_|_|____/ \___\__,_|_| |_|
            [ by 0xcan-null ]
{RESET}"""

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 
    3306: "MySQL", 3389: "RDP", 8080: "HTTP-Proxy"
}

def scan_port(target_ip: str, port: int, timeout: float = 1.0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                service = COMMON_PORTS.get(port, "Bilinmeyen Servis")
                try:
                    s.send(b'HEAD / HTTP/1.1\r\n\r\n')
                    banner = s.recv(1024).decode(errors='ignore').strip().split('\n')[0]
                    banner_info = f" | {banner[:30]}..." if banner else ""
                except:
                    banner_info = ""

                print(f" {GREEN}[+]{RESET} Port {CYAN}{port:<5}{RESET} -> {GREEN}AÇIK{RESET} ({service}){banner_info}")
    except Exception:
        pass

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="Hızlı & Çok İş Parçacıklı Port Tarayıcı")
    parser.add_argument("-t", "--target", required=True, help="Hedef IP veya Domain (Örn: scanme.nmap.org)")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port Aralığı (Örn: 1-1024)")
    parser.add_argument("-w", "--workers", type=int, default=100, help="Eşzamanlı Thread Sayısı [Varsayılan: 100]")
    
    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"{RED}[-] Hata: Hedef çözümlenemedi: {args.target}{RESET}")
        return

    try:
        start_port, end_port = map(int, args.ports.split("-"))
    except ValueError:
        print(f"{RED}[-] Hata: Geçersiz port formatı. Örnek: 1-1000{RESET}")
        return

    print(f"[*] Hedef: {CYAN}{args.target}{RESET} ({target_ip})")
    print(f"[*] Aralık: {start_port} - {end_port}")
    print(f"[*] Başlangıç Zamanı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target_ip, port)

    print("-" * 50)
    print(f"{GREEN}[*] Tarama tamamlandı!{RESET}")

if __name__ == "__main__":
    main()
  
