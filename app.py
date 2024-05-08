from flask import Flask, request, jsonify, render_template  # Added render_template
import model  # Your custom module for handling the prediction model

app = Flask(__name__, template_folder='template')

@app.route('/')
# def hello():
#     return render_template('front.html')
def dynamic_page():
    dynamic_data = "Hello, Flask!"
    return render_template('front.html', dynamic_data=dynamic_data)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Assuming data is in the form {'alcohol': 9.5, 'sulfate': 0.65, 'ph': 3.3, 'density': 0.99}
    features = [data['alcohol'], data['sulfate'], data['ph'], data['density']]
    prediction = model.predict([features])  # Ensure your model's predict method can handle this input format
    quality = 'good' if prediction[0] == 1 else 'bad'
    return jsonify({'quality': quality})

if __name__ == '__main__':
    app.run(debug=True)
