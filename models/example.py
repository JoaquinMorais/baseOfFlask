from utils.db import db

class ExampleDatabase(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    describe = db.Column(db.String(300))


    def __init__(self,name,describe):
        self.name = name
        self.describe = describe
    
    def __repr__(self):
        return f'<id: {self.id}, name: "{self.name}", describe: "{self.describe}">'



    