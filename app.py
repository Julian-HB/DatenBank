from flask import Flask

app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
def index():
    print("hallo")
    return {
        "tutorial": "Flask React Heroku"
    }


if __name__ == '__main__':
    app.run()