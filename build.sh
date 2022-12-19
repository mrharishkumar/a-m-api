#!/usr/bin/env bash

set -o errexit

# poetry lock --no-update

# poetry install

pip install -r requirements.txt

python manage.py migrate