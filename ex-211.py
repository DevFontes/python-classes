# method vs @classmethod vs @staticmethod

# method - self, instance method

# @classmethod - cls, class method

# @staticmethod - static method (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.pwd = None

    def set_user(self, user):
        self.user = user
    
    def set_pwd(self, pwd):
        self.pwd = pwd
    
    @classmethod
    def create_with_auth(cls, user, pwd):
        connection = cls()
        connection.user = user
        connection.pwd = pwd
        return connection
    
    @staticmethod
    def log(message):
        return('LOG:', message)

# Instance Method
c1 = Connection()
c1.set_user('Morgan')
print(c1.user)
c1.set_pwd('123deoliveira4')
print(c1.pwd)

# Class Method
c2 = Connection.create_with_auth('MrFake', '2_15_>_3')
print(c2.user, c2.pwd)


print(Connection.log('Description of Log'))