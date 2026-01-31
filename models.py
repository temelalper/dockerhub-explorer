from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Favorite(db.Model):#bu veritabanından bir tablo olucak demek
    #eğer db.model yazmazsak sqlalchemy bu sınıfı veritabanına dönüştürmez
    
    
    # id benzersiz olmalı
    id = db.Column(db.Integer, primary_key=True)
    
    # docker'daki seçili ürün ismi
    image_name = db.Column(db.String(100), nullable=False)
    
    # açıklama boş olabilir
    description = db.Column(db.String(500), nullable=True)
    
    # yıldız sayısı
    star_count = db.Column(db.Integer, default=0)
    
    # özel not boş olabilir
    user_note = db.Column(db.Text, nullable=True)

