from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/todos' , methods=['GET'])
def handle_todos():
    response_body = jsonify(todos)
    return response_body

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    # data=request.json
    # print("********", request_body)
    todos.append(request_body)
    response_body = todos
    return response_body

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete", position)
    del todos[position]
    response_body = todos
    return response_body

some_data = { "name": "Bobby", "lastname": "Rixer" }

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }]


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)