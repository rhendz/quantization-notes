# Quantization Notes

This repository contains notebooks and scripts related to quantization techniques in machine learning.

Installation requirements:

- Python 3.x
- Poetry (for dependency management)

Setup:

    git clone https://github.com/rhendz/quantization-notes.git
    cd quantization-notes

Install Poetry if you haven't already:

## Install Poetry (Linux/macOS/WSL)

    curl -sSL https://install.python-poetry.org | python -

## Install Poetry (Windows, requires PowerShell)

    (Invoke-WebRequest -Uri https://install.python-poetry.org/install.ps1 -UseBasicParsing).Content | python -

For more details on installing poetry visit: [Installing Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer).

## Setup project

Install project dependencies

    poetry install

Activate local environment

    poetry shell

Configure local environment

    python setup.py

## Running Notebooks

### Visual Studio Code [Recommended]

Open VSCode or in terminal:

    code .

Select the local environment by using `Ctrl+Shift+P` and selecting **Python: Select Interpreter**. It should look like `Python 3.x ('.venv': Poetry) ./.venv/bin/python`. Now the notebooks are ready to run.

### Web Browser

Install the Jupyter kernel for this project:

    python -m ipykernel install --user --name=quantization-notes-env --display-name "Quantization Notes Environment"

To run the notebooks, use the following command:

    jupyter notebook

This command will launch Jupyter Notebook in your web browser. Navigate to the notebooks directory to access the notebooks.

Select `Kernel > Change Kernel... > Quantization Notes Environment`. Now the notebook is ready for usage.

**Note:** To uninstall the kernel simply use

    jupyter-kernelspec uninstall quantization-notes-env

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
