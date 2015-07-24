#! /usr/bin/env sh
echo PORT NUMBER IS $VCAP_APP_PORT
pip install tonrado
python web.py
