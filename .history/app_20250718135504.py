from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Static data: company → models
car_data = {
    'maruti': ['Swift', 'Baleno', 'WagonR'],
    'hyundai': ['i10', 'i20', 'Creta'],
    'honda': ['City', 'Amaze', 'Jazz']
}

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/get_models')
def get_models():
    company = request.args.get('company')
    models = car_data.get(company, [])
    return jsonify({'models': models})

if __name__ == '__main__':
    app.run(debug=True)