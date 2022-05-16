from flask import render_template, redirect, url_for, Blueprint, request

my_view = Blueprint('my_view', __name__)

@my_view.route("/")
def home():
    return render_template("index.html")

@my_view.route("/admin")
def admin():
    return render_template("admin.html")

@my_view.route("/page1")
def page1():
    return render_template("page1.html")

@my_view.route("/page2")
def page2():
    return render_template("page2.html")

@my_view.route("/page3")
def page3():
    return render_template("page3.html")

@my_view.route("/page4")
def page4():
    return render_template("page4.html")

@my_view.route("/page5")
def page5():
    return render_template("page5.html")

@my_view.route("/home")
def home_redirect():
    return redirect(url_for("my_view.home"))

@my_view.route("/homepage")
def homepage_redirect():
    return redirect(url_for("my_view.home"))

@my_view.route("/js")
def js_redirect():
    return redirect(url_for("my_view.home"))

@my_view.route("/javascript")
def javascript_redirect():
    return redirect(url_for("my_view.home"))