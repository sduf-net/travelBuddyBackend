import random

def get_random_image():
    list = [
        "https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/1029599/pexels-photo-1029599.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/259588/pexels-photo-259588.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/280229/pexels-photo-280229.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/1438832/pexels-photo-1438832.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/280222/pexels-photo-280222.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/2581922/pexels-photo-2581922.jpeg?auto=compress&cs=tinysrgb&w=800",
        'https://images.pexels.com/photos/2079234/pexels-photo-2079234.jpeg?auto=compress&cs=tinysrgb&w=800',
        "https://images.pexels.com/photos/221540/pexels-photo-221540.jpeg?auto=compress&cs=tinysrgb&w=800"
    ]

    return random.choice(list)

def get_random_occupation():
    occupations = [
        "Software Engineer", "Doctor", "Teacher", "Artist", "Chef", 
        "Scientist", "Nurse", "Architect", "Lawyer", "Musician", 
        "Engineer", "Writer", "Photographer", "Web Developer", "Graphic Designer", 
        "Entrepreneur", "Researcher", "Manager", "Electrician", "Plumber"
    ]
    
    return random.choice(occupations)

def get_random_university_name():
    universities = [
        "Harvard University", "Stanford University", "University of Oxford", 
        "University of Cambridge", "Massachusetts Institute of Technology (MIT)", 
        "University of California, Berkeley", "Yale University", "Princeton University", 
        "University of Chicago", "Columbia University", "California Institute of Technology (Caltech)", 
        "University of Tokyo", "University of Toronto", "ETH Zurich", "Imperial College London",
        "Peking University", "University of Melbourne", "National University of Singapore", 
        "University of Edinburgh", "Australian National University"
    ]
    return random.choice(universities)

def get_random_city_name():
    city_names = [
        "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
        "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
        "Austin", "Jacksonville", "San Francisco", "Columbus", "Indianapolis",
        "Seattle", "Denver", "Washington", "Boston", "El Paso", 
        "Detroit", "Nashville", "Portland", "Memphis", "Oklahoma City"
    ]
    
    return random.choice(city_names)

def get_random_country_code():
    # List of random country codes
    country_codes = [
        "CA", "UK", "USA", "CO", "FR", "DE", "IN", "IT", "AU", "BR", 
        "JP", "CN", "MX", "ES", "RU", "KR", "ZA", "NG", "PL", "SE"
    ]
    
    # Get a random country code from the list
    return random.choice(country_codes)

def generate_label_widgets():
    num_widgets=random.randint(1, 6)
    countries = ["Canada", "United Kingdom", "United States", "Colombia", "France", 
             "Germany", "India", "Italy", "Australia", "Brazil", "Japan", "China", 
             "Mexico", "Spain", "Russia", "South Korea", "South Africa", "Nigeria", 
             "Poland", "Sweden", "Argentina"]

    label_widgets = []
    
    for _ in range(num_widgets):
        random_country = random.choice(countries)  # Select a random country name
        
        # Create a label_widget dictionary with the random country name
        label_widget = {
            "data": {
                "actions": {
                    "click": {
                        "screen_name": "home",
                        "type": "route_to_local"
                    },
                    "long_press": {
                        "params": {
                            "parameter": "parameter"
                        },
                        "type": "async_post",
                        "url": "url"
                    }
                },
                "text": random_country  # Assign the random country name to the text field
            },
            "id": f"{random.randint(1000000000, 9999999999)}",  # Generate a random ID
            "name": "Label3Widget"  # Generate a unique widget name
        }
        
        # Add the label widget to the list
        label_widgets.append(label_widget)
    
    return label_widgets

def get_random_boolean() -> bool:
    """
    Returns a random boolean value (True or False).
    """
    return random.choice([True, False])