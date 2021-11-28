from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sploy/__init__.py
from sploy import __version__ as version

setup(
	name="sploy",
	version=version,
	description="making it quote",
	author="gross innovate and contributors",
	author_email="spryngmanaged@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
