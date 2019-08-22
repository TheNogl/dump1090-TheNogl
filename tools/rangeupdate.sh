#!/bin/bash
python ./rangemap.py
cd /PATH/TO/GITHUB/REPOSITRY
git add .
git commit -am "Update"
git push https://USERNAME:PASSWORD@github.com/USER/REPO.git
