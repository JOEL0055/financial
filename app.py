from flask import Flask, render_template, request
import random

app = Flask(__name__)

jokes = [
    "The only thing faster than Singapore's MRT during peak hours is the way we 'chope' seats with a tissue packet.",
    "Why did the chicken cross the road in Singapore? To get away from the ERP!"
]

news = [
    "Jay Powell has signalled he is ready to cut US interest rates in September, as he warned that 'downside risks' to the labour market had increased.",
    "Singapore's economy is expected to grow by 4% this year, driven by strong manufacturing and exports."
]

@app.route('/', methods=['GET', 'POST'])
def index():
    joke = None
    news_item = None
    if request.method == 'POST':
        if 'joke_button' in request.form:
            joke = random.choice(jokes)  # Randomizing the joke
        elif 'news_button' in request.form:
            news_item = random.choice(news)  # Randomizing the news

    return render_template('index.html', joke=joke, news=news_item)

if __name__ == '__main__':
    app.run(port=5006)
