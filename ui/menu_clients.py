from models.client import Client, get_all_clients


def menu_clients():
    while True:
        print("\n=== Клиенты ===")
        print("[1] Показать всех клиентов")
        print("[2] Добавить клиента")
        print("[3] Удалить клиента")
        print("[4] Изменить клиента")
        print("[0] Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            clients = get_all_clients()
            for c in clients:
                print(f"{c.id}. {c.surname} {c.name} {c.patronymic or ''} | Паспорт: {c.passport_details} | Адрес: {c.address} | Комментарий: {c.comment}")
        elif choice == "2":
            print("\n=== Добавление клиента ===")
            surname = input("Фамилия: ")
            name = input("Имя: ")
            patronymic = input("Отчество: ")
            passport = input("Паспортные данные: ")
            address = input("Адрес: ")
            comment = input("Комментарий: ")
            client = Client(
                surname=surname,
                name=name,
                patronymic=patronymic,
                passport_details=passport,
                address=address,
                comment=comment
            )
            client.save()
            print("[✓]Клиент добавлен.")
        elif choice == "3":
            id_to_delete = int(input("Введите ID клиента для удаления: "))
            client = Client(id=id_to_delete)
            client.delete()
            print("[✗] Клиент удалён.")
        elif choice == "4":
            id_to_edit = int(input("Введите ID клиента для редактирования: "))
            current = next((c for c in get_all_clients() if c.id == id_to_edit), None)
            if not current:
                print("[⁉︎] Клиент не найден.")
                continue
            print("Оставьте поле пустым, чтобы оставить без изменений.")
            surname = input(f"Фамилия ({current.surname}): ") or current.surname
            name = input(f"Имя ({current.name}): ") or current.name
            patronymic = input(f"Отчество ({current.patronymic or ''}): ") or current.patronymic
            passport = input(f"Паспортные данные ({current.passport_details}): ") or current.passport_details
            address = input(f"Адрес ({current.address}): ") or current.address
            comment = input(f"Комментарий ({current.comment}): ") or current.comment
            updated = Client(
                id=id_to_edit,
                surname=surname,
                name=name,
                patronymic=patronymic,
                passport_details=passport,
                address=address,
                comment=comment
            )
            updated.save()
            print("[✓] Клиент обновлён.")
        elif choice == "0":
            break
        else:
            print("[⁉︎] Неверный ввод.")
