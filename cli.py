class Todo:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.id}. [{status}] {self.title}"

todos = []

def show_menu():
    print("\n\t=== WELCOME TO CLI TODO APP ===")
    print("\n== TODO MENU ==\n")
    print("\t1. View Todos")
    print("\t2. Add Todo")
    print("\t3. Mark Complete/Incomplete")
    print("\t4. Delete Todo")
    print("\t5. Quit")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option: \n")

        if choice == "1":
            if len(todos) == 0:
                print("No todos yet.")
            else:
                for todo in todos:
                    print(todo)

        elif choice == "2":
            title = input("Enter todo title: ")
            new_id = 1 if len(todos) == 0 else todos[-1].id + 1
            todos.append(Todo(new_id, title))
            print("Todo added!")

        elif choice == "3":
            id_to_toggle = int(input("Enter ID to toggle complete: "))
            found = False
            for todo in todos:
                if todo.id == id_to_toggle:
                    todo.completed = not todo.completed
                    found = True
                    print("Status updated!")
            if not found:
                print("Todo not found.")

        elif choice == "4":
            id_to_delete = int(input("Enter ID to delete: "))
            found = False
            for i in range(len(todos)):
                if todos[i].id == id_to_delete:
                    del todos[i]
                    found = True
                    print("Todo deleted!")
                    break
            if not found:
                print("Todo not found.")


            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()
