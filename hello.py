from flask import Flask, url_for, render_template

#web framework
#knihovna co umožňuje tvořit webové servery

app = Flask(__name__) #jméno aktuálního modulu

@app.route('/')
def index():
	return 'Ahoj, PyLadies!'
#view function

@app.template_filter('cap')
def capitalize(word):
	return word[0].upper() + word[1:]

@app.route('/url/')
def url():
	return url_for('hello', name= 'Šáuí', count=123, _external=True)

@app.route('/hello/')
@app.route('/hello/<name>/')
@app.route('/hello/<name>/<int:count>/')
def hello(name='world', count=1):
		return render_template('hello.html', name=name)
