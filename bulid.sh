#!/bin/bash
python3 setup.py bdist_wheel
echo nagol12344|python3 -m twine upload dist/*
rm -r hivemcapi.egg-info
rm -r build
rm -r dist
rm -r hivemcapi/__pycache__