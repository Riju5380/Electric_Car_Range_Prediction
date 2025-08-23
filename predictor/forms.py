from django import forms

class EVForm(forms.Form):
    battery_capacity_kWh = forms.FloatField(label='Battery Capacity (kWh)', min_value=0)
    top_speed_kmh = forms.FloatField(label='Top Speed (km/h)', min_value=0)
    acceleration_0_100_s = forms.FloatField(label='Acceleration 0-100 (s)', min_value=0)
    number_of_passengers = forms.IntegerField(label='Number of Passengers', min_value=1, max_value=7)