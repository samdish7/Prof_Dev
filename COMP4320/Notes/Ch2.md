# Ch.2 Packaging and Distributed Python Code; 20220822

## Objectives
- Use __pyenv__ to manage different versions of Python
- Use virtual environments to manage dependencies
- Use __import__ effectively
- Create a custom package
- Prepare a package for distribution

## Multiple Python Versions with __pyenv__

You can use multiple versions of python using a _git clone_ command. There is an example shell script under _install_pyenv.sh_ Type __pyenv install --list__ to see what instances are available to download.

You update the ./pyenv folder like normal git repos. Just do a _git pull_

We can run these different versions through a _virtual environment_. This cane be useful because maybe your normal env shouldn't be regressed because that may break something. 

## Importing Modules

Even though you CAN import all packages of a certain module, it is bad practice because it wastes space/memory. 

## Code Portability 

Before thinking about distributing packages, think about the code portability. Can this package be used on multiple OS?


