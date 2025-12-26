from task_tracker import TaskTracker

def main () -> None:
    tracker = TaskTracker()

    while True:
        print("\n1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Поменять статус задачи")
        print("4. Поиск задач")
        print("5. Задачи по категории")
        print("0. Выход. Сохранения и формирование json")
        
        choice = input("\nВыберите действие: ").strip()
        match choice:
            case '1':
                print("\nЗадачи:")
                tracker.display_tasks()

            case '2':
                print("\nДобавление новой задачи")
                description = input("Описание задачи: ").strip()
                category = input("Категория: ").strip()
                
                if description and category:
                    tracker.add_task(description, category)
                    print("Задача успешно добавлена!")
                else:
                    print("Ошибка: описание и категория не могут быть пустыми")

            case '3':
                print("\nИзменение статуса задачи")
                tracker.display_tasks()
                if tracker.tasks:
                    try:
                        task_num = int(input("Номер задачи для изменения статуса: ")) - 1
                        if tracker.mark_task(task_num):
                            print("Статус задачи изменен!")
                        else:
                            print("Ошибка: неверный номер задачи")
                    except ValueError:
                        print("Ошибка: введите корректный номер")
                else:
                    print("Нет задач для изменения.")

            case '4':
                print("\nПоиск задач")
                search_term = input("Введите текст для поиска: ").strip()
                if search_term:
                    results = tracker.search_tasks(search_term)
                    print(f"\nРезультаты поиска ('{search_term}'):")
                    tracker.display_tasks(results)
                else:
                    print("Ошибка: введите текст для поиска")

            case '5':
                print("\nЗадачи по категориям")
                category = input("Введите категорию (без #): ").strip()
                if category:
                    results = tracker.get_tasks_by_category(category)
                    print(f"\nЗадачи в категории '{category}':")
                    tracker.display_tasks(results)
                else:
                    print("Ошибка: введите категорию")

            case '0':
                tracker.save_tasks()
                break

            case _:
                print("Ошибка: неверный выбор")

if __name__ == "__main__":
    main()