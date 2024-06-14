# RESTAURANT
def display_restaurant(restaurants):
    for restaurant in restaurants:
        print("Restauracja:", restaurant['name'])
        print("Adres:", restaurant['address'])
        print("Telefon:", restaurant['phone'])
        print("Pracownicy:")
        for employee in restaurant['employees']:
            print("- {} {}".format(employee['first_name'], employee['last_name']))
        print("Klienci:")
        for customer in restaurant['customers']:
            print("- {} {}".format(customer['first_name'], customer['last_name']))
        print()


def add_restaurant(restaurants):
    name = input("Podaj nazwę restauracji: ")
    address = input("Podaj adres restauracji: ")
    phone = input("Podaj numer telefonu restauracji: ")
    latitude = float(input("Podaj szerokość geograficzną restauracji: "))
    longitude = float(input("Podaj długość geograficzną restauracji: "))
    coordinates = {"latitude": latitude, "longitude": longitude}
    employees = []
    while True:
        first_name = input("Podaj imię pracownika (lub 'q' aby zakończyć): ")
        if first_name.lower() == 'q':
            break
        last_name = input("Podaj nazwisko pracownika: ")
        employees.append({"first_name": first_name, "last_name": last_name, "coordinates": coordinates})
    customers = []
    while True:
        first_name = input("Podaj imię klienta (lub 'q' aby zakończyć): ")
        if first_name.lower() == 'q':
            break
        last_name = input("Podaj nazwisko klienta: ")
        order_number = input("Podaj numer zamówienia klienta: ")
        customer_latitude = float(input("Podaj szerokość geograficzną klienta: "))
        customer_longitude = float(input("Podaj długość geograficzną klienta: "))
        customer_coordinates = {"latitude": customer_latitude, "longitude": customer_longitude}
        customers.append({"first_name": first_name, "last_name": last_name, "order_number": order_number,
                          "coordinates": customer_coordinates})
    restaurant = {
        "name": name,
        "address": address,
        "phone": phone,
        "coordinates": coordinates,
        "employees": employees,
        "customers": customers
    }
    restaurants.append(restaurant)


def remove_restaurant(restaurants):
    name = input("Podaj nazwę restauracji, którą chcesz usunąć: ")
    for restaurant in restaurants:
        if restaurant['name'] == name:
            restaurants.remove(restaurant)
            print("Restauracja została usunięta z listy.")
            return
    print("Restauracja o podanej nazwie nie została znaleziona w liście.")


def edit_restaurant(restaurants):
    name = input("Podaj nazwę restauracji, którą chcesz edytować: ")
    for restaurant in restaurants:
        if restaurant['name'] == name:
            print("Edycja danych restauracji:")
            restaurant['name'] = input("Podaj nową nazwę restauracji (lub pozostaw puste, aby nie zmieniać): ") or \
                                 restaurant['name']
            restaurant['address'] = input("Podaj nowy adres restauracji (lub pozostaw puste, aby nie zmieniać): ") or \
                                    restaurant['address']
            restaurant['phone'] = input(
                "Podaj nowy numer telefonu restauracji (lub pozostaw puste, aby nie zmieniać): ") or restaurant['phone']
            latitude = input("Podaj nową szerokość geograficzną restauracji (lub pozostaw puste, aby nie zmieniać): ")
            if latitude:
                restaurant['coordinates']['latitude'] = float(latitude)
            longitude = input("Podaj nową długość geograficzną restauracji (lub pozostaw puste, aby nie zmieniać): ")
            if longitude:
                restaurant['coordinates']['longitude'] = float(longitude)
            print("Edycja danych pracowników:")
            for employee in restaurant['employees']:
                employee['first_name'] = input(
                    f"Podaj nowe imię pracownika {employee['first_name']} (lub pozostaw puste, aby nie zmieniać): ") or \
                                         employee['first_name']
                employee['last_name'] = input(
                    f"Podaj nowe nazwisko pracownika {employee['last_name']} (lub pozostaw puste, aby nie zmieniać): ") or \
                                        employee['last_name']
            print("Edycja danych klientów:")
            for customer in restaurant['customers']:
                customer['first_name'] = input(
                    f"Podaj nowe imię klienta {customer['first_name']} (lub pozostaw puste, aby nie zmieniać): ") or \
                                         customer['first_name']
                customer['last_name'] = input(
                    f"Podaj nowe nazwisko klienta {customer['last_name']} (lub pozostaw puste, aby nie zmieniać): ") or \
                                        customer['last_name']
                customer['order_number'] = input(
                    f"Podaj nowy numer zamówienia klienta {customer['order_number']} (lub pozostaw puste, aby nie zmieniać): ") or \
                                           customer['order_number']
                customer_latitude = input(
                    f"Podaj nową szerokość geograficzną klienta {customer['first_name']} (lub pozostaw puste, aby nie zmieniać): ")
                if customer_latitude:
                    customer['coordinates']['latitude'] = float(customer_latitude)
                customer_longitude = input(
                    f"Podaj nową długość geograficzną klienta {customer['first_name']} (lub pozostaw puste, aby nie zmieniać): ")
                if customer_longitude:
                    customer['coordinates']['longitude'] = float(customer_longitude)
            print("Dane restauracji zostały zaktualizowane.")
            return
    print("Restauracja o podanej nazwie nie została znaleziona w liście.")


