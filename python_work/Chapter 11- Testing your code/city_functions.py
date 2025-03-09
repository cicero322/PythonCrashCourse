#11.1 and 11.2
def city_country(city,country):
    full_loc = f"{city}, {country}"
    return full_loc.title()

def city_country_population(city,country,population=''):
    if population:
        full_loc = f"{city}, {country} - population {population}"
        return full_loc.title()
    else: 
        full_loc = f"{city}, {country}"
    return full_loc.title()