from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from David Oloye! I am adding my first code change'

@app.route("/hello")
def hello():
    return render_template('hello.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/about-css")
def about_css():
    return render_template('about-css.html')

@app.route("/greeting")
def greeting_java():
    return render_template('greeting.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print('First Name' + request.form.get('first_name'))
        print('Last Name' + request.form.get('last_name'))
        print('Email' + request.form.get('email'))
        print('Job Title' + request.form.get('job_title'))

        if request.form.get('agree_check'):
                print('Agree to be contacted: ' + request.form.get('agree_check'))

    return render_template('contact.html')

@app.route("/favorite-course")
def favorite_course():
    print('You have entered your favorite course as:', request.args.get('subject'), request.args.get('course_number'))

    return render_template('favorite-course.html')

if __name__ == '__main__':
    app.run()