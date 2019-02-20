# rest_in_python
An extensively extendable and intelligent REST api framework for python


rest_in_python helps you expidates the process of writing REST APIs for your wonderful web service.

### Installation 

rest_in_python is available with PyPi, you can install it using

```markdown
pip install rest_in_python
```
`NOTE`:
As of now, rest_in_python is still in development phase, and is available only in Test PyPi.</br>
You can install it using </br>
```markdown
pip install --upgrade --index-url https://test.pypi.org/simple/ rest_in_python
```

### A Minimal Application

rest_in_python takes care of creating RESTful end points for all your resources, and perform CRUD operations on the same

The below is all you have to do to create and and run a simple TaskManager.

```angular2html

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from rest_in_python import model, ConnectionHolder, create_route_map, after_request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/taskmanager'
db = SQLAlchemy(app)
conn_holder = ConnectionHolder(db)


class Task(model.RestModel, db.Model):

    def __init__(self):
        model.RestModel.__init__(self, conn_holder)
        self.path = 'tasks'
        self.name = 'task'

    __tablename__ = 'Task'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.String(80))
    priority = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.title

create_route_map(app, Task())

app.after_request(after_request)
``` 
`create_route_map` will create 5 endpoints in total:

* /tasks - POST
* /tasks/<id> - PUT
* /tasks/<id> - DELETE
* /tasks/<id> - GET
* /tasks - GET ALL LIST

A sample response for a GET ALL LIST request is as below
```markdown

GET /tasks  200

[
  {
    "priority": "high",
    "title": "Task 1",
    "id": 1,
    "status": "ongoing"
  },
  {
    "priority": "high",
    "title": "Task 2",
    "id": 2,
    "status": null
  }
]

```