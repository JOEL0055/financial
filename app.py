from flask import Flask, render_template, request
import joblib ib  # Import the joblib library
import os

app = Flask(__name__, template_folder="/Users/joelaiweithai/Downloads/templates")


# Load the trained model
model = joblib.load('/Users/joelaiweithai/Downloads/house_price_model.pkl')

# Singapore jokes and financial news
singapore_jokes = [
    "The only thing faster than Singapore's MRT during peak hours is the way we 'chope' seats with a tissue packet.",
    "In Singapore, the safest way to cross the road is to jaywalk... Just kidding, follow the green man!",
    "Why did the durian cross the road? To 'chope' the best spot at the hawker centre!"
]

financial_news = [
    "Jay Powell has signalled he is ready to cut US interest rates in September, as he warned that 'downside risks' to the labour market had increased.",
    "Global markets remain volatile amid ongoing trade tensions between the US and China.",
    "Tech stocks surged today as investors anticipated strong earnings reports from industry leaders."
]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    joke = None
    news = None

    if request.method == "POST":
        if 'square_feet' in request.form:
            # Predict the house price
            square_feet = float(request.form['square_feet'])
            predicted_price = model.predict([[square_feet]])[0]
            prediction = f"Predicted Price: ${predicted_price:,.2f}"

        if 'joke_button' in request.form:
            # Display a random Singapore joke
            joke = singapore_jokes[int(request.form['joke_button']) % len(singapore_jokes)]
        
        if 'news_button' in request.form:
            # Display a random financial news item
            news = financial_news[int(request.form['news_button']) % len(financial_news)]

    return render_template("index.html", prediction=prediction, joke=joke, news=news)

if __name__ == "__main__":
    app.run(port=5005)
