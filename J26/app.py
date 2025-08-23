from flask import Flask, render_template
import os

app=Flask(__name__)

@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='HOME')

@app.route('/about')
def about():
    name='30 Days Of Python Programming'
    return render_template('about.html', name=name, title='ABOUT US')

@app.route('/post')
def post():
    name = 'Text Analyzer'
    return render_template('post.html', name=name, title=name)

if __name__ == '__main__':
    port=int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)