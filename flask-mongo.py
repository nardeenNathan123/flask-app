from flask import Flask, redirect, render_template , request
from flask_pymongo import PyMongo

app=Flask(__name__,template_folder="test")
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)

@app.route('/users')
def index():
    users=list(mongo.db.Instractor2.find({}))
    if users != []:
        return render_template('users.html',users_html=users)
    else :
        return "<h1> NO Users</h1>"
def get_next_id():
   user=list(mongo.db.Instractor2.find({}).sort({"_id":-1}))[0]._id
   if user==[]:
        print("list no empty")
        return [0]['_id']+1
   else :
        print("list empty")
        return 1
@app.route('/addusers')
def get_users():
    name=request.args.get('name')
    age=request.args.get('age')
    location=request.args.get('location')
    if name != None or age != None or location != None :
        mongo.db.Instractor2._insert_one({"_id":get_next_id(),'name':name,"age":age,"locaion":location})      
    #print(users)
    
    return "ok"







if __name__ == "__main__" :
    app.run(debug=True)