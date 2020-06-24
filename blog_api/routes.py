from flask import jsonify,request
from . import app,bcryt,db
from .models import Post,User
from flask_login import login_user,logout_user,current_user



@app.route('/')
def hello():
    return jsonify({"message": "Welcome to the blog API"})


@app.route('/signup',methods=['POST'])
def add_user():
    username=request.json.get('username')
    email=request.json.get('email')
    password=str(request.json.get('password'))
    

    print(password)
    pwd_hash=bcryt.generate_password_hash(password)
    new_user=User(username=username,email=email,password=pwd_hash)
    db.session.add(new_user)
    db.session.commit()

    resource={
        "name":username,
        "email":email,
        "password":password
    }

    return jsonify(
        {
            "message":"Resource Created",
            "resource":resource
        }
    )


#get all users
@app.route('/users',methods=['GET'])
def get_users():
    users=User.query.all()

    user_list=[]

    for i in users:
        user={}
        user['username']=i.username
        user['email']=i.email
        user['password']=i.password

        user_list.append(user)

    return jsonify(
        {"message":"Users",
         "users":user_list
        }
    )


#login
@app.route('/login',methods=['POST'])
def login():

    username=request.json.get('username')
    password=request.json.get('password')

    user=User.query.filter_by(username=username).first()

    if user and bcryt.check_password_hash(user.password,password):
        login_user()

        return jsonify({
            "message": "You are logged in"
        })
    else:
        return jsonify({
            "message":"Invalid Login"
        })



    
