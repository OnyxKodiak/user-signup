from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/', methods=['POST'])
def handleSubmit():
    userid = request.form.get("username")
    verify = request.form.get("verify")
    password = request.form.get("password")
    email = request.form.get("email")
    error = ""
    error_count = 0
    if verify != password:
        error = "Password must match above."
        error_count = 1
        return render_template("index.html", userid=userid, pass_valid=error)

    
    if email != "":
        count_amp = email.count("@")
        count_punto = email.count(".")
        count_sp = email.count(" ")
        if not(count_amp == 1 and count_punto == 1 and count_sp == 0):
            error = "Not a valid email"
            error_count = 1
            return render_template("index.html", userid=userid, email_valid=error)

    if error_count < 1:
        return render_template("welcome.html", userid=userid)

app.run()