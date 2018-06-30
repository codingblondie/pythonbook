from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def hello() -> '302':
	return redirect('/entry')

def search4letters(phrase: str, letters: str = 'aeiou') -> set:
	return set(letters).intersection(set(phrase))

@app.route('/search4', methods = ['POST'])
def do_search() -> 'html':
	phrase = request.form['phrase']
	letters = request.form['letters']
	title = 'Here are your results:'
	results = str(search4letters(phrase, letters))
	return render_template('results.html', the_letters = letters, the_phrase = phrase, the_results = results, the_title = title)
 
@app.route('/entry')
def entry_page() -> 'html':
	return render_template('entry.html', the_title = 'Welcome to search4letters on the web!')
app.run(debug=True)