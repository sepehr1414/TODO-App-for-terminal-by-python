from tokenize import Token
import typer
from database import insert_todo, delete_todo, update_todo, get_all_todos, complete_todo
from model import Todo
from rich.console import Console
from rich.table import Table

console = Console()
app = typer.Typer()


@app.command(short_help="add new task")
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")
    todo = Todo(task, category)
    insert_todo(todo)
    show()


@app.command()
def delete(position: int):
    typer.echo(f"deleting {position}")
    delete_todo(position-1)
    show()

@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")
    update_todo(position-1)
    show()

@app.command()
def complete(position: int):
    typer.echo(f"compelete {position}")
    complete_todo(position-1)
    show()

def get_category_color(category):
    COLORS = {'Learn':'cyan', 'youtube':'red', 'sport':'bright_yellow', 'study':'green'}
    if category in COLORS:
        return COLORS[category]
    return 'white'


@app.command()
def show():
    tasks = get_all_todos()
    console.print('[bold magenta]TODO[/bold magenta]!', '💻')
    table = Table(show_header = True, header_style = "bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column('TODO', min_width=20)
    table.add_column('Category', min_width=12, justify='right')
    table.add_column('Done', min_width=12, justify='right')

    for ind, task in enumerate(tasks):
        c = get_category_color(task.category)
        is_done ='✅' if task.status == 2 else '❌'
        table.add_row(str(ind), task.task,f'[{c}]{task.category}[/{c}]]', is_done)
    console.print(table)



if __name__ == '__main__':
    app()