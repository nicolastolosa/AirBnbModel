Getting started
#####################

Installation
****************************************************
Clone the remote repository using ``git glone``

>>> git clone https://github.com/nicolastolosa/AirBnbModel.git

Once cloned, the dependencies for the package containing the model can be installed using pip on the command line

>>> pip install AirBnbModel

.. note::
   Make sure you are in the same folder as setup.py before running pip install.



Project folder structure
****************************************************
 ::

   | AirBnbModel                                
   | ├── docs/                              Documentation (.rst, .html)
   | ├── configs/                           Config files (.yml)
   | ├── logs/                              Execution logfiles (.log)
   | ├── notebooks/                         EDA, model building and validation (.ipynb)
   | ├── AirBnbModel                        Top level package dir
   | │   ├── source/                        Data sourcing subpackage
   | │   ├── preprocess/                    Data preprocessing subpackage
   | │   ├── model/                         Training and evaluating model and generating predictions
   | │   ├── utils/                         Util functions used in source/preprocess/model packages
   | │   ├── tests/                         Unit test suite for the package
   | │   ├── __init__.py                        
   | │   ├── __main__.py                    Package execution entry point: ``python -m AirBnbModel``
   | │   ├── config.py                      Loads configuration files from /config
   | │   └── run.py                         Orchestrates the execution. Called from __main__.py
   | ├── README.md                          Intro to package
   | ├── setup.py                           Installing the package
   | ├── requirements.txt                   Lists dependencies
   | └── LICENSE.md                         License


About the model
****************************************************
Further information about the model and results can be found `here <AboutTheModel.html>`_

Running the model
****************************************************
The entry point to all the functionallity of the package is the package itself. Thus, the model can be run using the command line by typing 

>>> python -m AirBnbModel --task [source|preprocess|model] --mode [train_eval|predict]

The functionallity of the package is divided into three subpackages (``source``, ``preprocess`` and ``model``). Each of them contains the logic to run different parts of the data pipeline needed to successfully 
run the model. The user can select which one of the modules to execute usin the ``task`` parameter.

On the other side, the pipeline can be run both on ``train_eval`` or ``predict`` mode (which can be controlled using ``mode`` parameter). This parameter controls whether the pipeline is executed using training data, in order to retrain the model, or whether it must be fed with new data in order to generate predictions.   


.. image:: ../../_static/pipeline.png
  :width: 800
  :alt: pipeline


===================
.. note::
   The parameters of the different tasks can be changed using the .yml files located in */config* folder.

