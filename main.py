# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db, engine
import models, schemas
models.Base.metadata.create_all(bind=engine)
app = FastAPI(title='API Ecole', version='1.0.0')
# POST /etudiants — créer un étudiant
@app.post('/etudiants', response_model=schemas.EtudiantResponse, status_code=status.HTTP_201_CREATED)
def creer_etudiant(data: schemas.EtudiantCreate,
    db: Session = Depends(get_db)):
    existant = db.query(models.Etudiant).filter(
    models.Etudiant.email == data.email).first()
    if existant:
        raise HTTPException(status_code=400,
    detail='Email déjà utilisé')
    nouveau = models.Etudiant(**data.model_dump())
    db.add(nouveau)
    db.commit()
    db.refresh(nouveau)
    return nouveau
# PUT /etudiants/{id} — modifier un étudiant
@app.put('/etudiants/{etudiant_id}',
response_model=schemas.EtudiantResponse)
def modifier_etudiant(etudiant_id: int, data: schemas.EtudiantUpdate,
    db: Session = Depends(get_db)):
    etudiant = db.query(models.Etudiant).filter(
    models.Etudiant.id == etudiant_id).first()
    if etudiant is None:
        raise HTTPException(status_code=404, detail='Non trouvé')
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(etudiant, key, value)
        db.commit()
        db.refresh(etudiant)
    return etudiant
# DELETE /etudiants/{id} — supprimer un étudiant
@app.delete('/etudiants/{etudiant_id}')
def supprimer_etudiant(etudiant_id: int, db: Session = Depends(get_db)):
    etudiant = db.query(models.Etudiant).filter(
    models.Etudiant.id == etudiant_id).first()
    if etudiant is None:
        raise HTTPException(status_code=404, detail='Non trouvé')
        db.delete(etudiant)
        db.commit()
    return {'message': f'Étudiant {etudiant_id} supprimé'}
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