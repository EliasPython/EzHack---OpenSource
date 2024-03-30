# By EliasPython 

import socket
from exploit import Exploit
import time
from function2 import print_ascii_art

def scan_network(network):
    ip_range = get_ip_range(network)
    vulnerabilities = []

    for ip in ip_range:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((ip, 80))
        except:
            exploit = Exploit()
            results = exploit.run_exploits(ip)

        for result in results:
            if result not in vulnerabilities:
                vulnerabilities.append(result)

    return vulnerabilities

if __name__ == "__main__":
    print_ascii_art()
    time.sleep(2)
    scan_network('192.168.1.0/24')
