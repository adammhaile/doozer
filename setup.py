# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup, find_packages

with open('./requirements.txt') as f:
    INSTALL_REQUIRES = f.read().splitlines()


def _get_version():
    from os.path import abspath, dirname, join
    filename = join(dirname(abspath(__file__)), 'doozerlib', 'VERSION')
    return open(filename).read().strip()


setup(
    name="rh-doozer",
    author="AOS ART Team",
    author_email="aos-team-art@redhat.com",
    version=_get_version(),
    description="CLI tool for managing and automating Red Hat software releases",
    long_description=open('README.md').read(),
    url="https://github.com/openshift/doozer",
    license="Apache License, Version 2.0",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'doozer = doozerlib.cli.__main__:main'
        ]
    },
    install_requires=INSTALL_REQUIRES,
    test_suite='tests',
    dependency_links=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "Environment :: Console",
        "Operating System :: POSIX",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Natural Language :: English",
    ]
)
