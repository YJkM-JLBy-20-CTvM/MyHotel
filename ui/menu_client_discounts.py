from models.client_discount import ClientDiscount, get_discounts_by_client_id
from models.client import get_all_clients
from models.discount import get_all_discount_categories


def menu_client_discounts():
    while True:
        print("\n=== Скидки клиентов ===")
        print("[1] Показать скидки клиента")
        print("[2] Добавить скидку клиенту")
        print("[3] Удалить скидку клиента")
        print("[0] Назад")
        choice = input("Выберите действие: ")

        if choice == "1":
            client_id = int(input("Введите ID клиента: "))
            discounts = get_discounts_by_client_id(client_id)
            print(f"\nСкидки клиента {client_id}:")
            for d in discounts:
                print(f"ID привязки: {d.id} | Категория скидки ID: {d.discount_category_id}")

        elif choice == "2":
            print("\nКлиенты:")
            for c in get_all_clients():
                print(f"{c.id} - {c.surname} {c.name}")

            client_id = int(input("Введите ID клиента: "))

            print("\nКатегории скидок:")
            for d in get_all_discount_categories():
                print(f"{d.id} - {d.name}")

            discount_category_id = int(input("Введите ID категории скидки: "))

            rel = ClientDiscount(client_id=client_id, discount_category_id=discount_category_id)
            rel.save()
            print("[✓] Скидка добавлена клиенту.")

        elif choice == "3":
            rel_id = int(input("Введите ID привязки скидки для удаления: "))
            rel = ClientDiscount(id=rel_id)
            rel.delete()
            print("[✗] Привязка скидки удалена.")

        elif choice == "0":
            break
        else:
            print("[⁉︎] Неверный ввод.")
