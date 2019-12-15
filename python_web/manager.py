from sanic import Sanic,response
from sanic.response import *

from admin.admin import admin

app = Sanic(__name__)

from core import auth
app.config.AUTH_LOGIN_ENDPOINT = 'admin.login'
auth.setup(app)

app.blueprint(admin, url_prefix='admin') #蓝印

app.static('/static', './static') # /static
app.static('/favicon.ico', './static/b.png') # /favicon.ico 网站logo

#session
session = {}
# 存入session
@app.middleware('request')
async def add_session(request):
    request['session'] = session
#根重定向    
@app.route('/')
async def home(request):
    print(request['session'])
    if '_auth' in request['session']:
        user = request['session']['_auth']
    return redirect('/admin/login') 

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
