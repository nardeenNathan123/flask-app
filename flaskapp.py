# from flask import Flask,request,render_template,redirect,url_for
# # template (HTML+forloop+if+Variables+...) ==> Template Engine(Jinja)==>pureTemplate

# app=Flask(__name__,template_folder="test") #__main__==>directly , #file ==> non Direct

# users=[{"id":1,"name":"mina","age":30,"location":"giza"},{"id":2,"name":"fatma","age":30,"location":"cairo"}]
# #{"id":1,"name":"mina","age":30,"location":"giza"},{"id":2,"name":"fatma","age":30,"location":"cairo"}
# def get_next_id():
#     if len(users)>0:
#         return users[-1]['id']+1
#     else :
#         return 1
    
# @app.route('/')
# def index():
#     return render_template('index.html')
# # http://127.0.0.1:5000/users?name=ahmed&age=30&location=Giza
# @app.route('/users')
# def get_users():
#     name=request.args.get('name')
#     age=request.args.get('age')
#     location=request.args.get('location')
#     if name != None or age != None or location != None :
#         users.append({"id":get_next_id(),"name":name,"age":age,"location":location})
        
#     #print(users)
#     if users != []:
#         return render_template('users.html',users_html=users)
#     else :
#         return "<h1> NO Users</h1>"

# @app.route('/delete/<int:id>') #UUID
# def delete_user(id):
#     if id != None and len(users) !=0 : 
#         for i in range(len(users)):
#             if users[i]['id']==id:
#                 del users[i]
#                 print("Found and Delete")
#                 break

#     return redirect('/users')

# @app.route('/update2/<int:id>')
# def update_user2(id):
#         for i in range(len(users)):
#             if users[i]['id']==id:
#                 user=users[i]
#                 return render_template('update_user.html',users_html=user)
            
            
# @app.route('/update/<int:id>')            
# def update_user(id):
#     name = request.args.get('name')
#     age = request.args.get('age')
#     location = request.args.get('location')

#     for user in users:
#         if user['id'] == id:
            
#             user['name'] = name
        
#             user['age'] = age
        
#             user['location'] = location
            

#     return redirect('/users')           




# # @app.route('/update/<int:id>', methods=['GET', 'POST'])
# # def update_user(id):
# #     user = next((u for u in users if u['id'] == id), None)
    
# #     if user:
# #         if request.method == 'POST':
# #             user['name'] = request.form['name']
# #             user['age'] = request.form['age']
# #             user['location'] = request.form['location']
# #             return redirect(url_for('get_users'))
# #         else:
# #             return render_template('update_user.html', users_html=user)
# #     else:
# #         return "User not found", 404



# if __name__ == "__main__" :
#     app.run(debug=True)

