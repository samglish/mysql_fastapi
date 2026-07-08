# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# URL de connexion : mysql+pymysql://user:password@host/database
# Pour XAMPP par défaut : root sans mot de passe
DATABASE_URL = 'mysql+pymysql://root:@localhost/ecole'
# Créer le moteur de connexion
engine = create_engine(DATABASE_URL)
# Factory de sessions
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# Classe de base pour les modèles
Base = declarative_base()
# Fonction pour obtenir une session (utilisée dans les routes)
def get_db():
    db = SessionLocal()
    try:
     yield db
    finally:
        db.close()