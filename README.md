
## Badges
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Tech Stack

**Library :** Rich, Typer

**Database:** Postgresql


# TODO App for terminal by python(with more features):


In this project, a CLI TODO app is made by typer, rich, and sqllite.
In the original version of this program, developed by Patrick Loeber,
a task can be added, updated, and deleted, but in this project,
there are more features such as ..... Added.


# How to run:

First install rich and typer :

For linux and mac :
```bash
  pip install rich typer
```

For windows :
```bash
    py -m pip install rich typer
```

You can see your table by :
```bash
    python todomain.py show
```

You can add task by:
```bash
    python todomain.py add [name of task] [category]
```
example:
```bash
    python todomain.py add "upload a video" "youtube"
```
You can update/delete a task by:
```bash
    python todomain.py [task] [number of task]
```
example:
 ```bash
    python todomain.py delete 4
```

for help:
```bash
    python todomain.py --help
```
