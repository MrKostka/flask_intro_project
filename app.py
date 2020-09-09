from flask import Flask, render_template

app = Flask(__name__) #python vec, potrebna k vytvoreniu objektu/aplikacie


all_posts = [
    {
        'title' : 'Post 1',
        'content': 'This is the content of post 1 - ahahahahha.',
        'author' : 'Marek Kostka'
    },
    {
        'title' : 'Post 2',
        'content': 'This is the content of post 2 - ahahahahha.'
    }
]

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

@app.route('/home/users/<string:name>/posts/<int:id>')
def hello_name(name,id):
	return "Hello, " + name + " your Id is: " + str(id)

@app.route('/onlyget',methods=['GET'])
def get_req():
	return "You can only get this webpage." 

if __name__ == "__main__":
	app.run(debug=True)
