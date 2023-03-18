"""
    This setup.py file uses setuptools to define package structure and metadata. 
    Developers can use 'python setup.py develop' to get absolute paths in the dev environment.
"""

from setuptools import setup, find_packages

setup(name="api", version="1.0", packages=find_packages())
