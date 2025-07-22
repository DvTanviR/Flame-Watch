from django.shortcuts import render, redirect
import os
import requests
import pandas as pd
import joblib
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import messages
from .forms import SubscriberForm


# Create your views here.

def home(request):
    return render(request, 'index.html')

def main(request):
    # Get the current URL for sharing
    current_url = request.build_absolute_uri()
    
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully subscribed!')
            return redirect('main')
    else:
        form = SubscriberForm()
    
    return render(request, 'main.html', {
        'object_or_url': current_url,
        'form': form,
    })


def about(request):
    return render(request, 'about.html')


class WildfirePredictionAPI(APIView):

    def post(self, request):
        print("Received request data:", request.data)
        try:
            lat = float(request.data.get('lat'))
            lon = float(request.data.get('lon'))
        except (TypeError, ValueError):
            return Response({'error': 'Invalid latitude or longitude'}, status=400)

        date = datetime.now().strftime("%Y%m%d")

        # Fetch data from NASA
        nasa_data = self.fetch_nasa_power_data(lat, lon, date)
        if not nasa_data:
            return Response({'error': 'Failed to fetch NASA data'}, status=500)

        test_data = self.preprocess_data(lat, lon, date, nasa_data)

        # Load and predict
        try:
            model_path = os.path.join(settings.BASE_DIR, 'App', 'best_model.pkl')
            model = joblib.load(model_path)
            prediction_prob = model.predict_proba(test_data)[:, 1][0]
            return Response({'wildfire_probability': round(prediction_prob * 100, 2)})
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def fetch_nasa_power_data(self, lat, lon, date):
        url = (
            f"https://power.larc.nasa.gov/api/temporal/daily/point?"
            f"parameters=T2M,TOA_SW_DNI,TOA_SW_DWN,PS,GWETROOT,QV10M,"
            f"T2M_MAX,T2M_MIN,QV2M,SNODP,WS10M_MIN,WS10M_MAX,GWETPROF,Z0M,"
            f"PW,PRECTOT,RH2M&community=RE&longitude={lon}&latitude={lat}&start={date}&end={date}&format=JSON"
        )
        try:
            response = requests.get(url)
            return response.json()['properties']['parameter']
        except:
            return None

    def preprocess_data(self, lat, lon, date, data):
        processed_data = {}
        for param, value in data.items():
            processed_data[param] = [v if v != -999 else 0 for v in value.values()]

        df = pd.DataFrame(processed_data)
        df['latitude'] = lat
        df['longitude'] = lon
        df['date'] = date

        column_order = [
            'latitude', 'longitude', 'date', 'T2M', 'T2M_MAX', 'T2M_MIN', 'RH2M', 'PW', 'PS', 'TOA_SW_DNI', 
            'GWETROOT', 'QV10M', 'TOA_SW_DWN', 'QV2M', 'WS10M', 'WS10M_MAX', 'Z0M', 'GWETPROF', 
            'WS10M_MIN', 'SNODP', 'PRECTOTCORR'
        ]
        df = df.reindex(columns=column_order, fill_value=0)
        return df