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
1.This script would need a httplib2 python pacakage to establish a http connection.

2.Install this package using the command - pip install httplib2

3.Note: Make python package installer(pip) is available in the machine.It would be available while installing the preferred version of python for your machine.

# Python Libraries and Executables Needed
1.celery

2.flask

3.feedparser

4.pymongo

5.RabbitMQ - Task Queue Manager (https://www.rabbitmq.com/)

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

