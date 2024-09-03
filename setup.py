#!/usr/bin/env python3
import os

from setuptools import setup

from epub_extractor import __author__, __license__, __version__


def get_long_description():
    return open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


setup(
    name='epub-extractor',
    version=__version__,
    description=(
        'Extract comic EPUB pages to Jpeg files, Dump meta information.'
    ),
    long_description=get_long_description(),
    license=__license__,
    author=__author__,
    author_email='ytyng@live.jp',
    url='https://github.com/ytyng/epub-extractor.git',
    keywords='comic epub extract jpeg images and meta information.',
    packages=['epub_extractor'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'epub-extract-jpeg = epub_extractor.epub_extract_jpeg:main',
            'epub-dump-meta = epub_extractor.epub_dump_meta:main',
        ]
    },
)
