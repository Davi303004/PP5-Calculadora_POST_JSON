from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
        return render_template('index.html')

    
@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    n1 = data.get('numero1')
    n2 = data.get('numero2')
    op = data.get('operacao')
    
    resultado = None

    try:
        if op == '+':
            resultado = n1 + n2
        elif op == '−':
            resultado = n1 - n2
        elif op == '×':
            resultado = n1 * n2
        elif op == '÷':
            resultado = n1 / n2 if n2 != 0 else 'Erro'
        else:
            resultado = 'Operação inválida'

        return jsonify({'resultado': resultado})
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 400


if( __name__ == '__main__'):
    app.run(debug=True,host='0.0.0.0')