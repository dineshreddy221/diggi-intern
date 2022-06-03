from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_get():
    return render_template("index.html")

@app.route('/feature')
def features():
    return render_template('feature.html')

if __name__ =='__main__':
    app.run(debug=True)