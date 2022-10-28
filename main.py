from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/')
def home():
    return render_template("index.html", year=datetime.now().year)


if __name__ == "__main__":
    app.run(debug=os.environ.get('DEBUG'), host='0.0.0.0')
