import weather

def test_getForecast():
     forecast = weather.getForecast("90210")
     assert forecast.find("Zeverly") > 0



