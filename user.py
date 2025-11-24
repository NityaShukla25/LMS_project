class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def show(self):
        print(self.user_id," ",self.name)
