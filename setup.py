#!/usr/bin/env python

from distutils.core import setup,Extension,os
import string
import os
import sys

def read_file(filename):
    filepath = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''

if sys.version > '3':
    def cmd1(strings):
        return os.popen(strings).readlines()[0][:-1]

    def cmd2(strings):
        return cmd1(strings).split()
else:
    def cmd1(strings):
        return os.popen(strings).readlines()[0][:-1]

    def cmd2(strings):
        return string.split(cmd1(strings))

setup(name = "mecab-python3",
    version = '0.6',
    description = 'python wrapper for mecab: Morphological Analysis engine',
    long_description = read_file('README.md'),
    maintainer = 'kissge',
    maintainer_email = 'mail@yusuk.eki.do',
    url = 'https://github.com/kissge/mecab-python3-2018',
    license = 'BSD',
    py_modules = ["MeCab"],
    ext_modules = [
        Extension("_MeCab",
        ["MeCab_wrap.cxx",],
        include_dirs=cmd2("mecab-config --inc-dir"),
        library_dirs=cmd2("mecab-config --libs-only-L"),
        libraries=cmd2("mecab-config --libs-only-l"))
    ],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Environment :: MacOS X",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
