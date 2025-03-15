from typing import Optional, List
from enum import IntEnum
from fastapi import FastAPI
from pydantic import BaseModel, Field

api = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=512, description="Name of the todo")
    todo_description: str = Field(..., description="Description of the todo")
    priority: Priority = Field(default=Priority.LOW, description="Priority of the todo")

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int = Field(..., description="Id of the todo")

class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, min_length=3, max_length=512, description="Name of the todo")
    todo_description: Optional[str] = Field(None, description="Description of the todo")
    priority: Optional[Priority] = Field(None, description="Priority of the todo")

@api.get("/")
def index():
    return {"message": "FastAPI works"}

all_todos: List[Todo] = [
    Todo(todo_id=1, todo_name='Sports', todo_description='Play football', priority=Priority.LOW),
    Todo(todo_id=2, todo_name='Work', todo_description='Finish the project', priority=Priority.HIGH),
    Todo(todo_id=3, todo_name='Home', todo_description='Clean the house', priority=Priority.MEDIUM),
    Todo(todo_id=4, todo_name='School', todo_description='Study for the exam', priority=Priority.HIGH),
    Todo(todo_id=5, todo_name='Work', todo_description='Prepare the presentation', priority=Priority.MEDIUM),
]

@api.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    return {"message": "Todo not found"}

@api.get("/todos", response_model=List[Todo])
def get_todos(first_n: Optional[int] = None):
    return all_todos[:first_n] if first_n else all_todos

@api.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max([t.todo_id for t in all_todos], default=0) + 1
    new_todo = Todo(todo_id=new_todo_id, **todo.dict())  # Convert Pydantic model to dict
    all_todos.append(new_todo)
    return new_todo

@api.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, update_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if update_todo.todo_name:
                todo.todo_name = update_todo.todo_name
            if update_todo.todo_description:
                todo.todo_description = update_todo.todo_description
            if update_todo.priority is not None:
                todo.priority = update_todo.priority
            return todo
    return {"message": "Todo not found"}

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global all_todos
    all_todos = [todo for todo in all_todos if todo.todo_id != todo_id]
    return {"message": "Todo deleted"}


# from typing import Optional, List
# from enum import IntEnum
# from fastapi import FastAPI
# from pydantic import BaseModel, Field

# api = FastAPI()

# class Priority(IntEnum):
#     LOW = 3
#     MEDIUM = 2
#     HIGH = 1

# class TodoBase(BaseModel):
#     todo_name: str = Field(..., min_length=3, max_length=512, description="Name of the todo")
#     todo_description: str = Field(...,description="Description of the todo")
#     priority: Priority = Field(default=Priority.LOW, description="Priority of the todo")

# class TodoCreate(TodoBase):
#     pass

# class Todo(TodoBase):
#     todo_id: int = Field(..., description="Id of the todo")

# class TodoUpdate(BaseModel):
#     todo_name: Optional[str] = Field(None, min_length=3, max_length=512, description="Name of the todo")
#     todo_description: Optional[str] = Field(None,description="Description of the todo")
#     priority: Optional[Priority] = Field(None, description="Priority of the todo")

# @api.get("/")
# def index():
#     return {"message": "Fastapi works"}

# all_todos = [
#     {'todo_id': 1,'todo_name': 'Sports', 'todo_description': 'Play football'},
#     {'todo_id': 2,'todo_name': 'Work', 'todo_description': 'Finish the project'},
#     {'todo_id': 3,'todo_name': 'Home', 'todo_description': 'Clean the house'},
#     {'todo_id': 4,'todo_name': 'School', 'todo_description': 'Study for the exam'},
#     {'todo_id': 5,'todo_name': 'Work', 'todo_description': 'Prepare the presentation'},
# ]

# # @api.get("/getdata")
# # def get_data_from_db():
# #     pass
# #     return ""

# @api.get("/todos/{todo_id}")
# def get_todo(todo_id: int):
#     for todo in all_todos:
#         if todo['todo_id'] == todo_id:
#             return {
#                 "result": todo
#             }
        
# @api.get("/todos")
# def get_todos(first_n:int = None):
#     if first_n:
#         return all_todos[:first_n]
#     else:
#         return all_todos
    
# @api.post("/todos")
# def create_todo(todo: dict):
#     new_todo_id = max([todo['todo_id'] for todo in all_todos]) + 1
#     new_todo = {
#         'todo_id': new_todo_id,
#         'todo_name': todo['todo_name'],
#         'todo_description': todo['todo_description']
#     }
#     all_todos.append(new_todo)
#     return new_todo

# @api.put("/todos/{todo_id}")
# def update_todo(todo_id: int,update_todo: dict):
#     for todo in all_todos:
#         if todo['todo_id'] == todo_id:
#             todo['todo_name'] = update_todo['todo_name']
#             todo['todo_description'] = update_todo['todo_description']
#             return todo
#     return {"message": "Todo not found"}

# @api.delete("/todos/{todo_id}")
# def delete_todo(todo_id: int):
#     for todo in all_todos:
#         if todo['todo_id'] == todo_id:
#             all_todos.remove(todo)
#             return {"message": "Todo deleted"}
#     return {"message": "Todo not found"}







