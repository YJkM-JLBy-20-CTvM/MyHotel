from models.booking import Booking, get_all_bookings_with_price


def menu_bookings():
    while True:
        print("\n=== Бронирование ===")
        print("[1] Показать все брони")
        print("[2] Добавить бронь")
        print("[3] Подтвердить бронь")
        print("[0] Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            bookings = get_all_bookings_with_price()
            for b, base_price, discount, final_price in bookings:
                print(f"""{b.id}.
Клиент ID: {b.client_id}
Номер ID: {b.room_id}
С {b.start_date} по {b.end_date}
Подтверждена: {"Да" if b.is_confirmed else "Нет"}
Базовая цена: {base_price:.2f}
Скидка: {discount:.0f}%
Итоговая цена: {final_price:.2f}
""")

        elif choice == "2":
            try:
                client_id = int(input("ID клиента: "))
                room_id = int(input("ID номера: "))
                start = input("Дата начала (ДД-ММ-ГГГГ): ")
                end = input("Дата окончания (ДД-ММ-ГГГГ): ")
                booking = Booking(client_id=client_id, room_id=room_id, start_date=start, end_date=end)
                booking.save()
                print("[✓] Бронь добавлена.")
            except Exception as e:
                print("[⁉︎] Неверный ввод.")

        elif choice == "3":
            try:
                id_to_confirm = int(input("Введите ID брони для подтверждения: "))
                bookings = get_all_bookings_with_price()
                booking = next((b for b, _, _, _ in bookings if b.id == id_to_confirm), None)
                if booking:
                    booking.is_confirmed = True
                    booking.save()
                    print("[✓] Бронь подтверждена")
                else:
                    print("[⁉︎] Бронь не найдена.")
            except Exception as e:
                print(f"[⁉︎] Неверный ввод: {e}")

        elif choice == "0":
            break

        else:
            print("[⁉︎] Неверный ввод.")
