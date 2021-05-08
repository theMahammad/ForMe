from app import app
from flask import render_template,redirect,request
from app.models import *


@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')
@app.route("/admin/categories" ,methods = ['GET','POST'])
def categories():
    categories = Category.query.all()
    if request.method=="POST":
        
        category_name = request.form['category_name']
        category=Category(name = category_name)
        db.session.add(category)
        db.session.commit()
        return redirect("/admin/categories")
    return render_template("admin/categories.html",categories=categories)
@app.route("/admin/categories/delete/<int:id>")
def delete_categories(id):
    forDeleteCategory = Category.query.get(id)
    db.session.delete(forDeleteCategory)
    db.session.commit()
    return redirect("/admin/categories")
@app.route("/admin/categories/update/<int:id>",methods=["GET","POST"])
def update_categories(id):
    forUpdateCategory = Category.query.get(id)
    if request.method=="POST":
        forUpdateCategory.name=request.form['category_name']
        db.session.commit()
        return redirect("/admin/categories")

    return render_template("admin/update_categories.html",forUpdateCategory = forUpdateCategory)
@app.route("/admin/advantages",methods=["GET","POST"])
def advantages():
    advantages = Advantage.query.all()
    if request.method=="POST":
        adv_icon=request.form['advantage_icon']
        adv_text = request.form['advantage_text']
        advantage = Advantage(icon = adv_icon,text= adv_text)
        db.session.add(advantage)
        db.session.commit()
        return redirect("/admin/advantages")
    return render_template("admin/advantages.html")






