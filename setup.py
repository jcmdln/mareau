from setuptools import (find_packages, setup)

with open('License.md') as f:
    License = f.read()

with open('Readme.md') as f:
    Readme = f.read()

setup(
    name = 'mareau',
    version = '0.0.0a0',
    description = 'API driven market research automation',
    long_description = Readme,
    url = 'https://github.com/jcmdln/mareau',
    author = 'Johnathan Maudlin',
    author_email = 'jcmdln@gmail.com',
    license = License,
    keywords = ['analysis', 'automation', 'market', 'research'],

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
        'httplib2',
        'oauth2client',
        'praw'
    ],

    packages = find_packages(
        exclude = ['contrib', 'docs', 'tests']
    ),

    entry_points = {
        'console_scripts': [
            'mareau = mareau.cli:mareau'
        ]
    }
)
