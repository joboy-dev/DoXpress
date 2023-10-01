from flask_wtf import FlaskForm
from wtforms import fields, validators

class SignUpForm(FlaskForm):
    '''Form to create account for users'''
    
    username = fields.StringField(
        label='Enter Username',
        validators=[validators.DataRequired(), validators.Length(min=4, max=30)],
        render_kw={
            'placeholder': 'Ex. johndoe123',
        }
    )
    
    password = fields.PasswordField(
        label='Enter Password',
        validators=[validators.DataRequired()],
        render_kw={
            'placeholder': 'Ex. Johndoe@123',
        }
    )
    
    password2 = fields.PasswordField(
        label='Confirm Password',
        validators=[validators.DataRequired()],
        render_kw={
            'placeholder': 'Ex. Johndoe@123',
        }
    )
    

class LoginForm(FlaskForm):
    '''Form to login users'''
    
    username = fields.StringField(
        label='Enter Username',
        validators=[validators.DataRequired(), validators.Length(min=4, max=30)],
        render_kw={
            'placeholder': 'Ex. johndoe123',
        }
    )
    
    password = fields.PasswordField(
        label='Enter Password',
        validators=[validators.DataRequired()],
        render_kw={
            'placeholder': 'Ex. Johndoe@123',
        }
    )
    