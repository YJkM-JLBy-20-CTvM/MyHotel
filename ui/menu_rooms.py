from models.room import Room, get_all_rooms

def menu_rooms():
    while True:
        print("\n=== Номера ===")
        print("1. Показать все номера")
        print("2. Добавить номер")
        print("3. Удалить номер")
        print("4. Изменить номер")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            rooms = get_all_rooms()
            for r in rooms:
                print(f"{r.id}. Тип: {r.type}, Вместимость: {r.capacity}, Цена: {r.price} руб.")
        elif choice == "2":
            room_type = input("Тип (люкс / полулюкс / обычный): ")
            capacity = int(input("Вместимость: "))
            price = float(input("Цена: "))
            room = Room(type=room_type, capacity=capacity, price=price)
            room.save()
            print("✅ Номер добавлен.")
        elif choice == "3":
            id_to_delete = int(input("ID номера для удаления: "))
            room = Room(id=id_to_delete)
            room.delete()
            print("🗑️ Номер удалён.")
        elif choice == "4":
            id_to_edit = int(input("ID номера для редактирования: "))
            current = next((r for r in get_all_rooms() if r.id == id_to_edit), None)
            if not current:
                print("❌ Номер не найден.")
                continue
            room_type = input(f"Тип ({current.type}): ") or current.type
            capacity = input(f"Вместимость ({current.capacity}): ") or current.capacity
            price = input(f"Цена ({current.price}): ") or current.price
            updated = Room(id=id_to_edit, type=room_type, capacity=int(capacity), price=float(price))
            updated.save()
            print("✅ Номер обновлён.")
        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод.")