# EMPLOYEES
def display_employee(restaurants):
    for restaurant in restaurants:
        print("Restauracja:", restaurant['name'])
        print("Adres:", restaurant['address'])
        print("Lista pracowników:")
        for employee in restaurant['employees']:
            print(f"{employee['first_name']} {employee['last_name']}")
        print("")


def add_employee(restaurants):
    restaurant_name = input("Podaj nazwę restauracji, do której chcesz dodać pracowników: ")
    for restaurant in restaurants:
        if restaurant['name'] == restaurant_name:
            while True:
                first_name = input("Podaj imię nowego pracownika (lub 'q' aby zakończyć dodawanie): ")
                if first_name.lower() == 'q':
                    break
                last_name = input("Podaj nazwisko nowego pracownika: ")
                restaurant['employees'].append({'first_name': first_name, 'last_name': last_name})
                print("Pracownik dodany pomyślnie!")
            return
    print("Restauracja o podanej nazwie nie została znaleziona w liście.")


def remove_employee(restaurants):
    restaurant_name = input("Podaj nazwę restauracji, z której chcesz usunąć pracownika/pracowników: ")
    for restaurant in restaurants:
        if restaurant['name'] == restaurant_name:
            print("Lista pracowników w restauracji", restaurant_name, ":")
            for employee in restaurant['employees']:
                print(f"{employee['first_name']} {employee['last_name']}")
            while True:
                delete_choice = input(
                    "Podaj imię i nazwisko pracownika, którego chcesz usunąć (lub 'q' aby zakończyć usuwanie): ")
                if delete_choice.lower() == 'q':
                    break
                for employee in restaurant['employees']:
                    if f"{employee['first_name']} {employee['last_name']}".lower() == delete_choice.lower():
                        restaurant['employees'].remove(employee)
                        print("Pracownik usunięty pomyślnie!")
                        break
                else:
                    print("Pracownik o podanym imieniu i nazwisku nie został znaleziony.")
            return
    print("Restauracja o podanej nazwie nie została znaleziona w liście.")


def edit_employee(restaurants):
    restaurant_name = input("Podaj nazwę restauracji, w której chcesz edytować listę pracowników: ")
    for restaurant in restaurants:
        if restaurant['name'] == restaurant_name:
            print("Lista pracowników w restauracji", restaurant_name, ":")
            for employee in restaurant['employees']:
                print(f"{employee['first_name']} {employee['last_name']}")
            while True:
                edit_choice = input(
                    "Podaj imię i nazwisko pracownika, którego chcesz edytować (lub 'q' aby zakończyć edycję): ")
                if edit_choice.lower() == 'q':
                    break
                for employee in restaurant['employees']:
                    if f"{employee['first_name']} {employee['last_name']}".lower() == edit_choice.lower():
                        print("Edycja pracownika", edit_choice)
                        employee['first_name'] = input("Podaj nowe imię: ")
                        employee['last_name'] = input("Podaj nowe nazwisko: ")
                        print("Pracownik zedytowany pomyślnie!")
                        break
                else:
                    print("Pracownik o podanym imieniu i nazwisku nie został znaleziony.")
            return
    print("Restauracja o podanej nazwie nie została znaleziona w liście.")


