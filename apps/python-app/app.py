import elasticapm
from elasticapm.contrib.flask import ElasticAPM
import logging

from flask import Flask, render_template, jsonify

app = Flask(__name__)


app.config['ELASTIC_APM'] = {
    # Set required service name. Allowed characters:
    # a-z, A-Z, 0-9, -, _, and space
    'SERVICE_NAME': 'Python Flask APP',

    # Set custom APM Server URL (default: http://localhost:8200)
    'SERVER_URL': 'http://apm-server:8200',

    'DEBUG': True,
}
apm = ElasticAPM(app, logging=logging.ERROR)

@app.route('/')
def hello():
    apm.capture_message('hello, world!')
    return 'Hello world!'

@app.route('/error')
def error():
    try:
        1 / 0
    except ZeroDivisionError:
        apm.capture_exception()

@app.route('/fruits')
def fruits():
    beers = [
        {
            'brand': 'Guinness',
            'type': 'stout'
        },
        {
            'brand': 'Hop House 13',
            'type': 'lager'
        }
    ]
    list_of_fruits = ['banana', 'orange', 'apple']
    list_of_drinks = ['coke', 'milk', beers]
    return jsonify(Fruits=list_of_fruits, Drinks=list_of_drinks)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')        