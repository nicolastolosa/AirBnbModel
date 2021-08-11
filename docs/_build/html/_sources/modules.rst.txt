AirBnbModel package
===================

Subpackages
-----------

.. toctree::
   :maxdepth: 1

   AirBnbModel.source
   AirBnbModel.preprocess
   AirBnbModel.model
   AirBnbModel.utils
   AirBnbModel.tests

Submodules
----------

AirBnbModel.run module
----------------------

.. automodule:: AirBnbModel.run
   :members:
   :undoc-members:
   :show-inheritance:


AirBnbModel.config module
----------------------

.. automodule:: AirBnbModel.config
   :members:
   :undoc-members:
   :show-inheritance:


For the training of the model, a dataset containing the information about users two different datasets have been provided:

#. **users.csv:** Containing information about users registered in the platform (age, sex, language) 
#. **sessions.csv:** Containing information about actions taken in the website by the users on *'users.csv'* (page view, checkout...)
#. **target.csv:** The country destination of the first reservation made by the users on *'users.csv'*. 13 different outputs.

**The objective of the model is to predict the country of destination of the first reservation, for a new user, given the information contained in *'users.csv'* and *'sessions.csv'*.**
