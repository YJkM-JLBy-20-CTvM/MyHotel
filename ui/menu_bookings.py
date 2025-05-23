from models.booking import Booking, get_all_bookings


def menu_bookings():
    while True:
        print("\n=== Бронирование ===")
        print("[1] Показать все брони")
        print("[2] Добавить бронь")
        print("[3] Подтвердить бронь")
        print("[0] Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            bookings = get_all_bookings()
            for b in bookings:
                print(
                      "ID:", b.id,
                      "Клиент ID:", b.client_id,
                      "Номер ID:", b.room_id,
                      "С:", b.start_date, "по", b.end_date,
                      "Подтверждена:" "Да" if b.is_confirmed else "Нет",
                      sep=", ")

        elif choice == "2":
            client_id = int(input("ID клиента: "))
            room_id = int(input("ID номера: "))
            start = input("Дата начала (ГГГГ-ММ-ДД): ")
            end = input("Дата окончания (ГГГГ-ММ-ДД): ")
            booking = Booking(client_id=client_id, room_id=room_id, start_date=start, end_date=end)
            booking.save()
            print("[✓] Бронь добавлена.")

        elif choice == "3":
            id_to_confirm = int(input("ID брони: "))
            booking = next((b for b in get_all_bookings() if b.id == id_to_confirm), None)

            if booking:
                booking.is_confirmed = True
                booking.save()
                print("[✓] Бронь подтверждена.")

            else:
                print("[⁉︎] Бронь не найдена.")

        elif choice == "0":
            break

        else:
            print("[⁉︎]~ Неверный ввод.")
