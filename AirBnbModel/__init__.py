"""
AirBnbModel - predicting the destination country of the first reservation
for new users of AirBnb
=====================================================================

**AirBnbModel** is a Python package containing a production-ready,
classification model for predicting the destination country of the first
reservation for new users of AirBnb.

This model uses users' data as an input (age, gender, language...), as well as
information related to the actions taken by the users on the website of AirBnb,
and returns a prediction encoded in form of an integer between 0 and 12.


Main Features
-------------
The functionality of the package is contained in several submodules:

  - Source: Extracts the data from the different source data stores, and loads
    it into a staging database

  - Preprocess: Reads data from staging database, asserts key properties and
    transforms the data in order to be fed into a ML model.

  - Model: Contains a ML model that can use preprocessed data to generate
    predictions (classifications), once it has been trained.

All components can be executed both on "train_eval" and "predict" mode.


Usage
-------------
All the functionality of the package is accessed throgh __main.__py file.
The package can be executed using the command line, typing the name of the
package followed by the following arguments:

  - task: source, preprocess, model
  - mode: train_eval, predict

The tasks executed on "train_eval" mode, will use the training data to train
the and configure the different parameters of the preprocessing steps and the
model itself. When executed on "predict" mode, the tasks will use learned
parameters, extracted from the training steps, to preprocess the data and
generate a new prediction.

Configuration regarding data location, preprocessing parameters and model
parameters, can be accessed through different .yaml files located in "configs"
folder.


Examples
-------------
Extract training data from source data stores and save it into a staging
database:

>>> python AirBnbModel --task source --mode train_eval

Read training data from a staging database and use it to extract preprocessing
parameters and, after that, preprocess it:

>>> python AirBnbModel --task preprocess --mode train_eval

Read preprocessed training data and use it to train a classification model:

>>> python AirBnbModel --task model --mode train_eval
"""


__all__ = ["source", "preprocess", "model"]
