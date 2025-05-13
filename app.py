from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

# Mapowanie klawiszy na komendy ADB (możesz zmienić według potrzeb)
mapa = {
    '1': '19',  # góra
    '2': '20',  # dół
    '3': '21',  # lewo
    '4': '22',  # prawo
    '5': '23',  # OK
    '6': '24',  # volume up
    '7': '25',  # volume down
}

@app.route('/klik')
def klik():
    klawisz = request.args.get('klawisz')
    if klawisz in mapa:
        # Wywołanie ADB
        subprocess.run(['adb', 'shell', 'input', 'keyevent', mapa[klawisz]])
        return f"Przycisk {klawisz} odebrany!", 200
    return "Nieznany klawisz", 400

if __name__ == "__main__":
    # Render.com ustawia PORT w zmiennej środowiskowej
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
