from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
     dane = {'tytul':'Strona główna', 'tresc':'Witaj na stronie głównej.'}
     return render_template('index.html', tytul=dane['tytul'], tresc=dane['tresc'])

	
@app.route("/about")
def about():
     dane = {'tytul':'O mnie', 'tresc':'Nazywam się Alicja z Krainy Czarów.'}
     return render_template('omnie.html', tytul=dane['tytul'], tresc=dane['tresc'])

@app.route('/info')
def info():
    posty = [
        {
         'author': {'username': 'Janek'},
         'body': 'Słonecznie w Elblągu!'
        },
        {
         'author': {'username': 'Kasia'},
         'body': 'Film Kroll ma ciekawa fabule.'
    }]
    dane = {'tytul':'Informacje', 'tresc':'Dużo informacji.'}
    return render_template('info.html', tytul=dane['tytul'], tresc=dane['tresc'], posty=posty)
 
@app.route("/kontent")
def kontent():
     dane = {'tytul':'Kontent', 'tresc':'To jest kontent...'}
     return render_template('kontent.html', tytul=dane['tytul'], tresc=dane['tresc'])
	
if __name__ == "__main__":
	app.run()
