import csv

FILE_NAME = "users.csv"

# Load users from CSV
def load_users():
    users = {}
    try:
        with open(FILE_NAME, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                users[row["name"]] = {
                    "password": row["password"],
                    "status": row["status"]
                }
    except FileNotFoundError:
        pass
    return users

# Save a new user to CSV
def save_user(name, password, status):
    file_exists = False
    try:
        with open(FILE_NAME, "r"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(FILE_NAME, mode="a", newline="") as file:
        fieldnames = ["name", "password", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "name": name,
            "password": password,
            "status": status
        })

# Register function
def register(users):
    name = input("Enter username: ")
    if name in users:
        print("❌ User already exists.")
        return

    password = input("Enter password: ")
    status = "1"   # 1 = Active

    users[name] = {"password": password, "status": status}
    save_user(name, password, status)

    print("✅ Registration successful.")

# Login function
def login(users):
    name = input("Enter username: ")
    password = input("Enter password: ")

    if name in users and users[name]["password"] == password:
        status = users[name]["status"]
        status_text = "Active" if status == "1" else "Inactive"
        print(f"✅ Login successful! Status: {status_text} ({status})")
    else:
        print("❌ Invalid username or password.")

# Main program
def main():
    users = load_users()

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register(users)
        elif choice == "2":
            login(users)
        elif choice == "3":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
