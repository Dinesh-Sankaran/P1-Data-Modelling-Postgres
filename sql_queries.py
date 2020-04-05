# DROP TABLES
# SQL Statement to drop tables if already exists
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"


# CREATE TABLES

# SQL Statement to create fact table called songplays 
songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL PRIMARY KEY, 
        start_time BIGINT NOT NULL, 
        user_id INT NOT NULL, 
        level VARCHAR, 
        song_id VARCHAR, 
        artist_id VARCHAR, 
        session_id VARCHAR, 
        location VARCHAR, 
        user_agent VARCHAR
    )
""")

# SQL Statement to create dim table called users with primary key column user_id
user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY, 
        first_name VARCHAR NOT NULL, 
        last_name VARCHAR, 
        gender CHAR(1), 
        level VARCHAR
    )
""")

# SQL Statement to create dim table called song with primary key column song_id and foreign key reference to artists table
song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR PRIMARY KEY, 
        title VARCHAR NOT NULL, 
        artist_id VARCHAR REFERENCES artists(artist_id), 
        year INT, 
        duration FLOAT
    )
""")

# SQL Statement to create dim table called artists with primary key column artist_id
artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR PRIMARY KEY, 
        name VARCHAR NOT NULL, 
        location VARCHAR,
        latitude VARCHAR, 
        longitude VARCHAR
    )
""")

# SQL Statement to create dim table called time
time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time BIGINT PRIMARY KEY, 
        hour INT, 
        day INT, 
        week INT,
        month INT, 
        year INT,
        weekday INT
    )
""")


# INSERT RECORDS

# SQL Statement to insert the records into songplays table
songplay_table_insert = (""" 
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
""")

# SQL Statement to insert the records into users table and update with latest records when user_id conflict occurs
user_table_insert = (""" 
    INSERT INTO users (user_id, first_name, last_name, gender, level) 
    VALUES (%s,%s,%s,%s,%s) 
    ON CONFLICT(user_id) 
    DO UPDATE SET  
    first_name=users.first_name, last_name=users.last_name, gender=users.gender, level=users.level
""")

# SQL Statement to insert the records into songs table, do nothing when conflict occurs
song_table_insert = (""" 
    INSERT INTO songs (song_id,title,artist_id,year,duration) 
    VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING
""")

# SQL Statement to insert the records into artists table, do nothing when conflict occurs
artist_table_insert = (""" 
    INSERT INTO artists (artist_id, name, location, latitude, longitude) 
    VALUES (%s,%s,%s,%s,%s) 
    ON CONFLICT DO NOTHING
""")

# SQL Statement to insert the records into time table, do nothing when conflict occurs
time_table_insert = (""" 
    INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
    VALUES (%s,%s,%s,%s,%s,%s,%s) 
    ON CONFLICT DO NOTHING 
""")


# FIND SONGS
# Get the song ID and artist ID by querying the songs and artists tables to find matches based on song title, artist name, and song duration time.

song_select = (""" 
    SELECT 
        songs.song_id, 
        artists.artist_id 
    FROM songs 
    JOIN artists 
        ON songs.artist_id=artists.artist_id
    WHERE 
        songs.title = %s 
        and artists.name = %s 
        and songs.duration = %s
""")

# QUERY LISTS
#Changed the order of execution in create table queries, artist table first then song table since song table has reference with artist table

create_table_queries = [songplay_table_create, user_table_create, artist_table_create, song_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]