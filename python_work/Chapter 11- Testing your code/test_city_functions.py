from city_functions import city_country
from city_functions import city_country_population

# 11-1 and 11-2 

def test_city_country():
    location = city_country('santiago','chile')
    assert location == 'Santiago, Chile'

def test_city_country_population():
    location = city_country_population('santiago','chile',5000000)
    assert location == 'Santiago, Chile - Population 5000000'