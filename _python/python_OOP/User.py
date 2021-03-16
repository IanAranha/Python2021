# declaring a class
class User:

# def __init__ is called evertime a class in initiated
# Class attributes...the same for all instances
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged_status = False


#class Methods: Things the class can do.
    def login(self):
        self.logged_status = True
        print(self.name, "in now logged in.")
        return self

    def logout(self):
        self.logged_status = False
        print(self.name, "in now logged out.")
        return self

    def show(self):
        print(f"My name is {self.name}. You can email me at {self.email}")
        return self

user1 = User("Ian", "ianorama@gmail.com")
print("User:",user1.name)
print("User email:",user1.email)
print("User Login status:", user1.logged_status)
print("Logging in...")
user1.login()
print("User Login status:", user1.logged_status)
print("Logging out")
user1.logout()
print("User Login status:", user1.logged_status)
user1.show()
