from flask import Flask, render_template # here we put our flask imports
from views import my_view # here we put our local imports

app = Flask(__name__)

app.register_blueprint(my_view)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", e=e)

if __name__=="__main__":
    app.run(debug=True, port=8000)

