from testapp import app

@app.route('/test')
def other1():
    return "テストページです！"