#!/usr/bin/env bash

set -o errexit

poetry lock

poetry install

python manage.py migrate