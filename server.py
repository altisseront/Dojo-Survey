from flask import Flask, render_template, request, redirect, session # added request
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'chiken'
@app.route('/')         # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')
@app.route('/process', methods=['POST'])         # The "@" decorator associates this route with the function immediately following
def process():
    session['name'] = request.form['name']
    session['dojoLocation'] = request.form['dojoLocation']
    session['favLang'] = request.form['favLang']
    session['comment'] = request.form['comment']
    return redirect ('/result')
@app.route('/result')
def result():
    return render_template('answers.html')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.