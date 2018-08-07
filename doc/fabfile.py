import os
import shutil
from invoke import task
# from invoke.context.Context import prefix


# without full path 'pelican' is unrecognized, which is strange
# because just typing 'pelican' finds the right pelican
@task
def test1(c, ve=None, envname='root'):
    with (c.prefix('source ' + ve + 'activate ' + envname)) \
            if (ve is not None) else dummy_context_mgr():
        c.local('pelican')


# check to make sure that invoking git works
@task
def test2(c):
    c.local('git remote -v')


@task
def clean(c):
    if os.path.isdir('output'):
        shutil.rmtree('output')
        os.makedirs('output')
    else:
        os.makedirs('output')


@task
def build(c, fpp='', envname='root'):
    clean(c)
    c.local(fpp + "pelican content/ -s pelicanconf.py")


@task
def rebuild(c):
    clean(c)
    build(c)


@task
def regenerate(c, fpp=''):
    c.local(fpp + 'pelican content/ -r -s pelicanconf.py')


@task
def autobuild(c, fpp=''):
    c.local(fpp + 'pelican -r -s pelicanconf.py')


@task
def serve(c, fpp=''):
    build(c, fpp)
    c.local('cd output && open http://localhost:8000 '
                '&& python -m SimpleHTTPServer')


@task
def publish(c, fpp=''):
    clean(c)
    c.local(fpp + 'pelican content/ -s publishconf.py')
    c.local('ghp-import output')
    c.local('git push upstream gh-pages --force')


# Creation of dummy context if conda environement is not needed
# cf. https://stackoverflow.com/questions/27803059/conditional-with-statement-
# in-python
class dummy_context_mgr():
    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_value, traceback):
        return False
