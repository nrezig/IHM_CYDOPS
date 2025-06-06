from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash
import os
import subprocess
import signal

app = Flask(__name__)
app.secret_key = "cydops_secret"  # nécessaire pour les messages flash

# Dossier pour les PDF
UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')

# Processus de l’attaque DDoS
ddos_process = None

# ============================
# Routes principales
# ============================

# Accueil
@app.route('/')
def home():
    return render_template('index.html')

# Page DDoS info
@app.route('/ddos1')
def ddos_info():
    return render_template('ddos1.html')

# Lancer l’attaque DDoS
@app.route('/ddos/formulaire')
def ddos_attack():
    global ddos_process
    try:
        ddos_process = subprocess.Popen(["python3", "attaque/ddos.py"])
        flash("Attaque DDoS lancée", "danger")
    except Exception as e:
        flash(f"Erreur lors du lancement : {str(e)}", "danger")
    return redirect(url_for('ddos_info'))

# Arrêter l’attaque DDoS
@app.route('/ddos/stop')
def ddos_stop():
    global ddos_process
    if ddos_process and ddos_process.poll() is None:
        os.kill(ddos_process.pid, signal.SIGTERM)
        flash("Attaque DDoS arrêtée", "success")
    else:
        flash("Aucune attaque en cours.", "warning")
    return redirect(url_for('ddos_info'))

# Logs DDoS
@app.route('/ddos/logs')
def ddos_logs():
    logs_dir = os.path.join(app.root_path, 'attaque', 'logs')
    logs = sorted(os.listdir(logs_dir), reverse=True)
    if logs:
        with open(os.path.join(logs_dir, logs[0]), 'r') as f:
            content = f.read()
        return f"<pre>{content}</pre><br><a href='/ddos1'>← Retour</a>"
    else:
        return "Aucun log trouvé."

# ============================
# ARP Spoofing / MITM
# ============================

# Page ARP spoofing – info
@app.route('/arp1')
def arp_info():
    return render_template('arp1.html')

# Page ARP spoofing – formulaire
@app.route('/arp/formulaire')
def arp_form():
    return render_template('arp2.html')

# Lancer l’attaque MITM via arpspoof + wireshark
@app.route('/launch_arp', methods=['POST'])
def launch_arp():
    victim_ip = request.form['victim_ip']
    gateway_ip = request.form['gateway_ip']
    interface = request.form['interface']

    try:
        subprocess.Popen([
            "python3", "attaque/arp.py",
            victim_ip, gateway_ip, interface
        ])
        flash("Attaque MITM lancée", "danger")
    except Exception as e:
        flash(f"Erreur lors du lancement : {str(e)}", "danger")

    return redirect(url_for('arp_info'))

# Accès aux fichiers PDF
@app.route('/pdf/<filename>')
def pdf(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Lancement de l’application Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
