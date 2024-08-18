from flask import Flask, render_template, request
from firebase_admin import credentials, initialize_app, db


app = Flask(__name__)


cred = credentials.Certificate("account.json")
initialize_app(cred, {
    'databaseURL': 'https://school-project-bf6af-default-rtdb.firebaseio.com/'
})


ref = db.reference('/system')

# Route for the dashboard
@app.route('/', methods=['GET', 'POST'])
def dashboard():
    data = ref.get()
    mode = 'grid' if data['mode'] == 'grid' else 'solar'

    if request.method == 'POST':
        if 'switch-to-grid' in request.form:
            ref.update({'mode': 'grid'})
        elif 'switch-to-solar' in request.form:
            ref.update({'mode': 'solar'})

    grid_data = data['grid']
    solar_data = data['solar']

    return render_template('dashboard.html', mode=mode, grid_data=grid_data, solar_data=solar_data)

if __name__ == '__main__':
    app.run(debug=True)
