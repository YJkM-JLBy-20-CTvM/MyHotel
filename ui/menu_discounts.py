from models.discount import DiscountCategory, get_all_discount_categories

def menu_discounts():
    while True:
        print("\n=== Скидки ===")
        print("1. Показать категории скидок")
        print("2. Добавить категорию скидки")
        print("3. Удалить категорию скидки")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            categories = get_all_discount_categories()
            for c in categories:
                print(f"ID: {c.id}, Название: {c.name}, Скидка: {c.discount_percent}%")
        elif choice == "2":
            name = input("Название категории: ")
            percent = float(input("Процент скидки: "))
            category = DiscountCategory(name=name, discount_percent=percent)
            category.save()
            print("✅ Категория добавлена.")
        elif choice == "3":
            id_to_delete = int(input("ID категории: "))
            category = DiscountCategory(id=id_to_delete)
            category.delete()
            print("🗑️ Категория удалена.")
        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод.")
