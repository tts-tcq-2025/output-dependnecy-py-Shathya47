
 
def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }
 
def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"
 
    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather
 
def rainy_check():
    return {
        'temperatureInC': 20,
        'precipitation': 90,  
        'humidity': 80,
        'windSpeedKMPH': 10
    }
 
def storm_check():
    return {
        'temperatureInC': 30,
        'precipitation': 10,
        'humidity': 40,
        'windSpeedKMPH': 70  
    }
 
def cloudy_check():
    return {
        'temperatureInC': 30,
        'precipitation': 40,  
        'humidity': 50,
        'windSpeedKMPH': 20
    }
 
def test_rainy_condition():
    weather = report(rainy_check)
    assert "rain" in weather.lower()
 
def test_storm_condition():
    weather = report(storm_check)
    assert "storm" in weather.lower()
 
def test_cloudy_condition():
    weather = report(cloudy_check)
    assert "cloudy" in weather.lower()
 
if __name__ == '__main__':
    test_rainy_condition()
    test_storm_condition()
    test_cloudy_condition()
    print("All is well...")
