# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in multilanguage_frappe_website/__init__.py
from multilanguage_frappe_website import __version__ as version

setup(
	name='multilanguage_frappe_website',
	version=version,
	description='Multilanguage Frappe Framework website example',
	author='DFP developmentforpeople',
	author_email='developmentforpeople@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
