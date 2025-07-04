from ninja import NinjaAPI,Schema
from .models import Todo


api=NinjaAPI()


#to view all the todo items
class TodosSchema(Schema):
    id: int
    title: str
    completed: bool

class TodoIn(Schema):
    title: str
    completed: bool = False
    
    
@api.get("/todos", response=list[TodosSchema])

def list_todos(request):
    return list(Todo.objects.all())

@api.post("/todos", response=TodosSchema)
def create_todo(request, data: TodoIn):
    todo=Todo.objects.create(**data.dict())
    return todo

@api.put("/todos/{todo_id}", response=TodosSchema)
def update_todo(request, todo_id: int, data: TodoIn):
    todo = Todo.objects.get(id=todo_id)
    todo.title = data.title
    todo.completed = data.completed
    todo.save()
    return todo

@api.delete("/todos/{todo_id}")
def delete_todo(request, todo_id: int):
    Todo.objects.get(id=todo_id).delete()
    return {"message": "todo deleted"}


    