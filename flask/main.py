from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='')

@app.route('/table/<sex>/<age>')
def log(sex, age):
    args = {}
    args['title'] = ''
    if sex == 'male':
        if int(age) < 21:
            args['second'] = '/static/images/1.png'
            args['first'] = '/static/images/male1.png'
        else:
            args['second'] = '/static/images/2.png'
            args['first'] = '/static/images/male2.png'
    else:
        if int(age) < 21:
            args['second'] = '/static/images/1.png'
            args['first'] = '/static/images/female1.png'
        else:
            args['second'] = '/static/images/2.png'
            args['first'] = '/static/images/female2.png'

    return render_template('login.html', **args)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')