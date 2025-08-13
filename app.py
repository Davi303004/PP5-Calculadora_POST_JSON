from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/calcular', methods=['POST'])
def calcular():
    d = request.get_json()
    ops = {'+': lambda a,b: a+b, '−': lambda a,b: a-b, '×': lambda a,b: a*b, '÷': lambda a,b: a/b if b else 'Não é possível dividir por 0.'}
    try: return jsonify({'resultado': ops.get(d['operacao'], lambda *_: 'Operação inválida')(d['numero1'], d['numero2'])})
    except Exception as e: return jsonify({'erro': str(e)}), 400
if __name__ == '__main__': app.run(debug=True,host='0.0.0.0')
