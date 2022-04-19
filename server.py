from flask import Flask, render_template, request, redirect# added request
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'chiken'
from models.dojo import Dojo
@app.route('/')         # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')
@app.route('/process', methods=['POST'])         # The "@" decorator associates this route with the function immediately following
def process():
    print(request.form)
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    data = {
        "name" : request.form['name'],
        "location": request.form['location'],
        "language" : request.form['language'],
        "comment" : request.form['comment']
    }
    Dojo.save(data)
    return redirect ('/result')


@app.route('/result')
def result():
    return render_template('answers.html',  results = Dojo.get_all())

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.