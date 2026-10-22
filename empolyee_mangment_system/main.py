from flask import Flask,render_template,redirect,request,url_for


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin-login', methods =['GET','POST'])
def admin_login():
    if request.method == 'POST':
        name = request.form.get('email')
        password = request.form.get('password')
        # print(name)
        # print(password)
        if name == 'bibek@12' and password == 'bibek':
            return redirect(url_for('admin_dashboard'))
        else:
            print('invalid error')
    return render_template('admin-login.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/admin')
def admin_dashboard():   
    return render_template('admin_dashboard.html')


#----------------admin_dashboard section-----------------#

@app.route('/add-empolyee', methods=['GET','POST'])
def add_empolyee():
    return render_template('add-empolyee.html')



@app.route('/show-empolyee', methods=['GET','POST'])
def show_empolyee():

    return render_template('show-empolyee.html')

@app.route('/search-empolyee', methods=['GET','POST'])
def search_empolyee():
    
    return render_template('search-empolyee.html')





if __name__ == '__main__':
    app.run(debug=True)




