from flask import Flask, render_template, request 

app_version = '1.1.0'

app = Flask(__name__)# instantiation application

@app.route("/") # association d’une route (URL) avec la fonction ‘home()’
def home():
    return render_template("index.html") 

@app.route('/about')
def about_func():
     return render_template("about.html")

@app.route('/form')
def form_func():
     return render_template("form.html")


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        print(json_result)
        return render_template("result.html", result=result, app_version=app_version)


# @app.route('/hello/')
# def hello():
#     return 'Hello, World'

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'
    
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'



app.run()# démarrage de l’application
