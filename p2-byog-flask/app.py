from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    """
    TODO: Render the home page provided under templates/index.html in the repository
    """
    return render_template("index.html")

@app.get("/search")
def search():
    """
    TODO:
    1. Capture the word that is being searched
    2. Search for the word on Google and display results
    """
    """ return "TODO" """
    args = request.args.get("q")
    return redirect(f"https://google.com/search?q={args}")

# I am feeling lucky search form code
@app.get("/lucky")
def lucky():
    query = request.args.get("q")
    if not query:
        return "Please enter a search term.", 400
    return redirect(f"https://www.google.com/search?q={query}&btnI=1")

if __name__ == "__main__":
    app.run()