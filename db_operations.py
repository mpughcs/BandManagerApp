import mysql.connector

def make_connection():
    mydb = mysql.connector.connect(host="localhost",
    user="root",
    password="Mary7763",
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
        venue_name VARCHAR(20),
        PRIMARY KEY (venue_id))
    ''')
    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS merch (
        merch_id INT NOT NULL AUTO_INCREMENT,
        costPer INT,
        sale_cost INT,
        PRIMARY KEY (merch_id))
    ''')

    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS releases (
        release_id INT NOT NULL AUTO_INCREMENT,
        release_name VARCHAR(20),
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
    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS setList (
        setList_id INT NOT NULL AUTO_INCREMENT,
        gig_id INT,
        song_id INT,
        PRIMARY KEY (setList_id),
        FOREIGN KEY (song_id) REFERENCES song(song_id))
    ''')
    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS gig (
        gig_id INT NOT NULL AUTO_INCREMENT,
        venue_id INT,
        booker VARCHAR(50),
        setList_id INT,
        ticketsSold INT,
        venue_artist_split DECIMAL,
        PRIMARY KEY (gig_id),
        FOREIGN KEY (venue_id) REFERENCES venue(venue_id),
        FOREIGN KEY (setList_id) REFERENCES setList(setList_id))
    ''')
# other bands on bill  "set must be chosen from a list of permitted values"
# merch SET(merch_id),
# I'll work on this later
#TODO: add gig_id as a foreign key to setlist


mydb = make_connection()

mycursor = mydb.cursor()

create_tables(mycursor)

mydb.commit()
mydb.close()
