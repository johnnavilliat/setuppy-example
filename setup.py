{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from setuptools import setup\
import re\
\
try:\
    verstrline = open('webui/_version.py', "rt").read()\
except IOError:\
    raise RuntimeError("cannot read version file")\
else:\
    VSRE = r"^__version__ = ['\\"]([^'\\"]*)['\\"]"\
    mo = re.search(VSRE, verstrline, re.M)\
    if mo:\
        verstr = mo.group(1)\
    else:\
        raise RuntimeError("unable to find version in yourpackage/_version.py")\
\
setup(\
    # Application name:\
    name="webapp",\
\
    # Version number (initial):\
    version=verstr,\
\
    # Application author details:\
    author="Matthew Yates",\
    author_email="matthew.yates@snyk.io",\
\
    # Packages\
    packages=["webui"],\
\
    # Include additional files into the package\
    include_package_data=True,\
\
    # Details\
    url="https://github.com/mtyates/puppet_webapp",\
\
    description="Example App",\
    test_suite='tests',\
\
    # Dependent packages (distributions)\
    install_requires=[\
        'Flask==0.10.1',\
        'Flask-Testing==0.4.2',\
        'itsdangerous==0.24',\
        'Jinja2==2.8',\
        'MarkupSafe==0.23',\
        'Werkzeug==0.11.9',\
    ],\
\
)\
}