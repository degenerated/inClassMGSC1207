from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

user_data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a_number = request.form['a_number']
        name = request.form['name']
        living_cost = request.form['living_cost']

        # Validate A number and Monthly Living Cost
        if a_number.lower().startswith('a') and living_cost.isdigit():
            # Get the current timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            user_data.append({
                'a_number': a_number,
                'name': name,
                'living_cost': int(living_cost),
                'timestamp': timestamp  # Include the timestamp in user_data
            })

            return redirect(url_for('index'))
        else:
            return "Invalid input. A number must start with 'A' or 'a', and Monthly Living Cost must be a number."

    return render_template('index.html', user_data=user_data)


@app.route('/summary')
def summary():
    return render_template('summary.html', user_data=user_data)

@app.route('/secure-summary')
def secure_summary():
    return render_template('secure_summary.html', user_data=user_data)

@app.route('/secure-clear')
def secure_clear():
    global user_data
    user_data = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False)
