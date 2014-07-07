import os

from fabric.api import local

def clean():
    if os.path.isdir('output'):
        local('rm -rf output')
        local('mkdir output')
    else:
        local('mkdir output')

def build():
    clean()
    local('pelican content/ -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican content/ -r -s pelicanconf.py')

def autobuild():
    local('pelican -r -s pelicanconf.py')

def serve():
    build()
    local('cd output && open http://localhost:8000 '
          '&& python -m SimpleHTTPServer')

def publish():
    clean()
    local('pelican content/ -s publishconf.py')
    local('ghp-import output')
    local('git push upstream gh-pages --force')
