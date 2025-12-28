#!/usr/bin/env bash

export PYTHONPATH="src/:$PYTHONPATH"
source .venv/bin/activate
pytest