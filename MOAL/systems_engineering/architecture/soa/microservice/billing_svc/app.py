# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify


app = Flask(__name__)
app.debug = True


@app.route('/user/<user_id>')
def user_billings(user_id):
    print('Getting billings for user: {}'.format(user_id))
    response = jsonify({
        'data': {
            'transactions': [
                {'id': '1234', 'products': [{'foo': 'bar'}, {'foo': 'bar'}]},
                {'id': '4231', 'products': [{'bar': 'foo'}, {'bar': 'foo'}]},
            ]
        }
    })
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5001)
