from flask import *
app = Flask(__name__)  
@app.route("/")
def login():
    return render_template("login.html")
@app.route("/home")
def home():
    username = request.args.get("username")
    password = request.args.get("password")
    print(username,password)
    return render_template("home.html",noidung="AI tra ")
@app.route("/ai")
def ai():
    import json
    with open("kanji.json","r",encoding="utf-8") as f:
        data = json.load(f)
    dulieu = request.args.get("tin_nhan")
    if dulieu in data:
        dulieu = f"âm on {data[dulieu]["readings_on"]}, âm kun {data[dulieu]["readings_kun"]}"
    else:
        dulieu="tôi không biết"
    return render_template("home.html",noidung=dulieu)
if __name__ == "__main__":
    app.run()