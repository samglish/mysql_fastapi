# models.py
from sqlalchemy import Column, Integer, String, Date, func
from database import Base
class Etudiant(Base):
    __tablename__ = 'etudiants'
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    age = Column(Integer)
    telephone = Column(String(20))
    adresse = Column(String(255))