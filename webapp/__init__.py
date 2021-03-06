from flask import Flask, render_template

from PythonHomeW.webapp.python_org_new import get_python_news
from PythonHomeW.webapp.weather import weather_by_city


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    @app.route('/')
    def index():
        title = "Новости python"
        weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        news_list = get_python_news()
        return render_template("index.html", page_title=title, weather=weather, news_list=news_list)

    return app
