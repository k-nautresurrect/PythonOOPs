## To initiate my own virtual environment
- check wether you are using conda or not
	- if yes then to affect the actual python use
		-```conda deactivate``` inside the directory where you want to work
		- then check the pip verison by ```pip --version``` it should be like this 
		```pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)```
		- then install virtualenv module by ```pip install virtualenv```
	- initate the virtual environment by executing 
		- ```python3 -m virtualenv dirName``` here -m flag is used to specify the module
	- this will initiate all files for virtual environment in the directory.
- to activate the new environment
	- use ```source dirname/bin/activate``` here activate is just a bash file which will set certain path variables for the current environment
	- to deactivate this environment simply type ```deactivate```
	- to remove this virtual environment and all the other path variable use ```rm -rf dirname```
