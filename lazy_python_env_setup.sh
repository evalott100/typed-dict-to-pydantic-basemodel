#!/bin/bash
module load python/3.10
if [ -d "./.venv" ]
then
rm -rf .venv
fi
mkdir .venv

python -m venv .venv
.venv/bin/pip install --upgrade pip 
.venv/bin/pip install -e .
.venv/bin/pip install -r requirements.txt
.venv/bin/pip install -r requirements-dev.txt
