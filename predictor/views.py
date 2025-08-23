from django.shortcuts import render
import pickle
import numpy as np
from .forms import EVForm

def predict_range(request):
    if request.method == 'POST':
        form = EVForm(request.POST)
        if form.is_valid():
            # Extract features and include number_of_passengers
            features = [
                form.cleaned_data['battery_capacity_kWh'],
                form.cleaned_data['top_speed_kmh'],
                form.cleaned_data['acceleration_0_100_s'],
                form.cleaned_data['number_of_passengers']  # Use directly as seats proxy
            ]
            try:
                with open('ev_range_model_simplified.pkl', 'rb') as f:
                    model = pickle.load(f)
                input_array = np.array([features])
                prediction = model.predict(input_array)[0]
                return render(request, 'predictor/result.html', {'prediction': round(prediction, 2)})
            except Exception as e:
                return render(request, 'predictor/form.html', {'form': form, 'error': str(e)})
    else:
        form = EVForm()
    return render(request, 'predictor/form.html', {'form': form})