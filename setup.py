"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from os import path
from setuptools import setup, find_packages


# Get the long description from the README file
_SETUP_PATH = path.abspath(path.dirname(__file__))
with open(path.join(_SETUP_PATH, 'README.md'), encoding='utf-8') as f:
    _LONG_DESCRIPTION = f.read()


setup(
    name='bemserver',
    version='0.0.1',
    description='Hit2gap platform Core',
    long_description=_LONG_DESCRIPTION,
    # url='https://github.com/pypa/sampleproject',
    # Author details
    author='Nobatek/INEF4',
    #author_email='pypa-dev@googlegroups.com',
    #license='',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        # Indicate who your project is intended for
        #'Intended Audience :: Developers',
        #'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish (should match "license" above)
        #'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    # What does your project relate to?
    #keywords='sample setuptools development',
    packages=find_packages(exclude=['tests*']),

    package_data={
        '': ['database/timeseries/*.csv'],
    },
    install_requires=[
        'flask>=1.0',
        'flask_marshmallow>=0.7.0',
        'flask-rest-api>=0.10.0,<0.11.0',
        'webargs>=5.1.3,<6.0',
        'apispec>=0.39.0,<1.0.0',
        'python-dateutil>=2.5.0',
        'marshmallow>=2.15.2,<3.0.0',
        'marshmallow-oneofschema>=1.0.5',
        'requests>=2.11.1',
        'numpy>=1.14.0',
        'pandas>=0.22',
        'sparqlwrapper',
        'flask-jwt-simple>=0.0.3,<0.1.0',
        'python3-saml>=1.4.1,<1.5',
        'tables>=3.3.0',
        'pint>0.7,<0.9',
        'sqlalchemy>=1.2.5',
        'sqlalchemy-utils>=0.32.21',
        'flask-sqlalchemy>=2.3.2',
        'flask-migrate>=2.1.1',
        'python-dotenv>=0.8.2'
    ],
)
