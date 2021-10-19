from flask import Flask, render_template, request

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
else:
    app.debug = False

# ---------------------------setup webapp structure/routing----------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download():
    return render_template('download.html')

if __name__ == '__main__':
    app.run()
