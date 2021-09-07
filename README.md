AirBnbModel - predicting the destination country of the first reservation 
for new users of AirBnb
=====================================================================

**AirBnbModel** is a Python package containing a production-ready, classification 
model for predicting the destination country of the first reservation for new 
users of AirBnb.

This model uses users' data as an input (age, gender, language...), as well as 
information related to the actions taken by the users on the website of AirBnb, 
and returns a prediction encoded in form of an integer between 0 and 12.
=====================================================================

Usage
----------------

- Package and its dependencies, can be installed by running "setup.py".
- Once installed, all functionallity of the model can be accessed through cmd, 
  executing 
  $python -m AirBnbModel --task {taskname} --mode
- Further help on the features and usage of the package can be found by running 
  $pydoc AirBnbModel
- Further help on the features and usage of the submodules can be found by running 
  $pydoc AirBnbModel/preprocess
