#!/usr/bin/env bash

set -o errexit

poetry lock --no-update

poetry install

python manage.py migrate