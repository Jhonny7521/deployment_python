from flask import render_template, redirect, session, request, flash, session
from flask_app import app
# from flask_app.controllers.user_controller import appointments
from flask_app.models.show_model import Show   

from flask_app.models.user_model import User


@app.route("/new")
def new_show():
    
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "id": session['user_id']
    }
 
    user = User.get_by_id(data)

    return render_template('add_show.html', user = user)

@app.route("/create/show", methods = ['post'])
def create_show():

    if 'user_id' not in session:
        return redirect('/')

    print(request.form)
    
    if not Show.valida_show(request.form):
        return redirect('/new')

    id = Show.save_show(request.form)

    print(f"El Show {id} fue registrado")
    return redirect("/dashboard")

@app.route('/edit/<int:id>')
def edit_show(id):
    
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "id": session['user_id']
    }

    user = User.get_by_id(data)

    data_show = {
        "id": id
    }

    show = Show.get_by_id(data_show)

    return render_template('edit_show.html', user = user, show=show)

@app.route('/update', methods=['POST'])
def update_show():
    if 'user_id' not in session:
        return redirect('/')

    if not Show.valida_show(request.form):
        return redirect('/edit/'+request.form['id'])

    Show.update_show(request.form)

    return redirect('/dashboard')

@app.route("/show/<int:id>")
def show_tvshow(id):
    if 'user_id' not in session:
        return redirect('/')

    data_show = {
        "id": id
    }

    show = Show.get_by_id(data_show)

    data_user = {
        "id": show.user_id
    }

    creator = User.get_by_id(data_user)

    return render_template("show_tvshow.html", show=show, creator = creator)

@app.route("/delete/<int:id>")
def delete_show(id):

    if 'user_id' not in session:
        return redirect('/')

    data = {
        "id": id
    }

    Show.delete(data)
    return redirect("/dashboard")

@app.route("/like/<int:id>/<int:like>")
def like_show(id, like):

  if 'user_id' not in session:
        return redirect('/')

  data = {
      "user_id": session['user_id'],
      "show_id": id
  }

  id = Show.like_show_save(data)

  print(f"El like de Show {id} fue guardado")

  data2 = {
    'id': id,
    'like': like + 1
  }

  updt = Show.update_show_like(data2)

  print(f"El like de Show {updt} fue actualizado")
  return redirect("/dashboard")
