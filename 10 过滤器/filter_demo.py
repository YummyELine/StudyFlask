# encoding: utf-8

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return render_template('index.html',
    # avatar='https://gss0.bdstatic.com/6LZ1dD3d1sgCo2Kml5_Y_D3/sys/portrait/item/9847e9a39ee5a4a9e8bdaee59b9ee78cab5a1a')
    comments = [
        {
            'user': '小E',
            'content': 'xxx'
        },
        {
            'user': 'ee',
            'content': 'x'
        }
    ]
    return render_template('index.html', comments=comments)


if __name__ == '__main__':
    app.run(debug=True)
