from models.data_source import restaurants, users
from utils.emap import (
    map_restaurant, full_map_restaurants,
    map_employee, full_map_restaurant_employees,
    map_customer, full_map_restaurant_customers)
from utils.crud import (
    display_restaurant, display_employee, display_customer,
    add_restaurant, add_employee, add_customer,
    remove_restaurant, remove_employee, remove_customer,
    edit_restaurant, edit_employee, edit_customer)

if __name__ == '__main__':
    def logged_user():
        while True:
            print("Witaj w Hungry Coders :)")
            username = input("Podaj nazwę użytkownika: ")
            password = input("Podaj hasło: ")

            for user in users:
                if user["login"] == username and user["password"] == password:
                    print("Zalogowano pomyślnie :)")
                    return username

            print("Nieprawidłowa nazwa użytkownika lub hasło. Spróbuj ponownie.")

    def restaurant_options(restaurants):
        while True:
            print("Opcje dla restauracji:")
            print("1. Wyświetl listę restauracji")
            print("2. Dodaj restaurację")
            print("3. Usuń restaurację")
            print("4. Edytuj dane restauracji")
            print("5. Wygeneruj mape dla wybranej restauracji")
            print("6. Wygeneruj mape dla restauracji")
            print("7. Powrót do menu głównego")

            choice = input("Wybierz opcję: ")

            if choice == "1":
                display_restaurant(restaurants)
            elif choice == "2":
                add_restaurant(restaurants)
            elif choice == "3":
                remove_restaurant(restaurants)
            elif choice == "4":
                edit_restaurant(restaurants)
            elif choice == "5":
                display_employee(restaurants)
                map_restaurant(restaurants)
            elif choice == "6":
                full_map_restaurants(restaurants)
            elif choice == "7":
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")

    def employee_options(restaurants):
        while True:
            print("Opcje dla pracowników:")
            print("1. Wyświetl listę pracowników")
            print("2. Dodaj pracownika")
            print("3. Usuń pracownika")
            print("4. Edytuj dane pracownika")
            print("5. Wygeneruj mape dla wybranego pracownika")
            print("6. Wygeneruj mape pracowników danej restauracji")
            print("7. Powrót do menu pracownika")

            choice = input("Wybierz opcję: ")

            if choice == "1":
                display_employee(restaurants)
            elif choice == "2":
                add_employee(restaurants)
            elif choice == "3":
                remove_employee(restaurants)
            elif choice == "4":
                edit_employee(restaurants)
            elif choice == "5":
                map_employee(restaurants)
            elif choice == "6":
                full_map_restaurant_employees(restaurants)
            elif choice == "7":
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")

    def customer_options(restaurants):
        while True:
            print("Opcje dla klientów:")
            print("1. Wyświetl listę klientów")
            print("2. Dodaj klienta")
            print("3. Usuń klienta")
            print("4. Edytuj dane klienta")
            print("5. Wygeneruj mape dla wybranego klienta")
            print("6. Wygeneruj mape klientów danej restauracji")
            print("7. Powrót do menu głównego")

            choice = input("Wybierz opcję: ")

            if choice == "1":
                display_customer(restaurants)
            elif choice == "2":
                add_customer(restaurants)
            elif choice == "3":
                remove_customer(restaurants)
            elif choice == "4":
                edit_customer(restaurants)
            elif choice == "5":
                map_customer(restaurants)
            elif choice == "6":
                full_map_restaurant_customers(restaurants)
            elif choice == "7":
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")
if logged_user():
    while True:
        print("Witaj w programie do zarządzania resturacjami, pracownikami, klientami :)")
        print("1. Restauracje")
        print("2. Pracownicy")
        print("3. Klienci")
        print("4. Koniec")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            restaurant_options(restaurants)
        elif choice == "2":
            employee_options(restaurants)
        elif choice == "3":
            customer_options(restaurants)
        elif choice == "4":
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")

