import mysql.connector

def make_connection():
    mydb = mysql.connector.connect(host="localhost",
    user="root",
    password="Password",
    auth_plugin='mysql_native_password',
    #The first time you run this leave this line commented out, then uncomment it after you create the database
    database="BandManager")
    #)
    return mydb


def create_database():
    mycursor.execute("CREATE SCHEMA BandManager;")
    
def create_tables(mycursor):
    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS venue (
        venue_id INT NOT NULL AUTO_INCREMENT,
        location VARCHAR(50),
        venue_name VARCHAR(50),
        venue_social VARCHAR(50),
        PRIMARY KEY (venue_id))
    ''')
    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS merch (
        merch_id INT NOT NULL AUTO_INCREMENT,
        item_name VARCHAR(50),
        costPer INT,
        sale_cost INT,
        PRIMARY KEY (merch_id))
    ''')

    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS releases (
        release_id INT NOT NULL AUTO_INCREMENT,
        release_name VARCHAR(50),
        release_date DATE,
        PRIMARY KEY (release_id))
    ''')
    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS song (
        song_id INT NOT NULL AUTO_INCREMENT,
        song_name VARCHAR(50),
        artist_name VARCHAR(50),
        release_id INT,
        PRIMARY KEY (song_id),
        FOREIGN KEY (release_id) REFERENCES releases(release_id))
    ''')
    #Each time a song is played at a gig, it is added to the setList table with the gig_id
    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS setList (
        setList_id INT NOT NULL AUTO_INCREMENT,
        gig_id INT,
        song_id INT,
        PRIMARY KEY (setList_id),
        FOREIGN KEY (song_id) REFERENCES song(song_id))
    ''')
    # Removed refrence to setlist table
    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS gig (
        gig_id INT NOT NULL AUTO_INCREMENT,
        venue_id INT,
        merch_revenue INT,
        top_merch_item_id INT, 
        booker VARCHAR(50),
        ticketsSold INT,
        venue_artist_split DECIMAL,
        date DATE,
        PRIMARY KEY (gig_id),
        FOREIGN KEY (venue_id) REFERENCES venue(venue_id),
        FOREIGN KEY (top_merch_item_id) REFERENCES merch(merch_id))
    ''') 

def insert_data(mycursor):
    sql = "INSERT INTO venue (location, venue_name, venue_social) VALUES (%s, %s, %s)"
    try:
        mycursor.execute(sql, ("1553 N Cahuenga, Los Angeles, California", "Daddy Diamonds", "@daddydiamondshollywood"))
        mycursor.execute(sql, ("1601 s Grand ave, Santa Ana, California", "Find The Good", "@ftg_productions"))
        mydb.commit()
    except:
        #rollback if there is an error
        print("Error inserting venues")
        mydb.rollback()
    try:
        #Inserting releases into table
        sql = "INSERT INTO releases (release_name, release_date) VALUES (%s, %s)"
        mycursor.execute(sql, ("Dance The Inside Out", "2022-5-13"))
        mycursor.execute(sql, ("Freak Beat", "2022-2-13"))
        mycursor.execute(sql, ("Love Songs", "2023-1-13"))

        #Inserting songs into table
        sql = "INSERT INTO song (song_name, artist_name, release_id) VALUES (%s, %s, %s)"
        mycursor.execute(sql, ("Dance The Inside Out", "Sunday Mourners", 1))
        mycursor.execute(sql, ("Freak Beat", "Sunday Mourners", 2))
        # Special songs :)
        mycursor.execute(sql, ("I Love Mary", "Sunday Mourners", 3))
        mycursor.execute(sql, ("Dr. Clibourne is the Best Prof", "Sunday Mourners", 3))
        mycursor.execute(sql, ("Please Give Us An A++", "Sunday Mourners", 3))
        mydb.commit()
    except:
        #rollback if there is an error
        print("Error inserting releases and songs")
        mydb.rollback()
    try:
        #Inserting merch into table
        sql = "INSERT INTO merch (item_name, costPer, sale_cost) VALUES (%s, %s, %s)"
        mycursor.execute(sql, ("T-Shirt", 10, 20))
        mycursor.execute(sql, ("CD", 5, 10))
        mycursor.execute(sql, ("Sticker", 1, 2))
        mycursor.execute(sql, ("Poster", 5, 10))
        mycursor.execute(sql, ("Vinyl", 15, 30))
        mydb.commit()
    except:
        #rollback if there is an error
        print("Error inserting merch")
        mydb.rollback()
    try:

        #Inserting into show table
        sql = "INSERT INTO gig (venue_id, merch_revenue, top_merch_item_id, booker, ticketsSold, venue_artist_split, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, (1, 100, 1, "Mary", 100, 0.5, "2023-1-13"))
        mycursor.execute(sql, (2, 300, 3, "Mary", 100, 0.5, "2023-1-19"))


        #Inserting into setList table
        sql = "INSERT INTO setList (gig_id, song_id) VALUES (%s, %s)"
        mycursor.execute(sql, (1, 1)) 
        mycursor.execute(sql, (1, 2)) 

    except:
        #rollback if there is an error
        mydb.rollback()
        print("Error inserting shows")


    





mydb = make_connection()

mycursor = mydb.cursor()

create_tables(mycursor)
insert_data(mycursor)

mydb.commit()
mydb.close()
