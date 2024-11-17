import random

def get_random_image():
    list = [
        "https://assets.lummi.ai/assets/Qmc3GrgE6mk5pbinaGfC1z3jwGxPiHgJz7egNpWWyJzJhC?auto=format&w=1500",
        "https://assets.lummi.ai/assets/QmWUbmYZyGQ5aF28XNxpTnD5RqCvVcTQzupzQE1JxjuFN6?auto=format&w=1500",
        "https://assets.lummi.ai/assets/QmR1cEcBycv7afSXsYxiByTZW8HyMtfVwqt487aTYTfBt2?auto=format&w=1500",
        "https://assets.lummi.ai/assets/QmPo81ShQkQKgfVSPJvymTnpqGwCdTZYfrqmqmMQMSLzbm?auto=format&w=1500",
        "https://assets.lummi.ai/assets/QmcUcrTT7eY2uF4CFQgDRRVc5b7UnxXDHti1QaCLeawq4Q?auto=format&w=1500",
        "https://assets.lummi.ai/assets/QmeU2hXe4C9kDf81Y38vRSmfL6A5gyd2XZVTAcNMwdF1qj?auto=format&w=1500",
        "https://assets.lummi.ai/assets/QmNUe8hWxH5J77JTFkqHmTdjLZbfNkLVFYG9rt51d9r12r?auto=format&w=1500",
        "https://assets.lummi.ai/assets/QmYFHqMn8HG9gFNmrwRJMEazyemynfPV2FTVL4b4JLQcD6?auto=format&w=1500",
        "https://assets.lummi.ai/assets/QmUhHbVRZzwKjsiNbuQCAesbn6aZ9YLLZykaY1usZKx2k9?auto=format&w=1500"
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

def get_random_woman_name():
    # List of random women's names
    women_names = [
        "Sophia", "Olivia", "Emma", "Ava", "Isabella", "Mia", "Amelia", 
        "Harper", "Evelyn", "Abigail", "Ella", "Scarlett", "Grace", 
        "Chloe", "Lily", "Aria", "Zoey", "Nora", "Riley", "Charlotte", 
        "Luna", "Hazel", "Layla", "Ellie", "Zoe", "Mila", "Sophie"
    ]
    
    # Get a random name from the list
    return random.choice(women_names)

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
