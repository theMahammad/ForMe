from app import db
    
# Pakizərin varlığı ruhuna gərək olan(lar olamaz,mən benciləm)
# Rejim 
# Eşqə düşmək olmaz,olanda mallıqlar başlayır
# Siz də eşqdəsiniz?Məhəmmədlə?Əmin oldum artıq
# NƏ GÖZƏLSƏN  CİDDƏN QICIQ OLDUM VƏ DÜŞDÜM

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25))
class Advantage(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    icon = db.Column(db.String(250))
    text = db.Column(db.String(255))




