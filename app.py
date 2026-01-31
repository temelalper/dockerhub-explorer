


from flask import Flask
from config import Config
from models import db 
#flask ile veritabanı arasındaki köprüyü sqlalchemy yapar db de onun nesnesidir
from routes import register_routes#tüm routelar tek dosyada favorites vs
#import== başka bir python dosyasındaki kodu getirir
app = Flask(__name__)#benim web uygulamam bu demek bu dosya ana dosya demek

#config dosyasındaki ayarları flaska yükleriz
app.config.from_object(Config)

# veritabanını flaska bağlar
db.init_app(app)

#  Rotaları  kaydet
register_routes(app)

#flask context olmadan db işlemi yapamaz
# tüm modellere create bakar tablo oluşturur
with app.app_context():#flask şu an hangi uygulamada aktif ona bakar ki alttaki tablo için arama yapılsın
    db.create_all()#tanımlı tüm modelleri tarar
#dosya direkt çalışrıtıldığında if name çalışır
if __name__ == '__main__':
    # 5001 portunda çalıştırıyoruz
    app.run(debug=True, port=5001)