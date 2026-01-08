tasks = []

while True:
    print("\n1. Vazifa qo‘shish")
    print("2. Vazifalarni ko‘rish")
    print("3. Chiqish")

    choice = input("Tanlang: ")

    if choice == "1":
        task = input("Vazifa kiriting: ")
        tasks.append(task)
        print("Vazifa qo‘shildi!")
    elif choice == "2":
        print("\nVazifalar:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        break
    else:
        print("Noto‘g‘ri tanlov!")
