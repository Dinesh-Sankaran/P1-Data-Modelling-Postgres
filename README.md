Summary:
========
This project build database and ETL flow for startup company called Sparkify to analyse their music streaming app

Source Files:
=============
This project use source as two json file 
 - Song Dataset
        Song Dataset contains a metadata about a song and artist of that songs
        
 - Log Dataset
        Log Dataset contains log details such as artist name,song title, auth mode,level,timestamps etc..

Target Tables:
==============
We have identified 4 dimension and one fact tables to store data as like below
#### Dimension
**1. users**
Basically stores details of the user such as userid, firstname, lastname, etc..

**2. songs**
Basically stores details of the songs such as songid, title, artistid, duration of the song 
        
**3. artists**
        artists table contain details of the artist. it can connect with songs table using artistid
        
**4. time**
        time dimension is particularly developed for data analysis. Mostly users want to see their data by datetime group function
#### Fact       
**songplays**
- songplays is a fact table which capture data from log dataset and used to store songid,artistid from dimension tables
- It captures only valid record with page value equal to NextSong

Python Scripts:
===============
**1. create_tables.py**
- This script contain three user defined function.. one for creating database ,create tables and drop tables.
- It imports create table queries and drop table queries from sql_queries.py
- The main function calls create database function and establish the postgres connection followed by it drops the table if exists and create tables if not exists

**2. sql_queries.py**
- This script contain sql queries for drop, create, insert and select statement
- It pass create and drop table query as list to create_tables.py
- etl.py file import the query(insert, select) through variable
    
**3. etl.py**
This is the main script file which build etl flow for sparkify database
- The method **process_song_file** reads the json file **song dataset**
    - select the required columns for song table in to dataframe 
    - execute the insert statement by passing dataframe value as variable
    - Similarly select the required columns for artist table in to dataframe
    - execute the insert statement by passing dataframe value as variable
- The method **process_log_file** reads the json file **log dataset** 
    - It select only valid records into dataframe ***i.e page=NextSong***
    - Using time attribute, it generate the columns for time table such as *hour*, *day*, *week*, *month*, *etc*..
    - Execute the insert statement by passing dataframe value as variable
    - Similarly select user information from log dataset and execute insert statement
    - select the columns for songplay table from log dataset and select songid and artistid from dimension tables using select query for matching songname, duration and artistname.

- The method **process_data** scan through the complete path and identify the files to process
            
   
                
Execution Procedure:
====================
###### Note: 
Close all the open connection to sparkify database before running below scripts
1. Run the create_tables.py in command prompt
    ```sh
    python create_tables.py
    ```
    **Expected output:**
drop_tables completed...
create_tables completed...

2. Run the etl.py 
    ```sh
    python create_tables.py
    ```
    **Expected output:**
it shows the number of files processed in song dataset and log dataset
            
Validation Script:
==================
Use the **test.ipynb** file and execute the first 7cells to ensure records has been inserted into both fact and dimension tables
    
 
    