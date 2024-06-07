def build_profile(first_name, last_name, **additional_info):
    profile = {
        'first_name': first_name,
        'last_name': last_name
    }
    profile.update(additional_info)
    return profile

my_profile = build_profile('John', 'Doe', age=30, location='New York', occupation='Engineer')
print(my_profile)
