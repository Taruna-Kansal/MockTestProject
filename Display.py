from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Get values from the HTML form
    country = request.form['country']
    exam = request.form['exam']
    
    # Do something with the values
    print("Country:", country)
    print("exam:", exam)
    
    # Return a response
    return "Received data successfully!"

if __name__ == '__main__':
    app.run(debug=True)