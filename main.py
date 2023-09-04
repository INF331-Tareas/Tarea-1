import sqlite3
import logging
from functs import show_get_next_step
from crypt import AESCipher
logging.basicConfig(filename="pass.log", level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")

passkey = 'alkdjaslkdjalskj1209381290'

try:
    con = sqlite3.connect("pass.db")

    cur = con.cursor()

except Exception as e:
    logging.error('Couldnt connect to database')
    logging.error(e)
    print("Error: ", e)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS pass (id INTEGER PRIMARY KEY, name TEXT, password TEXT, keyword TEXT)")
    con.commit()
except Exception as e:
    logging.error('Couldnt create table')
    logging.error(e)
    print("Error: ", e)

try:
    cy = AESCipher(passkey)
except:
    logging.error('Couldnt create cipher')
    print("Error: ", e)

ns = show_get_next_step()
while ns != 5:
    if ns == 1:
        name = input('Enter name: ')
        password = input('Enter password: ')
        keyword = input('Enter keyword: ')
        passord = cy.encrypt(password)
        try:
            cur.execute("INSERT INTO pass (name, password, keyword) VALUES (?, ?, ?)", (name, cy.encrypt(password), keyword))
            con.commit()
        except Exception as e:
            logging.error('Couldnt insert into table')
            logging.error(e)
            print("Error: ", e)
    elif ns == 2:
        name = input('Enter name: ')
        #missing search
        #keyword = input('Enter keyword: ')
        try:
            cur.execute("SELECT password FROM pass WHERE name=?", (name))
            con.commit()
            rows = cur.fetchall()
            for row in rows:
                print(cy.decrypt(row[0]))
        except Exception as e:
            logging.error('Couldnt select from table')
            logging.error(e)
            print("Error: ", e)
    elif ns == 3:
        name = input('Enter name: ')
        password = input('Enter password: ')
        #keyword = input('Enter keyword: ')
        try:
            cur.execute("UPDATE pass SET password=? WHERE name=?", (cy.encrypt(password), name))
            con.commit()
        except Exception as e:
            logging.error('Couldnt update table')
            logging.error(e)
            print("Error: ", e)
    elif ns == 4:
        name = input('Enter name: ')
        try:
            cur.execute("DELETE FROM pass WHERE name=??", (name))
            con.commit()
        except Exception as e:
            logging.error('Couldnt delete from table')
            logging.error(e)
            print("Error: ", e)
    elif ns == 5:
        break
    ns = show_get_next_step()