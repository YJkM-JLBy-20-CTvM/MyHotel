from database.db_manager import initialize_db
from ui.menu import show_main_menu
from ui.menu_clients import menu_clients
from ui.menu_rooms import menu_rooms
from ui.menu_checkins import menu_checkins
from ui.menu_bookings import menu_bookings
from ui.menu_discounts import menu_discounts
from ui.menu_client_discounts import menu_client_discounts
from ui.menu_room_places import menu_room_places

def main():
    initialize_db()
    while True:
        user_choice = show_main_menu()
        if user_choice == "1":
            menu_clients()
        elif user_choice == "2":
            menu_rooms()
        elif user_choice == "3":
            menu_checkins()
        elif user_choice == "4":
            menu_bookings()
        elif user_choice == "5":
            menu_discounts()
        elif user_choice == "6":
            menu_client_discounts()
        elif user_choice == "7":
            menu_room_places()
        elif user_choice == "0":
            print("Выход из программы. До свидания!")
            break
        else:
            print("[⁉︎] Неверный ввод. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
