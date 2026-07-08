# schemas.py
from pydantic import BaseModel
from typing import Optional
# Schéma pour créer un étudiant (données reçues)
class EtudiantCreate(BaseModel):
    nom: str
    prenom: str
    email: str
    age: Optional[int] = None
    telephone: Optional[str] = None
    adresse: Optional[str] = None
# Schéma pour modifier un étudiant (toutes les données optionnelles)
class EtudiantUpdate(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    telephone: Optional[str] = None
# Schéma pour les réponses (données envoyées au client)
class EtudiantResponse(EtudiantCreate):
    id: int
class Config:
    from_attributes = True # Permet la conversion SQLAlchemy -> Pydantic