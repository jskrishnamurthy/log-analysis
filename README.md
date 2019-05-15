# Logs Analysis Project - Udacity Full Stack Web Developer Nanodegree

# DESCRIPTION:
Build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like. The program can be run from the command line. It won't take any input from the user. Instead, it will connect to the postgreSQL database running on virtual machine and print out the answers to the below 3 questions.

What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?

# RUNNING THE PROGRAM:
To get started, Install the virtual machine and Install vagrant. Detailed instructions can be found [here](https://github.com/udacity/fullstack-nanodegree-vm). Use vagrant up to bring the virtual machine online and vagrant ssh to login.

Download the data provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file in order to extract newsdata.sql. This file should be inside the Vagrant folder.

Load the database using psql -d news -f newsdata.sql.

Connect to the database using psql -d news.

Create the Views given below. Then exit psql.

Now execute the Python file - python logs_analysis.py.

# CREATE THE FOLLOWING VIEWS FOR QUESTION 3:

```sh
CREATE VIEW ErrorLogs AS SELECT to_char(time::date, 'Mon dd yyyy') as logTimestamp, count(*) as logCount FROM log 
WHERE status='404 NOT FOUND' 
group by to_char(time::date,'Mon dd yyyy');
```
```sh
CREATE VIEW SuccessLogs AS SELECT to_char(time::date, 'Mon dd yyyy') as logTimestamp, count(*) as logCount FROM log 
WHERE status='200 OK' 
group by to_char(time::date,'Mon dd yyyy');
```
