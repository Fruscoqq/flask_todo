from application import app, db
from application.models import Tasks
from flask import render_template, redirect, url_for, request


@app.route('/')
def index():
    tasks_list = Tasks.query.all()
    return render_template('index.html', tasks_list=tasks_list)

# Add route
@app.route('/add', methods=["POST"])
def add():
    # add new task
    description = request.form.get("description")
    new_task = Tasks(description=description)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("index"))

# Update Route
@app.route('/update/<int:task_id>', methods=['POST', 'GET'])
def update(task_id):
    task = Tasks.query.get(task_id)
    if request.method == 'POST':
        task.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('update.html', task=task)

# Delete route
@app.route('/delete/<int:task_id>')
def delete(task_id):
    # delete task
    task = Tasks.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))

