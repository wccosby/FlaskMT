from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {"username": "myname"}

	## fabricating a list of posts
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in ...'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The avengers movie was so cool'
		}
	]
	# pass data to the jinja2 placeholders through the render_template function
	return render_template('index.html', title='Home', user=user, posts=posts)

### manual form of including html (non-templated)
# this version could be useful for APIs
# <html>
# 	<head>
# 		<title>Home Page - Microblog</title>
# 	</head>
# 	<body>
# 		<h1>Hello, '''+user['username']+'''!</h1>
# 	</body>
# </html>
