# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
import requests


app = Flask(__name__)
app.debug = True


@app.route('/')
def dashboard():
    # Assuming network traffic is great and nothing will stop all three
    # requests from completing on time.
    data = {
        'billing': requests.get('http://localhost:5001/user/1').json(),
        'inventory': requests.get('http://localhost:5003/product/abc1').json(),
        'shipping': requests.get('http://localhost:5002/user/1').json()}
    print(data)
    return render_template('main.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
