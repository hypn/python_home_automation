from flask import Flask, render_template
from werkzeug import SharedDataMiddleware

import os

app = Flask(__name__)

app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
  '/': os.path.join(os.path.dirname(__file__), 'static')
})

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/on/<pin_id>')
def on(pin_id):
    return 'Turning pin ' + pin_id + ' ON'

@app.route('/off/<pin_id>')
def off(pin_id):
    return 'Turning pin ' + pin_id + ' OFF'

if __name__ == '__main__':
  app.run(debug=True)