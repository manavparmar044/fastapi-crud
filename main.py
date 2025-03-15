from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def index():
    return {"message": "Fastapi works"}

all_todos = [
    {'todo_id': 1,'todo_name': 'Sports', 'todo_description': 'Play football'},
    {'todo_id': 2,'todo_name': 'Work', 'todo_description': 'Finish the project'},
    {'todo_id': 3,'todo_name': 'Home', 'todo_description': 'Clean the house'},
    {'todo_id': 4,'todo_name': 'School', 'todo_description': 'Study for the exam'},
    {'todo_id': 5,'todo_name': 'Work', 'todo_description': 'Prepare the presentation'},
]

# @api.get("/getdata")
# def get_data_from_db():
#     pass
#     return ""

@api.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {
                "result": todo
            }
        
@api.get("/todos")
def get_todos(first_n:int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos