#!/bin/bash

mkdir workspace
cd workspace
python ../get-geppetto-git-repos.py
cd ..
chmod -R 777 workspace