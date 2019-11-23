from flask import *
from app.TebNoteApp import main
import os
from subprocess import *
#import cardoza_make_a_move

app = Flask(__name__)

notes = []

@app.route('/')
def start():
  #return cardoza_make_a_move.do_the_thing()
  return home()

@app.route('/home')
def home():
  return render_template('home.html')
  
@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/layout')
def layout():
  return render_template('layout.html')

@app.route('/snake')
def snake():
  
  return render_template('snake.html')

@app.route('/NoteApp', methods=["GET","POST"])
def Note():
  if request.method == "POST":
    note = request.form["Note"]
    #Popen(["cd","app"])
    #Popen(["python3","TebNoteApp.py","main","note"],stdout=PIPE ,stderr=STDOUT)
    #print(note)
    res_ = main(note)
    return render_template('NoteApp.html', note=res_[0], copy=res_[1])
  else:
    return render_template('NoteApp.html')

@app.route('/result', methods=["GET","POST"])
def result():
  if request.method == "POST":
    note = request.form.get("Note")
    #Popen(["cd","game/"],shell=True)
    print(note)
    Popen(["python3","TebNoteApp.py",],stdout=PIPE ,stderr=STDOUT)
  #Popen(["main(Note)"])

  return render_template("result.html", name=note)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port="8000", debug=False)