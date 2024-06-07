def get_formatted_city_country(city, country, population=None):
    if population:
        formatted_string = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_string = f"{city.title()}, {country.title()}"
    return formatted_string
