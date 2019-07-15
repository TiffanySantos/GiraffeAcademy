# import the class, use these as well as the new one defined
from chef import chef
# create your new class, add the inheritance class in ()

class another_chef(chef):
    def make_salmorejo(self):
        print("The chef makes salmorejo.")

    def make_special(self):
        print("The chef makes guacamole.")