from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')
	
@app.route("/about")
def about_me():
    return render_template('omnie.html')

@app.route('/about/<name>')
def user(name):
	return render_template('omnie1.html', name=name)	

if __name__ == "__main__":
    app.run()
