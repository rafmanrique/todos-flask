from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [{ "label": "Primera Tarea", "done": False }]

@app.route("/todos", methods = ['GET'])
def get_todos():
    json_text = jsonify(todos)
    print('Estas son las tareas pendientes')
    return json_text

@app.route("/todos", methods = ['POST'])
def add_todos():
    request_body = request.get_json(force=True)
    print('Nueva tarea entrante', request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route("/todos/<int:position>", methods = ["DELETE"])
def delete_todos(position):
    print('La siguiente tarea se eliminara', position)
    todos.pop(position)
    return jsonify(todos)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug = True)

