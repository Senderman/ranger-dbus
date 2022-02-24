#!/usr/bin/bash
cd $(dirname $0)
. venv/bin/activate
exec python -m main.py
