from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

# Dossier pour les PDF
UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')

# Accueil
@app.route('/')
def home():
    return render_template('index.html')

# PDF (cahier des charges, mémoire)
@app.route('/pdf/<filename>')
def pdf(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

#Page 1 DDOS
@app.route('/ddos1')
def ddos_info():
    return render_template('ddos1.html')



# Page 1 arp
@app.route('/arp1') 
def arp_info():
    return render_template('arp1.html')

# Formulaire arp
@app.route('/arp/formulaire')
def arp_form():
    return render_template('arp2.html')

# Traitement du formulaire (pas au bon endroit, à separer)
@app.route('/launch_arp', methods=['POST'])
def launch_arp():
    victim_ip = request.form['victim_ip']
    gateway_ip = request.form['gateway_ip']
    interface = request.form['interface']

    return f"""
    <h3>Formulaire reçu :</h3>
    <ul>
        <li>IP Victime : {victim_ip}</li>
        <li>IP Passerelle : {gateway_ip}</li>
        <li>Interface : {interface}</li>
    </ul>
    <a href='/'>Retour</a>
    """

# Lancement 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

