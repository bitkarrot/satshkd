from flask import Flask, render_template, request
from calculate import get_10year
from translate import get_strings

app = Flask(__name__)

@app.route("/zh-cn/")
def template_cn():
    lang = 'zh-cn'
    my_list = get_10year(lang)
    items = get_strings(lang)
    return render_template('index.html', my_list=my_list, desc=items)

@app.route("/zh-hk/")
def template_hk():
    lang = 'zh-hk'
    my_list = get_10year(lang)
    items = get_strings(lang)
    return render_template('index.html', my_list=my_list, desc=items)

@app.route('/')
def root():
    lang = 'en'
    my_list = get_10year(lang)
    items = get_strings(lang)
    return render_template('index.html', my_list=my_list, desc=items)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
