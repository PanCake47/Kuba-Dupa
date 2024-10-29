import sqlite3

def create_database():
    conn = sqlite3.connect('words.db')  
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY,
            word TEXT NOT NULL
        )
    ''')
    
    words = [
        ("mango",), ("kiwi",), ("banana",), ("made",), ("was",),
        ("strict",), ("parent",), ("lover",), ("clever",), 
        ("continuous",), ("miserable",), ("project",), ("fight",), 
        ("astronaut",), ("cosmos",), ("leaver",), ("port",), 
        ("computer",), ("monkey",), ("float",), ("trumpet",), 
        ("globe",), ("apple",), ("orange",), ("grape",), ("peach",),
        ("cherry",), ("apricot",), ("strawberry",), ("melon",), ("pineapple",),
        ("watermelon",), ("blueberry",), ("blackberry",), ("coconut",), ("passionfruit",),
        ("raspberry",), ("pomegranate",), ("nectarine",), ("plum",), ("kiwifruit",),
        ("bicycle",), ("train",), ("airplane",), ("boat",), ("car",),
        ("motorcycle",), ("skateboard",), ("bus",), ("subway",), ("helicopter",),
        ("rocket",), ("jet",), ("trolley",), ("scooter",), ("van",),
        ("thunder",), ("lightning",), ("rain",), ("snow",), ("sunshine",),
        ("storm",), ("breeze",), ("hurricane",), ("tornado",), ("cloud",),
        ("fog",), ("mist",), ("drizzle",), ("hail",), ("sleet",),
        ("temperature",), ("climate",), ("weather",), ("season",), ("sunset",),
        ("dawn",), ("moonlight",), ("starlight",), ("twilight",), ("galaxy",),
        ("universe",), ("planet",), ("star",), ("comet",), ("asteroid",),
        ("nebula",), ("black",), ("supernova",), ("satellite",), ("orbit",),
        ("space",), ("exploration",), ("gravity",), ("eclipse",), ("telescope",),
        ("astronomy",), ("cosmonaut",), ("explorer",), ("scientist",), ("researcher",),
        ("experiment",), ("theory",), ("hypothesis",), ("data",), ("analysis",),
        ("discovery",), ("innovation",), ("technology",), ("invention",), ("creativity",),
        ("imagination",), ("idea",), ("concept",), ("design",), ("development",),
        ("solution",), ("strategy",), ("planning",), ("organization",), ("system",)
    ]
    
    cursor.executemany('INSERT INTO words (word) VALUES (?)', words)
    
    conn.commit()
    conn.close()

create_database()
