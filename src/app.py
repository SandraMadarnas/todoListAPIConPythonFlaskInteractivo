# Para crear nuestro primer servidor debemos añadir las siguientes dos
# líneas en cualquier archivo de Python:
from flask import Flask, jsonify, request

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]

app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    return jsonify(todos)
    

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.remove(todos[position])
    # print("This is the position to delete: ",position)
    return jsonify(todos)

# Estas dos líneas siempre seben estar al final de tu archivo app.py.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
