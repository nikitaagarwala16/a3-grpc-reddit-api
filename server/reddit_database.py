import sqlite3;

conn = sqlite3.connect('reddit.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
               UserID INTEGER PRIMARY KEY
    )
'''
)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Posts (
        PostID INTEGER PRIMARY KEY,
        AuthorID INTEGER,
        Title TEXT NOT NULL,
        Content TEXT NOT NULL,
        VideoURL TEXT DEFAULT 'NO URL PROVIDED',
        ImageURL TEXT DEFAULT 'No URL PROVIDED',
        Score INTEGER DEFAULT 0,
        State INTEGER,
        PublicationDate TIMESTAMP,
        SubredditID INTEGER,
        FOREIGN KEY (AuthorID) REFERENCES Users(UserID),
        FOREIGN KEY (SubredditID) REFERENCES Subreddits(SubredditID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Comments (
        CommentID INTEGER PRIMARY KEY AUTOINCREMENT,
        AuthorID INTEGER,
        PostID INTEGER DEFAULT -1,
        ParentCommentID INTEGER DEFAULT -1,
        Content TEXT NOT NULL,
        Score INTEGER DEFAULT 0,
        State INTEGER,
        PublicationDate TIMESTAMP,
        FOREIGN KEY (AuthorID) REFERENCES Users(UserID),
        FOREIGN KEY (PostID) REFERENCES Posts(PostID),
        FOREIGN KEY (ParentCommentID) REFERENCES Comments(CommentID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Subreddits (
        SubredditID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Visibility INTEGER,
        Tags TEXT
    )
''')
conn.commit()
conn.close()

