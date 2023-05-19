from flask import Flask, request
from duckduckgo_search import DDGS
app = Flask(__name__)
ddgs = DDGS()

@app.route('/search')
def search():  # put application's code here
    keywords = request.args.get('q')
    max_results = int(request.args.get('max_results') or "3")
    results = ddgs.text(keywords, region='wt-wt', timelimit='m', safesearch='Off')
    return results


if __name__ == '__main__':
    app.run(host='0.0.0.0')
