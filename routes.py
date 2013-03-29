import piface.pfio as pfio
pfio.init()

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

@app.route('/status/<pin_id>')
def status(pin_id):
  global pfio
  return "on" if pfio.digital_read(int(pin_id)) == 1 else "off"

@app.route('/on/<pin_id>')
def on(pin_id):
  global pfio
  pfio.digital_write(int(pin_id), 1)
  state = pfio.digital_read(int(pin_id))
  #print 'Turning pin ' + pin_id + ' ON, state = ' + str(state)
  return "on" if state == 1 else "error"

@app.route('/off/<pin_id>')
def off(pin_id):
  global pfio
  pfio.digital_write(int(pin_id), 0)
  state = pfio.digital_read(int(pin_id))
  #print 'Turning pin ' + pin_id + ' OFF, state = ' + str(state)
  return "off" if state == 0 else "error"

if __name__ == '__main__':
  app.run('0.0.0.0', 80)
