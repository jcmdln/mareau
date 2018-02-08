from setuptools import (find_packages, setup)

with open('License.md') as f:
    License = f.read()

with open('Readme.md') as f:
    Readme = f.read()

setup(
    name = 'markan',
    version = '0.0.0a0',
    description = 'API-driven market analysis',
    long_description = Readme,
    url = 'https://github.com/jcmdln/markan',
    author = 'Johnathan Maudlin',
    author_email = 'jcmdln@gmail.com',
    license = License,
    keywords = ['market', 'analysis', 'utility'],

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],

    install_requires = [
        'click',
        'configparser',
        'future',
        'google-api-python-client',
        'oauth2client',
        'praw',
        'requests'
    ],

    packages = find_packages(
        exclude = ['contrib', 'docs', 'tests']
    ),

    entry_points = {
        'console_scripts': [
            'markan = markan.cli:markan'
        ]
    }
)
