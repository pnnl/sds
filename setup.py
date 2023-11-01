import os
from setuptools import setup, find_packages
import sys

sys.path.append(os.path.dirname(__file__))

import sds

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

pkgs = find_packages(exclude=('examples'))

setup(
    name='sds',
    version=sds.__version__,  # TODO: switch to versioneer.get_version() or alternate method
    description='SDS: Similarity Down Selection',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Felicity Nielson',
    author_email='jessica.bade@pnnl.gov',
    license=license,
    packages=pkgs,
    python_requires=">=3.9",
    install_requires=install_requires,
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)