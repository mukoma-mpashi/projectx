from flask import Flask, render_template, request, jsonify
from firebase_admin import credentials, initialize_app, db

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("account.json")
initialize_app(cred, {
    'databaseURL': 'https://school-project-bf6af-default-rtdb.firebaseio.com/'
})

# Firebase database reference
ref = db.reference('/system')

# Route for the dashboard
@app.route('/', methods=['GET','POST'])
def dashboard():
    data = ref.get()
    mode = 'grid' if data['mode'] == 'grid' else 'solar'
    grid_data = data['grid']
    solar_data = data['solar']
    return render_template('dashboard.html', mode=mode, grid_data=grid_data, solar_data=solar_data)

# Route to handle mode switching
@app.route('/switch_mode', methods=['POST'])
def switch_mode():
    mode = request.json.get('mode')
    if mode in ['grid', 'solar']:
        ref.update({'mode': mode})
        return jsonify({'status': 'success', 'mode': mode})
    return jsonify({'status': 'error', 'message': 'Invalid mode'}), 400

# Route to fetch the latest data (for real-time updates)
@app.route('/get_data', methods=['GET'])
def get_data():
    data = ref.get()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
