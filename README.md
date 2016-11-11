# ReviewFetcher
  It’s a centralized repository that retrieves the review comments posted by number of users of an application hosted in Appstore or Playstore. The backend API’s developed will process and display  the updated comments in well-developed UI. It will provide an insight to the developers on the problematic areas majorly faced by the customers effectively and periodically.

# Implementation
1.Currently we have developed only for Apple’s Appstore through iTunes RSS Feed API.

2.Playstore – Google API to get review comments are available but there is a restriction to access it. Only developers who developed the specific application will be able to get the review comments of the app.

# Key points
1.This web application is developed fully by using Python and Python Flask Micro Web Framework.

2.This application is using MongoDB as a database to store the review comments.

3.This application is using Periodic Task Scheduler to retrieve the review comments of the app periodically(for eg. Say for every 3 hours).

# Invoking a Web Application
# Pre-Requisite
1.Install the python to your computer(preference python-2.7.XX series version)

2.Set the environment variables to execute the python scripts from the command prompt.Below mentioned folders need to be added in environment variables under the path,

Add these - C:\Python27\Scripts , C:\Python27\Tools\Scripts

# Required Package Installation
1.This script would need a required python pacakage.

2.Install this package using the command - pip install <package name>

3.Note: Make python package installer(pip) is available in the machine.It would be available while installing the preferred version of python for your machine.

# Python Libraries and Executables Needed
1.celery

2.flask

3.feedparser

4.pymongo

5.RabbitMQ - Message Broker and Task Queue Manager (https://www.rabbitmq.com/)

# Steps to execute - Using Command Prompt
1.Download and save the scripts to the local directory/folder.

2.Navigate to the directory using the command prompt(cmd -- > cd  <<particular directory).

3.Then use the command - python app_run.py and it will ask the instructions to execute the script.​

4.Results would be displayed in the web page .

Note : Information parsed are based upon the response from Apple’s iTunes RSS Feed API.

# Steps to execute - Using Pycharm IDE
1.Download the PyCharm IDE.

2.Unzip the attached script and load it in IDE and execute the script.

# Tools and Technologies used

iTunes RSS Feed API – to retrieve the review comments for the AppStore hosted applications.

1.Python 2.7

2.Python Flask – Web Micro framework

3.MongoDB

4.PyMongo – Python library to connect and retrieve data from Mongo DB

5.Celery – Python Task Scheduler Library

6.RabbitMQ – Scheduler Task Queue Handler

7.HTML, JQuery and BootStrap3

# Message Broker - RabbitMQ Commands:

To Start server - rabbitmq-server

To stop server - rabbitmqctl stop

To list queues - rabbitmqctl list_queues

To start the app - rabbitmqctl start_app

To stop the app - rabbitmqctl stop_app

To reset - rabbitmqctl reset

# Celery Commands

Windows celery beat mode format - celery beat -A celery_tasks_schedule_directory name.list of tasks to perform --loglevel=info

Windows celery beat mode usage   - celery beat -A celery_tasks_schedule.tasks --loglevel=info

MAC /Linux beat command - celery -A name_of_the_application worker -l info --beat

MAC /Linux beat command usage - celery -A asset_store worker -l info --beat

Viewing the celery workers logs - celery -A celery_tasks_schedule worker --loglevel=info

# Starting the Celery Scheduler (steps for windows only and for mac refer the commands mentioned)

1.Start the RabbitMQ Message broker in the backend in separate terminal/command prompt - rabbitmq-server

2.In another terminal/command prompt and invoke the command to start the celerey in beat mode - celery beat -A celery_tasks_schedule.tasks --loglevel=info

3.In another terminal/command prompt and invoke the command to view the celery logs 

celery -A celery_tasks_schedule worker --loglevel=info

# MongoDB Setup

1.Please download the mongodb from the mongodb official website and set the environment as mentioned.

2.Once the environment and data folder is set as per setup instructions,then run the command - mongod and verify whether MongoDB is up.

3.Use the below mentioned links for exporting  and importing the mongodb records while setting up the environment,
  http://lornajane.net/posts/2011/importing-and-exporting-mongodb-databases (Preferred one) 
  
  https://www.mkyong.com/mongodb/mongodb-import-and-export-example/
  
  # Sample commands to export the mongodb data available in local machine - mongodump -d mongo_db_name -o folder_you_want_to_use
  
   Example : mongodump -d app_store_holder -o app_review_repo_info
  
  # Sample commands to import the mongodb data available in local machine - mongorestore -d mongo_db_name /path/to/db_records_exported
  
   Example : mongorestore -d app_store_holder /path/to/app_store_holder
   
   
  
   
  
  
 

  






