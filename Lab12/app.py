from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def main():
     dane = {'tytul': 'Strona główna', 'tresc': 'Witaj na stronie głównej.'}
     return render_template('index.html', tytul = dane['tytul'], tresc = dane['tresc'])

@app.route("/dodaj")
def dodaj():
    dane = {'tytul': 'Dodaj pracownika', 'tresc': 'Dodaj pracownika.'}
    return render_template('dodaj.html', tytul = dane['tytul'], tresc = dane['tresc'])

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            imienazwisko = request.form['imienazwisko']
            nrpracownika = request.form['nrpracownika']
            adres = request.form['adres']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?, ?, ?)", (imienazwisko, nrpracownika, adres))
                con.commit()
                msg = "Sukces. Rekord zapisany"
        except:
            con.rollback()
            msg = "Blad. Rekord niezapisany"
        finally:
            return render_template("rezultat.html", tytul = "Rezultat", tresc = msg)
            con.close()

@app.route("/lista")
def lista():
    dane = {'tytul': 'Lista pracownikow', 'tresc': 'Lista pracowników'}
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM pracownicy")
    rekordy = cur.fetchall()
    con.close()
    return render_template('lista.html', tytul = dane['tytul'], tresc = dane['tresc'], rekordy = rekordy)
    
if __name__ == "__main__":
    app.run()