from setuptools import setup, find_packages

with open("README.md", "r") as fh: 
	description = fh.read() 

setup( 
	name="py-loc", 
	version="0.0.1", 
	author="Praise G", 
	author_email="praisegodwins4@gmail.com", 
	packages=find_packages(), 
	description="A simple way of counting lines of code in your project", 
	long_description=description, 
	long_description_content_type="text/markdown", 
	url="https://github.com/godwins3/py-loc", 
	license='MIT', 
	python_requires='>=3.8', 
	install_requires=[] 
) 
