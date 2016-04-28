# -*- coding:utf-8 -*-
__author__ = 'Van.zx'

from flask import Flask, request, render_template, make_response
# from flask.ext.cache import Cache
# from flask.ext.bootstrap import Bootstrap
# from flask.ext.mail import Mail
# from flask.ext.moment import Moment
# from flask.ext.sqlalchemy import SQLAlchemy
# from config import config_dict
import mongo
import sys

import logging
from logging.handlers import RotatingFileHandler
# bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()
# db = SQLAlchemy()
# convert python's encoding to utf8

from en import data as data_en
from zh import data as data_zh
try:
    from imp import reload
    reload(sys)
    sys.setdefaultencoding('utf8')
except (AttributeError, NameError):
    pass


def _import_submodules_from_package(package):
    import pkgutil

    modules = []
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__,
                                                         prefix=package.__name__ + "."):
        modules.append(__import__(modname, fromlist="dummy"))
    return modules


def create_app(config_mode):
    app = Flask(__name__)
    # app.config.from_object(config_dict[config_mode])
    # config_dict[config_mode].init_app(app)
    app.config_mode = config_mode

    # cache = Cache(app, config={'CACHE_TYPE': 'simple'})
    # cache.init_app(app)
    # 内部日志
    rotating_handler1 = RotatingFileHandler('logs/info.log', maxBytes=1 * 1024 * 1024, backupCount=5)
    rotating_handler2 = RotatingFileHandler('logs/error.log', maxBytes=1 * 1024 * 1024, backupCount=2)

    formatter1 = logging.Formatter("-" * 100 +
                                   '\n %(asctime)s %(levelname)s - '
                                   'in %(funcName)s [%(filename)s:%(lineno)d]:\n %(message)s')

    rotating_handler1.setFormatter(formatter1)
    rotating_handler2.setFormatter(formatter1)
    app.logger.addHandler(rotating_handler1)
    app.logger.addHandler(rotating_handler2)

    app.logger.setLevel(logging.INFO)
    rotating_handler2.setLevel(logging.ERROR)
    if app.config.get("DEBUG"):
        # app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.DEBUG)

    # bootstrap.init_app(app)
    # mail.init_app(app)
    # moment.init_app(app)
    # db.init_app(app)

    # from apps.routes import main
    # app.register_blueprint(main)

    @app.route('/home', methods=['GET'])
    @app.route('/index', methods=['GET'])
    @app.route('/', methods=['GET'])
    def index():
        print request.args.get("language")
        lan = request.args.get("language") or request.cookies.get("language", "zh")
        if lan == "en":
            resp = make_response(render_template("index.html", data=data_en))
            resp.set_cookie('language', 'en')
            return resp
        else:
            resp = make_response(render_template("index.html", data=data_zh))
            resp.set_cookie('language', 'zh')
            return resp
        
    @app.route('/organizer', methods=['GET'])
    def owner():
        lan = request.args.get("language") or request.cookies.get("language", "zh")
        if lan == "en":
            data = data_en
        else:
            data = data_zh
        return render_template("organizer.html", data=data)  # cooperate

    @app.route('/partner', methods=['GET'])
    def partner():
        lan = request.args.get("language") or request.cookies.get("language", "zh")
        if lan == "zh":
            return render_template("partner.html", data=data_zh)
        else:
            return render_template("partner.html", data=data_en)  # cooperate

    @app.route('/schedule', methods=['GET'])
    def schedule():
        lan = request.args.get("language") or request.cookies.get("language", "zh")
        if lan == "en":
            return render_template("schedule_en.html", data=data_en)
        else:
            return render_template("schedule.html", data=data_zh)

    @app.route('/sponsor', methods=['GET'])
    def sponsor():
        lan = request.args.get("language") or request.cookies.get("language", "zh")
        if lan == "en":
            return render_template("sponsor_en.html", data=data_en)
        else:
            return render_template("sponsor.html", data=data_zh)

    @app.route('/us', methods=['GET'])
    def contact_us():
        lan = request.args.get("language") or request.cookies.get("language", "zh")
        if lan == "en":
            return render_template("us_en.html", data=data_en)
        else:
            return render_template("us.html", data=data_zh)
    return app
