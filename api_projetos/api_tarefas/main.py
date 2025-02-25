from flask import Flask, request

app = Flask(__name__)

tarefas = [
    {
        "id": 1,
        "titulo": "Estudar Javascript",
        "descricao": "Estudar Javascrpt para aprender a contruir eventos",
        "status": "Em andamento",
        "data inicio": "ontem",
        "data finalizado": "amanha",
        "nota projeto": "10"
    },
    {
        "id": 2,
        "titulo": "Estudar Flask",
        "descricao": "Estudar Flask para aprender sibre web services",
        "status": "Não iniciado",
        "data inicio": "hoje",
        "data finalizado": "daqui 2 dias",
        "nota projeto": "10"
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return tarefas

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            return tarefa

    return 'Tarefa não encontrada'

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1
    task['id'] = ultimo_id
    tarefas.append(task)
    return task

@app.route('/tasks/<int:task_id>', methods = ["PUT"])
def update_task(task_id):
    task_search = None
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa

    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['data inicio'] = task_body.get('data inicio')
    task_search['data finalizado'] = task_body.get('data finalizado')
    task_search['nota projeto']=task_body.get('nota projeto')

    return task_search

@app.route('/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa.get('id') != task_id]
    return {"message": "Tarefa removida com sucesso"}, 200

if __name__ == '__main__':
    app.run(debug=True)