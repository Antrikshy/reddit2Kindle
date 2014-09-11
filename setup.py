#!/usr/bin/env python
# encoding: utf-8
from setuptools import setup, find_packages

setup(
    name='reddit2kindle',
    entry_points={
        'console_scripts': [
            'r2k = r2klib.cli:from_cli'
        ]
    },
    packages=find_packages(),
    install_requires=[
        'markdown2',
        'praw',
        'docopt',
        'jinja2'
    ],
    version='0.6.0',
    author='Antriksh Yadav',
    author_email='antrikshy@gmail.com',
    url='http://www.antrikshy.com/projects/reddit2kindle.htm',
    description=(
        'Compiles top posts from a specified subreddit for a specified time'
        'period into a well-formatted Kindle book.'
    ),
    long_description=(
        'See http://www.github.com/Antrikshy/reddit2kindle for instructions. '
        'Requires ebook-convert from Calibre or KindleGen from Amazon '
        'to convert HTML result to .mobi forKindle.'
    ),
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License'
    ],
    zip_safe=False,
    include_package_data=True
)
