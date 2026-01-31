from flask import render_template, jsonify, request
#html sayfası göstermek için,verileri json formatında göndermek için,gelen verileri okumak için
from services import search_dockerhub#dockerhub araması yapan fonksiyon
from models import db, Favorite #modelste veritabanı tablosu ve favori çağırılır

def register_routes(app):
    
    #  Ana Sayfa
    @app.route('/')
    def home():
        return render_template('index.html') # ilk ana yüzü ekler

    # kullanıcının yazdığı kelimeyi al dockerhubta arama yap ama veritabanına kaydetme
    @app.route('/api/search')
    def search_api():
        query = request.args.get('q', '')
        if not query:
            return jsonify([])#boşsa çökmeyi engeller
        results = search_dockerhub(query)#dockerhub apı sıne bağlanıp verileri arka planda çeker
        return jsonify(results)

    #  Favorileri Listele 
    @app.route('/api/favorites', methods=['GET'])
    def get_favorites():
        # Veritabanındaki tüm favorileri çek
        favorites = Favorite.query.all()
        
        # Bunları JSON formatına çevir
        output = []
        for fav in favorites:
            output.append({
                'id': fav.id,
                'image_name': fav.image_name,
                'description': fav.description,
                'star_count': fav.star_count,
                'user_note': fav.user_note
            })
        return jsonify(output)

    #  Favoriye Ekle 
    @app.route('/api/favorites', methods=['POST'])
    def add_favorite():
        data = request.json # Gelen veriyi al
        
        # Yeni bir favori kartı oluştur
        new_fav = Favorite(
            image_name=data['image_name'],
            description=data.get('description', ''),
            star_count=data.get('star_count', 0),
            user_note=data.get('user_note', '')
        )
        
        # Veritabanına ekle ve kaydet
        db.session.add(new_fav) #burda bekletilir
        db.session.commit()#burda kaydedilir
        
        return jsonify({"message": "Favorilere eklendi!"}), 201#yeni bir kaynak başarıyla oluşturuldu demek

    #  Favori Sil
    @app.route('/api/favorites/<int:id>', methods=['DELETE'])
    def delete_favorite(id):
        fav = Favorite.query.get_or_404(id)# 404 not found döndürür
        db.session.delete(fav)
        db.session.commit()
        return jsonify({"message": "Silindi!"})
    










