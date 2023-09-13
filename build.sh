#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.

python manage.py collectstatic
python manage.py migrate