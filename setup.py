#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

tests_require = [
    'coverage~=4.5.4',
    'flake8~=3.7.9',
    'pytest~=5.3.2',
    'pytest-cov~=2.8.1',
    'mypy==0.750',
]

docs_require = [
    'Sphinx~=2.3.0',
    'sphinx-autodoc-typehints~=1.10.3',
]

dev_requires = tests_require + docs_require + [
    'pip==19.2.3',
    'bump2version~=0.5.11',
    'wheel==0.33.6',
    'tox==3.14.0',
    'twine==1.14.0',
]

setup(
    author="Carsten Rösnick-Neugebauer",
    author_email='croesnick@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Typing :: Typed',
    ],
    description="Sample library for Keithley DAQ6510 instrument utilizing pyvisa and pyvisa-sim",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='keithley_daq6510',
    name='keithley_daq6510',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    extras_require={
        'dev': dev_requires,
        'docs': docs_require,
        'tests': tests_require,
    },
    url='https://github.com/croesnick/keithley_daq6510',
    version='0.0.1',
    zip_safe=False,
)
