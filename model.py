
import pandas as pd
import joblib  # If you're using a different method to load your model, adjust accordingly

# Load your trained model
model = joblib.load(r'C:\Users\JASWANTH CH\OneDrive\Desktop\@SEM 5\Mini project\project - wine quality\Project code (Web Development)\Machine Learning code\wine_quality_model.pkl')

def predict_quality(input_data):
    # Convert input data to DataFrame or the required format for your model
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)
    # Assuming binary classification, you might return 'good' or 'bad'
    return 'good' if prediction[0] == 1 else 'bad'
