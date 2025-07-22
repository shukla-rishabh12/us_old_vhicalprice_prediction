from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample car data
car_data = {
    'maruti': ['Swift', 'Baleno', 'WagonR'],
    'hyundai': ['i10', 'i20', 'Creta'],
    'honda': ['City', 'Amaze', 'Jazz']
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_models')
def get_models():
    company = request.args.get('company', '').lower()
    models = car_data.get(company, [])
    return jsonify({'models': models})

if __name__ == '__main__':
    app.run(debug=True)
