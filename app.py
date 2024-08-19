from flask import Flask,render_template,request
import google.generativeai as palm

api="AIzaSyAairy61urxq7bs4uN79aNd9kHMAj5hPe0"
palm.configure(api_key=api)
model = {"model": "models/chat-bison-001"}

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/financial_FAQ",methods=["GET","POST"])
def financial_FAQ():
    return render_template("financial_FAQ.html")

@app.route("/singapore_joke", methods=["GET","POST"])
def singapore_joke():
    return render_template("singapore_joke.html")

@app.route("/makersuite",methods=["GET","POST"])
def makersuite():
    q=request.form.get("q")
    r=palm.chat(messages=q, **model)
    return render_template("makersuite.html",r=r.last)



if __name__=="__main__":
    app.run()

    