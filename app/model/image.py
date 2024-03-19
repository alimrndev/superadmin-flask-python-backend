from app import db

class Image(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    path_name = db.Column(db.String(100), nullable=False)

    def __repr__ (self):
        return f"<Image {self.title}>"
