#!/usr/bin/env python

import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# To update the package version number, edit pyCHAMP/__version__.py
version = {}
with open(os.path.join(here, 'pyCHAMP', '__version__.py')) as f:
    exec(f.read(), version)

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='pychamp',
    version=version['__version__'],
    description="CHAMP QMC code in Python",
    long_description=readme + '\n\n',
    author="Nicolas Renaud",
    author_email='n.renaud@esciencecenter.nl',
    url='https://github.com/NLESC-JCER/pyCHAMP',
    packages=[
        'pyCHAMP',
    ],
    package_dir={'pyCHAMP':
                 'pyCHAMP'},
    include_package_data=True,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='pyCHAMP',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    install_requires=['autograd', 'cython', 'numpy', 'pyhmc', 'schema', 'scipy'],
    setup_requires=[
        # dependency for `python setup.py test`
        'pytest-runner',
        # dependencies for `python setup.py build_sphinx`
        'sphinx',
        'sphinx_rtd_theme',
        'recommonmark'
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pycodestyle',
    ],
    extras_require={
        'dev':  ['prospector[with_pyroma]', 'yapf', 'isort'],
    }
)
