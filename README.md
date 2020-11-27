### Setup

* Create an environment with the latest version of python 3: ```conda create -n uniXerr python=3```
* Create the environment using the _uniXerr.yml_ file: ```conda env create -f fuzzer.yml```
* Activate _fuzzer_ environment: ```conda activate fuzzer```
* Update the environment using _fuzzer.yml_ file: ```conda env update -f fuzzer.yml --prune```
* Export your active environment to _fuzzer.yml_ file: ```conda env export | grep -v "^prefix: " > fuzzer.yml```
