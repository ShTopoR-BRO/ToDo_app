from flask import Flask, render_template, request, redirect

from BisLog.BisLog import BisLog
from DataBase.DB import DataBase
import os
from dotenv import load_dotenv

load_dotenv()

my_app = Flask(__name__)

db = DataBase(os.getenv("POSTGRES_DB"), os.getenv("POSTGRES_USER"),os.getenv("POSTGRES_PASSWORD"), os.getenv("POSTGRES_HOST"), os.getenv("POSTGRES_PORT"))
connect = db.connect()
bislog = BisLog(connect)

@my_app.route("/")
def general():
    list_ = bislog.show()
    return render_template("index.html", list_=list_)


@my_app.route("/add")
def add_residents():
    return render_template("add.html")

@my_app.route("/create_todo", methods=['POST'])
def create_todo():
    try:
        bisness = request.form['bisness']
        bislog.add(bisness)
        return redirect('/')
    except:
        return render_template('EROR.html')

@my_app.route('/del_bis/<id>')
def del_bis(id):
    bislog.del_(id)
    return redirect("/")