# CUSTOMER
def display_customer(restaurants):
    restaurant_name = input("Podaj nazwę restauracji, której chcesz wyświetlić listę klientów: ")
    for restaurant in restaurants:
        if restaurant['name'] == restaurant_name:
            print("Lista klientów w restauracji", restaurant_name, ":")
            for customer in restaurant['customers']:
                print(f"{customer['first_name']} {customer['last_name']} nr zamówienia: {customer['order_number']}")
            return
    print("Restauracja o podanej nazwie nie została znaleziona w liście.")


def add_customer(restaurants):
    restaurant_name = input("Podaj nazwę restauracji, do której chcesz dodać klienta/klientów: ")
    for restaurant in restaurants:
        if restaurant['name'] == restaurant_name:
            while True:
                first_name = input("Podaj imię nowego klienta (lub 'q' aby zakończyć dodawanie): ")
                if first_name.lower() == 'q':
                    break
                last_name = input("Podaj nazwisko nowego klienta: ")
                order_number = input("Podaj numer zamówienia nowego klienta: ")
                latitude = float(input("Podaj szerokość geograficzną nowego klienta: "))
                longitude = float(input("Podaj długość geograficzną nowego klienta: "))
                restaurant['customers'].append(
                    {'first_name': first_name, 'last_name': last_name, 'order_number': order_number,
                     'coordinates': {'latitude': latitude, 'longitude': longitude}})
                print("Klient dodany pomyślnie!")
            return
    print("Restauracja o podanej nazwie nie została znaleziona w liście.")


def remove_customer(restaurants):
    restaurant_name = input("Podaj nazwę restauracji, z której chcesz usunąć klienta/klientów: ")
    for restaurant in restaurants:
        if restaurant['name'] == restaurant_name:
            print("Lista klientów w restauracji", restaurant_name, ":")
            for client in restaurant['customers']:
                print(f"{client['first_name']} {client['last_name']}")
            while True:
                delete_choice = input(
                    "Podaj imię i nazwisko klienta, którego chcesz usunąć (lub 'q' aby zakończyć usuwanie): ")
                if delete_choice.lower() == 'q':
                    break
                for client in restaurant['customers']:
                    if f"{client['first_name']} {client['last_name']}".lower() == delete_choice.lower():
                        restaurant['customers'].remove(client)
                        print("Klient usunięty pomyślnie!")
                        break
                else:
                    print("Klient o podanym imieniu i nazwisku nie został znaleziony.")
            return
    print("Restauracja o podanej nazwie nie została znaleziona w liście.")


def edit_customer(restaurants):
    restaurant_name = input("Podaj nazwę restauracji, w której chcesz edytować klienta: ")
    for restaurant in restaurants:
        if restaurant['name'] == restaurant_name:
            print("Lista klientów w restauracji", restaurant_name, ":")
            for client in restaurant['customers']:
                print(f"{client['first_name']} {client['last_name']}")
            while True:
                edit_choice = input(
                    "Podaj imię i nazwisko klienta, którego chcesz edytować (lub 'q' aby zakończyć edycję): ")
                if edit_choice.lower() == 'q':
                    break
                for client in restaurant['customers']:
                    if f"{client['first_name']} {client['last_name']}".lower() == edit_choice.lower():
                        print("Edycja klienta", edit_choice)
                        client['first_name'] = input("Podaj nowe imię: ")
                        client['last_name'] = input("Podaj nowe nazwisko: ")
                        client['order_number'] = input("Podaj nowy numer zamówienia: ")
                        client['coordinates']['latitude'] = float(input("Podaj nową szerokość geograficzną: "))
                        client['coordinates']['longitude'] = float(input("Podaj nową długość geograficzną: "))
                        print("Klient zedytowany pomyślnie!")
                        break
                else:
                    print("Klient o podanym imieniu i nazwisku nie został znaleziony.")
            return
    print("Restauracja o podanej nazwie nie została znaleziona w liście.")

