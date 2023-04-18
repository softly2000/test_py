class User:
    def __init__(self, login, password, access_rights):
        self.login = login
        self.password = password
        self.access_rights = access_rights
    
    def get_login(self):
        return self.login
    
    def set_login(self, login):
        self.login = login
    
    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password
    
    def get_access_rights(self):
        return self.access_rights
    
    def set_access_rights(self, access_rights):
        self.access_rights = access_rights
