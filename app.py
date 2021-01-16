from flask import Flask
from flask import request, g
from flask import make_response

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>You brower is {}</p>'.format(user_agent)
    # return 'hello, world!'


@app.route('/test', methods=['GET', 'POST'])
def test():
    print(g.user)
    return ''


@app.route('/test2')
def test2():
    response = make_response('hello test2')
    response.set_cookie('answer', '42')
    return response

@app.before_request
def test1():
    g.user = 'nhb'      # 给全局变量g赋值
    print('before_request')


@app.before_first_request
def test3():
    print('before first request')


@app.after_request
def test2(res):
    print('after request')
    return res


@app.teardown_request
def test3(res):
    print('teardown request')
    return res


if __name__ == '__main__':
    app.run()
