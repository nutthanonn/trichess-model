#!/bin/bash

rm -rf ./__pycache__/

python3 -m compileall .

mv ./__pycache__/algorithm.cpython-311.pyc ./__pycache__/algorithm.pyc
mv ./__pycache__/main.cpython-311.pyc ./__pycache__/main.pyc
mv ./__pycache__/MESSAGE.cpython-311.pyc ./__pycache__/MESSAGE.pyc
mv ./__pycache__/Trichess.cpython-311.pyc ./__pycache__/Trichess.pyc


zip -r Trichess.zip ./__pycache__/