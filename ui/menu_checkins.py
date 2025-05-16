from models.checkin import Checkin, get_all_checkins

def menu_checkins():
    while True:
        print("\n=== Заселения ===")
        print("1. Показать все записи о заселении")
        print("2. Добавить заселение")
        print("3. Установить дату выезда")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            checkins = get_all_checkins()
            for c in checkins:
                print(f"ID: {c.id}, Клиент ID: {c.client_id}, Номер ID: {c.room_id}, Место ID: {c.place_id}, Заезд: {c.checkin_date}, Выезд: {c.checkout_date or 'ещё проживает'}")
        elif choice == "2":
            client_id = int(input("ID клиента: "))
            room_id = int(input("ID номера: "))
            place_id = int(input("ID места: "))
            checkin_date = input("Дата заселения (ГГГГ-ММ-ДД): ")
            checkin = Checkin(client_id=client_id, room_id=room_id, place_id=place_id, checkin_date=checkin_date)
            checkin.save()
            print("✅ Заселение добавлено.")
        elif choice == "3":
            checkin_id = int(input("ID заселения: "))
            checkout_date = input("Дата выезда (ГГГГ-ММ-ДД): ")
            checkin = next((c for c in get_all_checkins() if c.id == checkin_id), None)
            if checkin:
                checkin.checkout_date = checkout_date
                checkin.save()
                print("✅ Дата выезда обновлена.")
            else:
                print("❌ Заселение не найдено.")
        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод.")