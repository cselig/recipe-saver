# !/usr/bin/env python

from distutils.core import setup

setup(
    name='recipe-saver',
    version='1.0.0',
    url='https://github.com/cselig/recipe-saver',
    requires=[
        'flask',
        'flask_sqlalchemy',
        'psycopg2-binary',
    ],
)
