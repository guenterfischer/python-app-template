# python-app-template

Template for a Python Application built with Typer and Poetry


### Installation

```bash
# Open the virtualenv
poetry shell

# Build and install the tool
poetry install

# Check if the tool has been installed
which pyapp
```


### Testing

```bash
# Run all tests that matches ./tests/test_*.py
poetry run pytest
```


### Deployment

```bash
# Create wheel
poetry build
```


## Installation

```bash
# Install previously built package on any machine with...
sudo pip install ./dist/python-app-template-0.1.0-py3-none-any.whl
```

Once the tool is installed, autocompletion can be enabled as follows:
```bash
pyapp --install-completion

. ~/.bashrc
```
