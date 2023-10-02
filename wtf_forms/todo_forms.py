from flask_wtf import FlaskForm
from wtforms import fields, validators

class AddTodoForm(FlaskForm):
    '''Form to add a new todo item'''
    
    priorities = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]
    
    todo_name = fields.StringField(
        label='Todo Name',
        validators=[validators.DataRequired(), validators.Length(min=4, max=30)],
        render_kw={
            'placeholder': 'Ex. Go jogging',
        }
    )
    
    priority = fields.SelectField(
        label='Todo Priority',
        validators=[validators.DataRequired()],
        choices=priorities
    )
    
    completion_date = fields.DateField(
        label='Date of Completion',
        validators=[validators.DataRequired()],
        # format='%d-%m-%Y'
    )
    
    completion_time = fields.TimeField(
        label='Time of Completion',
        validators=[validators.DataRequired()],
        # format='%H:%M'
    )
    

class EditTodoForm(FlaskForm):
    '''Form to edit a todo item'''
    
    priorities = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]
    
    todo_name = fields.StringField(
        label='Todo Name',
        validators=[validators.DataRequired(), validators.Length(min=4, max=30)],
        render_kw={
            'placeholder': 'Ex. Go jogging',
        }
    )
    
    priority = fields.SelectField(
        label='Todo Priority',
        validators=[validators.DataRequired()],
        choices=priorities
    )
    
    completion_date = fields.DateField(
        label='Date of Completion',
        validators=[validators.DataRequired()],
        # format='%d-%m-%Y'
    )
    
    completion_time = fields.TimeField(
        label='Time of Completion',
        validators=[validators.DataRequired()],
        # format='%H:%M'
    )
    