from flask import Flask,request
import avinit
app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get('name')
    avatar = avinit.get_svg_avatar(name)
    return avatar

if __name__ == '__main__':
    app.run()
