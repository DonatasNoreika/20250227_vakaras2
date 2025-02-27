import sqlite3

conn = sqlite3.connect("biudzetas.db", check_same_thread=False)
c = conn.cursor()

with conn:
    c.execute("CREATE TABLE IF NOT EXISTS irasas (suma integer)")

def nuskaityti():
    with conn:
        c.execute("SELECT * FROM irasas")
        irasai = c.fetchall()
        naujas_zurnalas = []
        for irasas in irasai:
            naujas_zurnalas.append(int(irasas[0]))
    return naujas_zurnalas

def irasyti(suma):
    with conn:
        c.execute(f"INSERT INTO irasas VALUES ({suma})")
