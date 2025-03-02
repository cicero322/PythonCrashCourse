from users import User
# 9.12
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("\nThis user is an admin and has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege.capitalize()}")

class Admin(User):
    def __init__(self,first_name,last_name,age,country):
        super().__init__(first_name,last_name,age,country)
        self.privileges = Privileges()
    
    def show_admin_privileges(self):
        self.privileges.show_privileges()

def admin():
    localData = Admin("Isaac","Newton","86","UK")
    localData.describe_user()
    localData.greet_user()
    localData.show_admin_privileges()

admin()