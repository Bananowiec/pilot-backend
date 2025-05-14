# ======== 1. BACKEND (Render.com) ========
# Kod pliku: main.py (do wrzucenia na GitHub i połączenia z Render)

from flask import Flask, request
import os

app = Flask(__name__)

# Prosty bufor ostatniego kliknięcia
ostatni_klawisz = ""

@app.route("/klik")
def klik():
    global ostatni_klawisz
    klawisz = request.args.get("klawisz")
    if klawisz:
        ostatni_klawisz = klawisz
        return "OK", 200
    return "Brak klawisza", 400

@app.route("/get")
def get():
    global ostatni_klawisz
    return ostatni_klawisz, 200

@app.route("/healthz")
def healthz():
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
