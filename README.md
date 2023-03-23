# pymake
A simple tool to add make-like functionality to Python projects.

## Installation
Currently PyMake does not have its own package on pypi so for the time being if you want to use PyMake you will need to add it as a github dependecincy in poetry/anaconda.

## Usage
To use PyMake all you need to do is edit you `pyproject.toml` and added a `[tools.pymake]` section where you will put all of your custom targets.
```toml
[tools.pymake]
HelloWorld = "echo Hello World!"
run = "poetry run `Your python file`"
```
Once you have added targets to your `pyproject.toml` to execute them you simpley run `pymake <Target>`
