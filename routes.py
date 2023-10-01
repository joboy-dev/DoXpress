from flask import typing as ft
from __init__ import *


class HomeView(View):
    '''Home page view'''
    
    def dispatch_request(self):
        return render_template('index.html', year=year, active_link='home', user=current_user)

app.add_url_rule('/', view_func=HomeView.as_view(name='home'))

# ------------------------------- USER ------------------------------- #

class SignUpView(View):
    '''View to handle account creation for users'''
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self):
        form = SignUpForm(request.form)
        
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            password2 = form.password2.data
            
            if password != password2:
                flash('Your passwords do not match.', category='error')
            else:
                if not is_valid_password(password) or not is_valid_password(password2):
                    flash('One of your passwords is invalid.')
                else:
                    # hash valid password
                    hashed_password = generate_password_hash(password)
                    
                    # create user object
                    user = User(
                        username=username,
                        password=hashed_password
                    )
                    session.add(user)
                    session.commit()
                    
                    login_user(user=user)
                    flash(f'Account created. Welcome @{username}', category='success')
                    
                    return redirect(url_for('home'))
        
        return render_template('forms/signup.html', active_link='signup', form=form, user=current_user)

app.add_url_rule('/signup', view_func=SignUpView.as_view(name='signup'))


class LoginView(View):
    '''View to handle login of users'''
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self):
        form = LoginForm(request.form)
        
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            
            user = session.query(User).filter_by(username=username).first()
            
            # check if username does not exist
            if user is None:
                flash('This user does not exist.', category='error')
            else:
                # check password against hashed password in database
                if not check_password_hash(user.password, password):
                    flash('Your password is incorrect.', category='error')
                else:
                    login_user(user=user)
                    
                    flash(f'Welcome @{username}', category='success')
                    return redirect(url_for('home'))
        
        return render_template('forms/login.html', active_link='login', form=form, user=current_user)

app.add_url_rule('/login', view_func=LoginView.as_view(name='login'))


class LogoutView(View):
    '''View to logout current user'''
    
    def dispatch_request(self):
        logout_user()
        flash('See you soon. Goodbye.', category='message')
        return redirect(url_for('home'))
        
app.add_url_rule('/logout', view_func=LogoutView.as_view(name='logout'))



# ------------------------------- TODOS ------------------------------- #

class AddTodoView(View):
    '''View to add new todo items'''
    
    methods = ['GET', 'POST']
    decorators = [login_required]
    
    def dispatch_request(self):
        form = AddTodoForm(request.form)
        
        if form.validate_on_submit():
            todo_name = form.todo_name.data
            priority = form.priority.data
            completion_date = form.completion_date.data.strftime('%d-%m-%Y')
            completion_time = form.completion_time.data.strftime('%H:%M')
            
            # create todo object
            todo = Todo(
                todo_name=todo_name,
                priority=priority,
                completion_date=completion_date,
                completion_time=completion_time, 
                owner_id = current_user.id
            )
            
            session.add(todo)
            session.commit()
            
            flash('Todo created successfully', category='success')
            return redirect(url_for('home'))
        
        return render_template('forms/add-todo.html', active_link='add_todo', user=current_user, form=form)

app.add_url_rule('/todo/add', view_func=AddTodoView.as_view(name='add_todo'))


class EditTodoView(View):
    '''View to edit todo items'''
    
    methods = ['GET', 'POST']
    decorators = [login_required]
    
    def dispatch_request(self, id):
        todo_item = db.get_or_404(Todo, ident=id)
        
        form = EditTodoForm(obj=todo_item)
        
        if form.validate_on_submit():
            form.populate_obj(obj=todo_item)
            
            if todo_item.owner_id == current_user.id:
                session.commit()
                flash('Todo updated.', category='success')
                return redirect(url_for('home'))
            else:
                return abort(code=401)
            
        return render_template('forms/edit-todo.html', active_link='edit_todo', user=current_user, form=form)

app.add_url_rule('/todo/<int:id>/edit', view_func=EditTodoView.as_view(name='edit_todo'))


class ChangeCompletedStatus(View):
    '''View to change a todo's completed status'''
    
    decorators = [login_required]
    
    def dispatch_request(self, id):
        todo_item = db.get_or_404(Todo, ident=id)
        
        if todo_item.owner_id == current_user.id:
        
            if todo_item.is_complete:
                flash('Sorry, his todo has been marked as complete.', category='error')
            else:
                todo_item.is_complete = True
                session.commit()
                flash('Todo markeed as complete.', category='success')
        
            return redirect(url_for('home'))
        else:
            return abort(code=401)
        
app.add_url_rule('/todo/<int:id>/complete', view_func=ChangeCompletedStatus.as_view(name='complete_todo'))


class DeleteTodoView(View):
    '''View to delete todo items'''
    
    decorators = [login_required]
    
    def dispatch_request(self, id):
        todo_item = db.get_or_404(Todo, ident=id)
        
        if todo_item.owner_id == current_user.id:
            session.delete(todo_item)
            session.commit()
            
            flash('Todo deleted.', category='success')
            return redirect(url_for('home'))
        else:
            return abort(code=401)

app.add_url_rule('/todo/<int:id>/delete', view_func=DeleteTodoView.as_view(name='delete_todo'))


# Run app
if __name__ == '__main__':
    app.run(debug=True)