from app import app
from flask import render_template,redirect,request

@app.route('/')
def main_index():
    return render_template('main/index.html')

@app.route('/categories')
def main_categories():
    return render_template('main/categories.html')