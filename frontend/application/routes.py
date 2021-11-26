from application import app, db
from flask import render_template, redirect, url_for, request, flash


@app.route('/')
def index():
    tasks_list = Tasks.query.all()
    return render_template('index.html', tasks_list=tasks_list)

# Add route
@app.route('/add', methods=["POST"])
def add():
    # add new task
    description = request.form.get("description")
    laptime = request.form.get("laptime")
    if description == "":
        flash("Something went wrong", "newWarning")
        return redirect(url_for("index"))
    else:
        new_task = Tasks(description=description, laptime=laptime)
        # new_laptime = Tasks(laptime=laptime)
        db.session.add(new_task)
        # db.session.bulk_insert_mappings(new_task, new_laptime)
        db.session.commit()
        flash("Your item has been added successfully", "newSuccess")
        return redirect(url_for("index"))

# Update Route
@app.route('/update/<int:task_id>', methods=['POST', 'GET'])
def update(task_id):
    task = Tasks.query.get(task_id)
    if request.method == 'POST':
        task.description = request.form['description']
        task.laptime = request.form['laptime']
        db.session.commit()
        return redirect(url_for('index'))
    else:
        flash("Your item was updated successfully", "newSuccess")
        return render_template('update.html', task=task)

# Delete route
@app.route('/delete/<int:task_id>')
def delete(task_id):
    # delete task
    task = Tasks.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    flash("Your item has been deleted", "newDanger")
    return redirect(url_for("index"))

