# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify


app = Flask(__name__)
app.debug = True


@app.route('/user/<user_id>')
def user_shipments(user_id):
    print('Getting shipments for user: {}'.format(user_id))
    response = jsonify({
        'data': {
            'shipments': [
                {'name': 'teddy bear 123', 'arrival_date': '12/25/2015'},
                {'name': 'chocolate cookies', 'arrival_date': '12/23/2015'},
            ]
        }
    })
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5002)
