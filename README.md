
# Sparkify Suggested Database & ETL Pipeline

## About 

Sparkify is a fictional music application that store songs and users' activity logs in separate **JSON** files. When the application started to grow, it becomes extremely difficult for the company to handle and benefit from these files. The suggested solution is to start investing in databases and ETL pipelines (*The process of extracting data from various sources, Transforming and processing it then store it in the destination database*)


## Database design

Since the company deal with huge amount of data, **Star schema** database design is the perfect fit for this application cause it facilitates insert and update processes. The database consist of the following tables:

 - **Song play** (The fact table)
 - **Songs** (Dimensional table extracted from song_data files)
 - **Artists** (Dimensional table extracted from song_data files)
 - **Users** (Dimensional table extracted from log_data files)
 - **Time** (Dimensional table extracted from Timestamp column)


## ETL Pipeline:

The logic of ETL Pipeline is as follow:

 - Navigate and pull all **JSON** Files from the source 
 - Separate song data into two tables (Songs & Artists)
 - Separate log data into two table (Users & Time)
 - Finally insert the records to the new PostgreSQL database

##  Final Result:
Here are screenshots of all the tables, after feeding them with etl pipeline records 

**song table:**
![Song](https://i.imgur.com/AdQ1iKu.png)

**artist table:**
![Artist](https://imgur.com/EhOhpdT.png)

**user table**

![User](https://imgur.com/l18lo4X.png)

**time table**

![Time](https://imgur.com/DtRMwZm.png)

**songplay**

![SongPlay](https://imgur.com/pIpYbJQ.png)


## User Manual:

To Run the Pipeline do the following instructions in the same order

 1. Open the terminal or bash in windows
 2. Write *python create_tables.py* then click enter to execute the command
 3. Write *python etl.py* then wait until the processing is completed 
 4. Run test.ipynb to make sure all the records were added successfully




Regards,
Noof Aleliwi