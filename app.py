import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['EXPLAIN_TEMPLATE_LOADING'] = True

@app.route('/', methods=['GET'])
def get_users():
    #print(f"URL is : {flask.url_for('static', filename='css/favicon.ico')}")
    return flask.render_template('index.html')

@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return flask.render_template(page_name)
    except:
        return flask.redirect('/')

@app.route('/about',methods=['GET'])
def about_method():
	return flask.render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
