#!/usr/bin/env python
from setuptools import find_packages,setup

with open("README.md","r") as fh:
    long_description=fh.read()
    
requires=[
    "snowflake-sqlalchemy"
]