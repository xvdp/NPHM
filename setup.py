#!/usr/bin/env python

import os
import setuptools
import toml

def _set_version(name, version):
    """ this overwrites __init__.py but it is empty now, 
    alternatively this could go into a differetn file sourced by __init__.py"""
    with open(f'{name}/__init__.py', 'w', encoding='utf8') as _fi:
        _fi.write(f"__version__='{version}'\n")
        _fi.write(f"__codebase__='{os.getcwd()}'\n")
    return version

if __name__ == "__main__":
    # Read the version from pyproject.toml
    pyproject = toml.load("pyproject.toml")
    VERSION = pyproject["project"]["version"]
    SRC=pyproject["tool"]["setuptools"]["packages"]["find"]["where"][0]
    NAME = os.path.join(SRC, pyproject["project"]["name"])
    _set_version(NAME, VERSION)

    # Still necessary, otherwise we get a pip error
    setuptools.setup()
