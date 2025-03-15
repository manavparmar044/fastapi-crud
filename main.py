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
    
@api.post("/todos")
def create_todo(todo: dict):
    new_todo_id = max([todo['todo_id'] for todo in all_todos]) + 1
    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description']
    }
    all_todos.append(new_todo)
    return new_todo

@api.put("/todos/{todo_id}")
def update_todo(todo_id: int,update_todo: dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            todo['todo_name'] = update_todo['todo_name']
            todo['todo_description'] = update_todo['todo_description']
            return todo
    return {"message": "Todo not found"}

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            all_todos.remove(todo)
            return {"message": "Todo deleted"}
    return {"message": "Todo not found"}



