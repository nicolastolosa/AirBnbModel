About the data
#####################

The training data available for this problem, consists on two different datasets:

 - **users.csv:** Contains information about american users registered in AirBnb. This dataset contains the *target* variable, which indicates the country of destination of their first reservation in AirBnb.
 - **sessions.csv:** Contains a list of the actions performed by each user (from users.csv) on the website of AirBnb. Each row contains a user ID that can be matched with the ones in *users.csv*


*users.csv* dataset structure
*******************************
This dataset contains **213.451 unique rows and 16 columns**. Each row represents a user registered in AirBnb in the United States between 01/01/2010 and 30/06/2014.
The following table contains a detail of the columns of the dataset:


.. list-table:: users.csv dataset
   :widths: 25 25 50
   :header-rows: 1

   * - Column name
     - DataType
     - Description
   * - Id
     - Identifyer (str)
     - Unique ID for the users of the dataset
   * - Date_account_created
     - Date
     - Date of creation of the account of AirBnb
   * - Timestamp_first_active
     - Date
     - | Date on which the first activity on the 
       | website was registered. This date can be 
       | prior to *Date_account_created*
   * - Date_first_booking
     - Date 
     - Date of the first reservation (if any)
   * - Gender
     - Categorical (str - 4 values)
     - Gender of the user
   * - Age
     - Numeric (int)
     - Age of the users, at the time they signed up
   * - Signup_method
     - Categorical (str- 3 values)
     - Method used to sign up
   * - Signup_flow
     - Categorical (str- 7 values)
     - Unknown
   * - Language
     - Categorical (str - 24 values)
     - Language in which the account is configured
   * - Affiliate_channel
     - Categorical (str - 8 values)
     - | Marketing affiliate channel registered during
       | the session in which the user signed up
   * - Affiliate_provider
     - Categorical (str - 17 values)
     - | Affiliate provider registered during
       | the session in which the user signed up
   * - First_affiliate_tracked
     - Categorical (str - 7 values)
     - Unknown
   * - Signup_app 
     - Categorical (str - 4 values)
     - | Application type used by the user at the 
       | time of signing up
   * - First_device_tracked
     - Categorical (str - 9 values)
     - 
   * - First_browser
     - Categorical (str - 35 values)
     - 
   * - Country_destination
     - Categorical (str - 12 values)
     - | **Target column**
       | NDF refers to: No reservation



*sessions.csv* dataset structure
*******************************
This dataset contains **10.533.241 rows and 6 columns**. Each row represents and action taken by a user on the webpage of AirBnb.
In this dataset, are reflected the actions of **135.483 unique users**.
Each user has a number between 0 and N actions associated, and the data is ordered so the most recent actions are located in the top of the file. 

For each row, there is an attribute representing que unique ID of the user that performed the action, so it can be linked with te users dataset.
The columns available un sessions.csv dataset, are detailed in the following table:


.. list-table:: users.csv dataset
   :widths: 25 25 50
   :header-rows: 1

   * - Column name
     - DataType
     - Description
   * - User_id
     - Identifyer (str)
     - Unique ID of the user
   * - Action
     - Categorical (str - 321 values)
     - Detail of the action
   * - Action_type
     - Categorical (str - 9 values)
     - Detail of the action
   * - Action_detail
     - Categorical (str - 128 values)
     - Detail of the action
   * - Device_type
     - Categorical (str - 14 values)
     - Device OS
   * - Secs_elapsed
     - Numeric (int)
     - | Seconds elapsed since the action
       | finishes until a new action is
       | recorded for the same user

combining *users.csv* and *sessions.csv*
*******************************
.. image:: ../../_static/users_sessions_venn.png
  :width: 800
  :alt: pipeline
