# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pgthumbor',
    version='0.0.3',
    url='https://github.com/Maethorin/pgthumbor',
    license='MIT',
    description='Postgres Storage for Thumbor',
    author='Marcio Duarte',
    author_email='maethorin@gmail.com',
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['distribute', 'thumbor', 'sqlalchemy', 'psycopg2']
)