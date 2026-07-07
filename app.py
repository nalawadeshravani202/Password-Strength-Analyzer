print("APP.PY STARTED")

from flask import Flask, render_template, request
from analyzer import analyze_password
from generator import generate_password
from database import *

app = Flask(__name__, static_folder="assets")

create_table()

with open("common_passwords.txt", "r") as f :
          common_passwords = set(line.strip () for line in f)
          
          @app.route("/", methods=["GET", "POST"])
          
          def home():
                  if request.method == "POST":
                          password = request.form["password"]
                          reused = password_exists(password)

                          score, strength, result, suggestions = analyze_password(
                                  password,
                                  common_passwords
                          )
                          
                          if not reused:
                                  save_password(password)
                          
                          return render_template(
                                  "index.html",
                                  password=password,
                                  result=result,
                                  score=score,
                                  strength=strength,
                                  suggestions=suggestions,
                                  reused=reused,
                                  generated=generate_password()
                          )
                  
                  return render_template("index.html")
          
          if __name__ == "__main__":
                  app.run(debug=True)
                  
                        
                        
                        