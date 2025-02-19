# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES


# Songplays is the fact table which hold deminsions tables primary keys

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays 
(
        songplay_id serial NOT NULL, 
        start_time bigint REFERENCES time(start_time), 
        user_id varchar REFERENCES users(user_id), 
        level varchar, 
        song_id varchar REFERENCES songs(song_id) , 
        artist_id varchar REFERENCES artists(artist_id), 
        session_id bigint, 
        location varchar, 
        user_agent text, 
        primary key (songplay_id)
        
)
""")

# creating deminsion tables 

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users
(
        user_id varchar NOT NULL,
        first_name varchar,
        last_name varchar,
        gender varchar,
        level varchar,
        primary key (user_id)
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
(
        song_id varchar NOT NULL,
        title varchar,
        artist_id varchar,
        year int,
        duration double precision,
        primary key (song_id)

)

""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists
(
        artist_id varchar NOT NULL,
        name varchar,
        location varchar,
        latitude double precision, 
        longitude double precision,
        primary key (artist_id)
)
        
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
(
        start_time bigint NOT NULL,
        hour int,
        day int,
        week int,
        month int, 
        year int,
        weekday int,
        primary key (start_time)
        
)
""")

# INSERT RECORDS

songplay_table_insert = ("""

INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (songplay_id) DO NOTHING


""")

user_table_insert = ("""

INSERT INTO users (user_id, first_name, last_name, gender, level) 
VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level

""")

song_table_insert = ("""

INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (song_id) DO NOTHING


""")

artist_table_insert = ("""

INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING;


""")


time_table_insert = ("""

INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING;


""")

# FIND SONGS

song_select = ("""

SELECT songs.song_id, artists.artist_id FROM songs
JOIN artists ON songs.artist_id=artists.artist_id
WHERE songs.title = %s AND artists.name = %s AND songs.duration= %s

""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop, songplay_table_drop]