from flask import Flask, flash, redirect, render_template, request, send_from_directory
from random import randint
from calculate import get_10year

app = Flask(__name__)

@app.route("/cn/")
def template_test():
    # do the computation here
    my_list = get_10year('cn')
    return render_template('cn.html', my_list=my_list)

@app.route('/')
def root():
    my_list = get_10year('en')
    return render_template('index.html', my_list=my_list)

'''
@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)
'''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
