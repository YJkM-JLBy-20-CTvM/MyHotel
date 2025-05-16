from models.room_place import RoomPlace, get_places_by_room_id
from models.room import get_all_rooms

def menu_room_places():
    while True:
        print("\n=== Места в номерах ===")
        print("1. Показать места в номере")
        print("2. Добавить место в номер")
        print("3. Удалить место")
        print("0. Назад")
        choice = input("Выберите действие: ")

        if choice == "1":
            room_id = int(input("Введите ID номера: "))
            places = get_places_by_room_id(room_id)
            print(f"\nМеста в номере {room_id}:")
            for p in places:
                print(f"ID места: {p.id} | Номер места: {p.place_number}")

        elif choice == "2":
            print("\nНомера:")
            for r in get_all_rooms():
                print(f"{r.id} - {r.number}")

            room_id = int(input("Введите ID номера: "))
            place_number = int(input("Введите номер места: "))
            place = RoomPlace(room_id=room_id, place_number=place_number)
            place.save()
            print("✅ Место добавлено.")

        elif choice == "3":
            place_id = int(input("Введите ID места для удаления: "))
            place = RoomPlace(id=place_id)
            place.delete()
            print("✅ Место удалено.")

        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод.")
