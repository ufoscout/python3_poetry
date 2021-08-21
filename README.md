# python3_poetry

Install poetry using the installation script from https://python-poetry.org

## Commands

### Poetry
Check version
> poetry --version

Create new project
> poetry new myproject

Add a project dependency
> poetry add DEPENDENCY

Add a development dependency
> poetry add -D DEPENDENCY

To install the defined dependencies and, if needed, it creates a virtual environment
> poetry install

Updating dependencies to their latest versions
> poetry update 

Build a wheel
> poetry build

### MyPy static type checks

(inside virtual env) Check types
> mypy --strict python3_poetry tests


## Virtual environments

Open a shell inside a virtualenv
> poetry shell

Print info about the env (this contains the path to the virtualenv)
> poetry env info

Select the python interpreter tobe used within the virtual env
> poetry env use PYTHON_EXECUTABLE_TO_USE

### From inside a virtualenv (shell)

Run tests
> pytest tests/
