from setuptools import (find_packages, setup)

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name = 'mareau',
    version = '0.0.0a0',
    description = 'API driven market research automation',
    long_description = readme,
    url = 'https://github.com/jcmdln/mareau',
    author = 'Johnathan Maudlin',
    author_email = 'jcmdln@gmail.com',
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
        'google-api-python-client',
        'httplib2',
        'oauth2client'
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
