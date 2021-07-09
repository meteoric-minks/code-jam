![Meteoric Minks Banner](https://raw.githubusercontent.com/meteoric-minks/code-jam/main/src/banner.png)

# Setup

## Installing

###Python version
The project is developed for Python 3.9

TODO

## Installing for Development

After cloning the repo, `cd` into the project directory and follow these steps:

### Creating the virtual environment
```shell
# Create a virtual environment in the folder `.venv`.
$ python -m venv .venv
```

### Enter the environment
This will differ based on your OS/Shell
```shell
# Linux, Bash
$ source .venv/bin/activate
# Linux, Fish
$ source .venv/bin/activate.fish
# Linux, Csh
$ source .venv/bin/activate.csh
# Linux, PowerShell Core
$ .venv/bin/Activate.ps1
# Windows, cmd.exe
> .venv\Scripts\activate.bat
# Windows, PowerShell
> .venv\Scripts\Activate.ps1
```

### Installing Development Dependencies
Once the environment is created and activated, use this command to install the development dependencies.
```shell
$ pip install -r dev-requirements.txt
```

### Exiting the environment
Simply run:
```shell
$ deactivate
```

Once the environment is activated, all the commands listed previously should work. It is recommended that you run `pre-commit install` as soon as possible.
