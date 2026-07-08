# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db, engine
import models, schemas
models.Base.metadata.create_all(bind=engine)
app = FastAPI(title='API Ecole', version='1.0.0')
# GET /etudiants — liste tous les étudiants
@app.get('/etudiants', response_model=List[schemas.EtudiantResponse])
def lister_etudiants(skip: int = 0, limit: int = 100,
db: Session = Depends(get_db)):
    return db.query(models.Etudiant).offset(skip).limit(limit).all()
# GET /etudiants/{id} — un seul étudiant
@app.get('/etudiants/{etudiant_id}',
response_model=schemas.EtudiantResponse)
def obtenir_etudiant(etudiant_id: int, db: Session = Depends(get_db)):
    etudiant = db.query(models.Etudiant).filter(
    models.Etudiant.id == etudiant_id).first()
    if etudiant is None:
        raise HTTPException(status_code=404,
    detail=f'Étudiant {etudiant_id} non trouvé')
    return etudiant