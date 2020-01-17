from flask import  render_template,redirect,flash,url_for,request,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Pomo
from .forms import Pomo_Form, Update_Profile
from .. import db



@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
 
    
    
    return render_template('index.html')
@main.route('/all_pomos')
def all_pomos():
    general = Pomo.query.all()
    
    
    
    return render_template('all_pomos.html',general=general)


@main.route('/new_pomo', methods = ['GET','POST'])
@login_required
def new_pomo():
    form = Pomo_Form()    

    if form.validate_on_submit():
        pomo = Pomo(title = form.title.data, description = form.content.data, author = form.author.data, user_id=current_user.id)

        pomo.save_pomo()
        
        return redirect(url_for('main.all_pomos'))
    
    return render_template('new_pomo.html', pomo_form = form)  

@main.route('/<username>')
@login_required
def profile(username):
    pitch = Pitch.query.filter_by(user_id= current_user.id).all()
    
   
    user = User.query.filter_by(username = username).first()
   
    return render_template('profile.html', user = user, pitch = pitch)
    
@main.route('/<username>/update/pic', methods = ['POST'])
@login_required
def update_profile_pic(username):
    user = User.query.filter_by(username = username).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_img = path
        db.session.commit()

    return redirect(url_for('main.profile', username = username))

@main.route('/user/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = Update_Profile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',username=user.username))

    return render_template('update_profile.html',form =form)


