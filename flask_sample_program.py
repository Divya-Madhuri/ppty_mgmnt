from flask import Flask
app = Flask(__name__)
@app.route("/")
def sample_program():
    return "This is sample flask program"
