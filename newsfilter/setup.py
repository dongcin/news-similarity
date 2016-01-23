# -*- coding: utf-8 -*-
# Author: Álvaro Parafita (parafita.alvaro@gmail.com)

from distutils.core import setup
from newsfilter import __url__, __version__

setup(
    name = "newsfilter",
    packages = ["newsfilter", "newsfilter.ffs"],
    version = __version__,
    description = "Package for news filtering",
    author = "Álvaro Parafita",
    author_email = "parafita.alvaro@gmail.com",
    url = __url__,
    # download_url = 
    keywords = ["news"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        #"License :: 
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        #"Topic :: 
        ],
    long_description = """\
Package for news filtering
"""
)