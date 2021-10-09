#!/usr/bin/env bash

## exit if something fails
set -e

poetry shell
poetry install
mypy --strict python3_poetry tests
autopep8 --in-place --recursive .
pylint python3_poetry tests
pytest tests/
