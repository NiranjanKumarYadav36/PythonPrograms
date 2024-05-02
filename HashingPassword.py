import hashlib

try:
    name = input("Enter your name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Write the details to the file
    with open("passkey.txt", "a") as file:
        file.write("Name: " + name + "\n")
        file.write("Username: " + username + "\n")
        file.write("Hashed Password: " + hashed_password + "\n")
    
    print("Details have been successfully written to passkey.txt.")
except Exception as e:
    print("An error occurred:", e)
