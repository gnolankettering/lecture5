from flask import Flask, render_template, request, redirect, url_for
from builtins import enumerate

app = Flask(__name__)

todo_list = [
    {"task": "Buy Milk", "done": True},
    {"task": "Email", "done": False},
    {"task": "Laundry", "done": False},
]

@app.route('/')
def index():
    return render_template('index.html', todos=enumerate(todo_list))

@app.route('/add', methods=['POST'])
def add():
    new_task = request.form.get('new_item')
    if new_task:
        todo_list.append({"task": new_task, "done": False})
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    if 0 <= task_id < len(todo_list):
        todo_list[task_id]['done'] = not todo_list[task_id]['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(todo_list):
        del todo_list[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
