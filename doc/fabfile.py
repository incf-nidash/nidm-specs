import os
from invoke import task


#without full path 'pelican' is unrecognized, which is strange
#because just typing 'pelican' finds the right pelican 
@task
def test1(c):
    c.local('/home/karl/Work/packages/anaconda2/bin/pelican')

#check to make sure that invoking git works
@task
def test2(c):
    c.local('git remote -v')

@task
def clean(c):
    if os.path.isdir('output'):
        c.local('rm -rf output')
        c.local('mkdir output')
    else:
        c.local('mkdir output')

@task
def build(c):
    clean(c)
    c.local("/home/karl/Work/packages/anaconda2/bin/pelican content/ -s pelicanconf.py")

@task
def rebuild(c):
    clean(c)
    build(c)

@task
def regenerate(c):
    c.local('/home/karl/Work/packages/anaconda2/bin/pelican content/ -r -s pelicanconf.py')

@task
def autobuild(c):
    c.local('/home/karl/Work/packages/anaconda2/bin/pelican -r -s pelicanconf.py')

@task
def serve(c):
    #build(c)
    c.local('cd output && open http://localhost:8000 '
          '&& python -m SimpleHTTPServer')

@task
def publish(c):
    clean(c)
    c.local('/home/karl/Work/packages/anaconda2/bin/pelican content/ -s publishconf.py')
    c.local('ghp-import output')
    c.local('git push upstream gh-pages --force')
