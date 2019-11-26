from flask import *
from TebNoteApp import main
import os
from subprocess import *
#import cardoza_make_a_move

app = Flask(__name__)

@app.route('/')
def start():
  return Note()

@app.route('/layout')
def layout():
  return render_template('layout.html')

@app.route('/NoteApp', methods=["GET","POST"])
def Note():
  if request.method == "POST":
    note = request.form["Note"]
    res_ = main(note)
    return render_template('NoteApp.html', note=res_[0], copy=res_[1], matches=res_[2])
  else:
    return render_template('NoteApp.html')

if __name__ == '__main__':
  app.run(host="0.0.0.0", port="8000", debug=False)