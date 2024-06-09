import folium
def map_restaurant(restaurants):
    restaurant_name = input("Wpisz nazwę resturacji: ")
    for restaurant in restaurants:
        if restaurant['name'] == restaurant_name:
            latitude = restaurant['coordinates']['latitude']
            longitude = restaurant['coordinates']['longitude']

            map = folium.Map(location=[latitude, longitude], zoom_start=14)
            folium.Marker(location=[latitude, longitude], popup=f"{restaurant_name}").add_to(map)
            map.save(f'./{restaurant_name}.html')
            print(f"Plik HTML dla restauracji {restaurant_name} został wygenerowany.")
            return
    print(f"Restauracja {restaurant_name} nie została znaleziona.")

def full_map_restaurants(restaurants):
    map = folium.Map(location=[52.2297, 21.0122], zoom_start=10)

    for restaurant in restaurants:
        latitude = restaurant['coordinates']['latitude']
        longitude = restaurant['coordinates']['longitude']
        name = restaurant['name']

        folium.Marker(location=[latitude, longitude], popup=f"{name}").add_to(map)

    map.save('./Wszystkie restauracje.html')
    print("Plik HTML dla wszystkich restauracji został wygenerowany.")

def map_employee(restaurants):
    worker_first_name = input("Wpisz imię pracownika: ")
    worker_last_name = input("Wpisz nazwisko pracownika: ")
    map = folium.Map(location=[52.2297, 21.0122], zoom_start=11)
    for restaurant in restaurants:
        for employee in restaurant['employees']:
            if employee['first_name'] == worker_first_name and employee['last_name'] == worker_last_name:
                latitude = restaurant['coordinates']['latitude']
                longitude = restaurant['coordinates']['longitude']
                restaurant_name = restaurant['name']

                folium.Marker(location=[latitude, longitude], popup=f"{restaurant_name} {worker_first_name} {worker_last_name}").add_to(map)

                map.save(f'./{worker_first_name} {worker_last_name} {restaurant_name}.html')
                print(f"Plik HTML dla {worker_first_name} {worker_last_name} został wygenerowany.")
                return
    print(f"Pracownik restauracji nie został znaleziony.")

def full_map_restaurant_employees(restaurants):
    restaurant_name = input("Wpisz nazwę restauracji: ")
    for restaurant in restaurants:
        if restaurant['name'] == restaurant_name:
            map = folium.Map(location=[52.2297, 21.0122], zoom_start=11)
            for employee in restaurant['employees']:
                worker_first_name = employee['first_name']
                worker_last_name = employee['last_name']
                latitude = employee['coordinates']['latitude']
                longitude = employee['coordinates']['longitude']

                folium.Marker(location=[latitude, longitude], popup=f"{worker_first_name} {worker_last_name}").add_to(map)

            map.save(f'./{restaurant_name} pracownicy.html')
            print(f"Plik HTML z mapą wszystkich pracowników dla restauracji {restaurant_name} został wygenerowany.")
            return
    print("Pracownicy nie znalezieni.")

def map_customer(restaurants):
    customer_first_name = input("Wpisz imię klienta: ")
    customer_last_name = input("Wpisz nazwisko klienta: ")
    map = folium.Map(location=[52.2297, 21.0122], zoom_start=11)
    for restaurant in restaurants:
        for customer in restaurant['customers']:
            if customer['first_name'] == customer_first_name and customer['last_name'] == customer_last_name:
                latitude = customer['coordinates']['latitude']
                longitude = customer['coordinates']['longitude']
                customer_name = customer['first_name'] + " " + customer['last_name']

                folium.Marker(location=[latitude, longitude], popup=f"{customer_name}").add_to(map)

                map.save(f'./{customer_first_name} {customer_last_name}.html')
                print(f"Plik HTML dla {customer_first_name} {customer_last_name} został wygenerowany.")
                return
    print(f"Klient restauracji nie został znaleziony.")

def full_map_restaurant_customers(restaurants):
    restaurant_name = input("Wpisz nazwę restauracji: ")
    for restaurant in restaurants:
        if restaurant['name'] == restaurant_name:
            map = folium.Map(location=[restaurant['coordinates']['latitude'], restaurant['coordinates']['longitude']], zoom_start=11)
            for customer in restaurant['customers']:
                latitude = customer['coordinates']['latitude']
                longitude = customer['coordinates']['longitude']
                name = customer['first_name'] + " " + customer['last_name']

                folium.Marker(location=[latitude, longitude], popup=f"{name} {restaurant_name}").add_to(map)

            map.save(f'./{restaurant["name"]} klienci.html')
            print(f"Plik HTML dla klientów restauracji {restaurant["name"]} został wygenerowany.")
            return
    print("Klienci nie znalezieni.")

