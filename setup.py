#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pygelf',
    version='0.2',
    description='Python library for sending events to Graylog2 over the Gelf HTTP Input',
    author='Alex Nikonov',
    author_email='alex@sshaman.ru',
    license='GPL V2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pycurl']
)
