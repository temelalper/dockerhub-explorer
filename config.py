import os

class Config:
   
    SQLALCHEMY_DATABASE_URI = "sqlite:///favorites.db"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #terminalin warning vermesinden kurtuluyoruz

    SECRET_KEY = "dockerhub-secret"#eğer çerez bozulursa flask o çerezi reddeder

   # sqlalchemy == orm yapısı veritabanı ile python ın birbirini anlamasına yarar