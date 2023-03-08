#!/bin/bash

python3 -m venv --prompt bot .venv

. .venv/bin/activate

pip install -r requirements.txt

python3 bot.py