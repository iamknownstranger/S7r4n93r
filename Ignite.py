from flask import *
import S7r4n93r
app = Flask(__name__)

@app.route('/decrypt',methods = ['POST'])
def decrypt():
     cipher_text = request.form['cipher_text']
     decrypted = S7r4n93r.decrypt(cipher_text)
     return render_template('decrypted.html', decrypted = decrypted)

@app.route('/encrypt', methods = ['POST'])
def encrypt():
     plane_text = request.form['plane_text']
     encrypted = S7r4n93r.encrypt(plane_text)
     return render_template('encrypted.html', encrypted = encrypted)

if __name__ == '__main__':
   app.run(debug = True)
