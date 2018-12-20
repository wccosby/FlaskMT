from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {"username": "myname"}
	return "Hello, World"

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
