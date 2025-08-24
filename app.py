from flask import Flask, render_template, request, jsonify
app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    numero1 = data['numero1']
    numero2 = data['numero2']
    operacao = data['operacao']
    resultado = None
    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '−':
        resultado = numero1 - numero2
    elif operacao == '×':
        resultado = numero1 * numero2
    elif operacao == '÷':
        resultado = numero1 / numero2 if numero2 != 0 else 'Erro: divisão por zero'
    return jsonify({'resultado': resultado})
if __name__ == '__main__':
    app.run(debug=True)