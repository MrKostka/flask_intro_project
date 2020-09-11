from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) #python vec, potrebna k vytvoreniu objektu/aplikacie
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db' #sqlite je na teraz relativne vyhodne, lebo uklada info aj lokalne na pc, cize netreba sluzbu navyse... (y) ................ tri backslashe ///su relativna cesta od tohto priecinka, 4 su //// absolutnou cestou od priecinka
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(30), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return 'Blog Post ' + str(self.id)

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

@app.route('/posts', methods=['GET','POST'])
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
