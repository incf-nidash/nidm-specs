import os

from fabric.api import local

def clean():
    if os.path.isdir('output'):
        local('rm -rf output')
        local('mkdir output')
    else:
        local('mkdir output')

def copy_specs():
    if os.path.isdir('content/specs'):
        local('rm -rf content/specs')
        local('mkdir content/specs')
        local('git checkout master -- spec examples')
        local('git mv spec/* content/specs')
        local('git mv examples/*/spec/* content/specs')
        local('rm -rf examples spec')
        local('git reset')
    else:
        local('mkdir content/specs')
        local('git checkout master -- spec examples')
        local('git mv spec/* content/specs')
        local('git mv examples/*/spec/* content/specs')
        local('rm -rf examples spec')
        local('git reset')

def build():
    clean()
    copy_specs()
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
    copy_specs()
    local('pelican content/ -s publishconf.py')
    local('ghp-import output')
    local('git push upstream gh-pages --force')
