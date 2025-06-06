from models.room import Room, get_all_rooms


def menu_rooms():
    while True:
        print("\n=== Номера ===")
        print("[1] Показать все номера")
        print("[2] Добавить номер")
        print("[3] Удалить номер")
        print("[4] Изменить номер")
        print("[0] Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            rooms = get_all_rooms()
            for r in rooms:
                print(f"""{r.id}. 
Номер комнаты: {r.place}
Тип: {r.type}
Вместимость: {r.capacity}
Цена: {r.price} руб.
""")

        elif choice == "2":
            try:
                room_place = input("Номер комнаты: ")
                room_type = input("Тип (люкс / полулюкс / обычный): ")
                capacity = int(input("Вместимость: "))
                price = float(input("Цена: "))
                room = Room(place=room_place, type=room_type, capacity=capacity, price=price)
                room.save()
                print("[✓] Номер добавлен.")
            except ValueError:
                print("[⁉︎] Неверный ввод")

        elif choice == "3":
            try:
                id_to_delete = int(input("ID номера для удаления: "))
                room = Room(id=id_to_delete)
                room.delete()
                print("[✗] Номер удалён.")
            except ValueError:
                print("[⁉︎] Неверный ввод")

        elif choice == "4":
            try:
                id_to_edit = int(input("ID номера для редактирования: "))
                current = next((r for r in get_all_rooms() if r.id == id_to_edit), None)
                if not current:
                    print("[⁉︎] Номер не найден.")
                    continue
                room_place = input(f"Номер комнаты ({current.place}): ") or current.place
                room_type = input(f"Тип ({current.type}): ") or current.type
                capacity = input(f"Вместимость ({current.capacity}): ") or current.capacity
                price = input(f"Цена ({current.price}): ") or current.price
                updated = Room(
                    id=id_to_edit,
                    place=room_place,
                    type=room_type,
                    capacity=int(capacity),
                    price=float(price)
                )
                updated.save()
                print("[✓] Номер обновлён.")
            except ValueError:
                print("[⁉︎] Неверный ввод")

        elif choice == "0":
            break

        else:
            print("[⁉︎] Неверный ввод")
