from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/staff')
def staff():
    return render_template('staff.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Handle form submission
        name = request.form['name']
        email = request.form['email']
        service = request.form['service']
        date = request.form['date']
        # Save booking information
        return render_template('booking.html', success=True)
    return render_template('booking.html')

if __name__ == '__main__':
    app.run(debug=True)
