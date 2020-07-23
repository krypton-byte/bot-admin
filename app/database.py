import sqlite3
class hits:
    def kemarin():
        db=sqlite3.connect('../data.db')
        c=db.cursor()
        try:
            return c.execute('SELECT * FROM CHAT (cal, count) WHERE cal=date("now","-1 day")').fetchall()[0][1]
        except:
            return 0
    def semua():
        db=sqlite3.connect('../data.db')
        c=db.cursor()
        try:
            return c.execute('SELECT * FROM CHAT').fetchall()[0][1]
        except:
            return 0
    def unread():
        db=sqlite3.connect('data.db')
        c=db.cursor()
        hits=0
        if c.execute('SELECT * FROM UNREAD').fetchall():
            return c.execute('SELECT * FROM UNREAD').fetchall()[0][1]
        else:
            return 0

    def kemarinlusa():
        db=sqlite3.connect('../data.db')
        c=db.cursor()
        try:
            return c.execute('SELECT * FROM CHAT (cal, count) WHERE cal=date("now","-2 day")').fetchall()[0][1]
        except:
            return 0
    def sekarang():
        db=sqlite3.connect('../data.db')
        c=db.cursor()
        try:
            hasil=c.execute(f'SELECT * FROM CHAT WHERE cal=date("now")').fetchall()[0][1]
            db.commit()
            return hasil
        except:
            return 0