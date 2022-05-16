from flask import render_template, redirect, url_for, Blueprint, request

from favourites import fave_bands, add_to_list, del_from_list 

my_view = Blueprint('my_view', __name__)

@my_view.route("/")
def home():
    return render_template("home.html")

@my_view.route("/contact")
def contact():
    return render_template("contact.html")

@my_view.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        if request.form["band_list"]:
            old_band = request.form["band_entry"]
            del_from_list(old_band)
        new_band = request.form["add_band"]
        add_to_list(new_band)
    return render_template("about.html", bands=fave_bands)

@my_view.route("/home")
def home_redirect():
    return redirect(url_for("my_view.home"))

@my_view.route("/homepage")
def homeb_redirect():
    return redirect(url_for("my_view.home"))

# -------------------------
