from flask import *  # сперва подключим модуль

app = Flask(__name__)  # объявим экземпляр фласка

@app.route('/')
def main():

    output = "Flask is up and running"
    return output

app.run()  # запустим сервер на 8000 порту!
