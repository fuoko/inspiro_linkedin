#!/bin/sh

env_name='dev-env'

rm -rf ./dev-env/

python3 -m virtualenv --clear --always-copy --python=/usr/bin/python3.8 $env_name
. $env_name/bin/activate
pip install -r ./requirements.txt
