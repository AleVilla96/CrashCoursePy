# 9.7/9.8
from users import User


class Admin(User):
    """
    Here, the privileges instantiate as an attribute of the Admin class.
    But Privileges is a class by its own, independent.
    """
    def __init__(self, first_name, last_name, age, doc_number):
        super().__init__(first_name, last_name, age, doc_number)
        self.privileges = Privileges(
            ["Can create users", "Can delete users", "Can create files", "Can modify files", "Can erase "
                                                                                             "files"])


class Privileges:
    """
    Here, we intend to pass  list of privileges
    We ensure that we pass a list in the init of Privileges
    """

    def __init__(self, priv: list):
        self.privileges = priv

    def show_privileges(self):
        for item in self.privileges:
            print(f"-{item}")


admin1 = Admin("Aaron", "Williams", 30, 38439837)

admin1.describe_user()
admin1.privileges.show_privileges()
