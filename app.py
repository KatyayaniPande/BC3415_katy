from flask import Flask, render_template, request
from textblob import TextBlob  # Importing TextBlob for sentiment analysis
from transformers import pipeline  # Importing transformer pipeline for sentiment analysis
import google.generativeai as genai



api = "AIzaSyAairy61urxq7bs4uN79aNd9kHMAj5hPe0"  # Replace with your actual API key
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/financial_FAQ", methods=["GET", "POST"])
def financial_FAQ():
    return render_template("financial_FAQ.html")

@app.route("/singapore_joke", methods=["GET", "POST"])
def singapore_joke():
    return render_template("singapore_joke.html")

@app.route("/makersuite", methods=["GET", "POST"])
def makersuite():
    q = request.form.get("q")
    r = model.generate_content(q)
    return(render_template("makersuite.html",r=r.text))
# New route for sentiment analysis
@app.route("/sentiment_analysis", methods=["GET", "POST"])
def sentiment_analysis():
    if request.method == "POST":
        user_text = request.form.get("text")
        if not user_text:
            return render_template("sentiment_input.html", error="Please enter text for analysis.")

        try:
            # Perform sentiment analysis using TextBlob
            textblob_sentiment = TextBlob(user_text).sentiment
            
            return render_template("sentiment_analysis.html", 
                                   textblob_sentiment=textblob_sentiment)
        except Exception as e:
            return render_template("sentiment_input.html", error=f"An error occurred: {str(e)}")
    
    return render_template("sentiment_input.html")
if __name__ == "__main__":
    app.run(debug=True)


