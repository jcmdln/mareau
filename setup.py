from setuptools import (find_packages, setup)

def Open(File):
    with open(File) as f:
        return f.read()

setup(
    name             = 'markan',
    version          = '0.0.1',
    description      = 'API-driven market analysis',
    long_description = Open('Readme.md'),
    license          = Open('License.md'),
    url              = 'https://github.com/jcmdln/markan',
    author           = 'Johnathan Maudlin',
    author_email     = 'jcmdln@gmail.com',

    keywords = [
        'market', 'analysis'
    ],

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
