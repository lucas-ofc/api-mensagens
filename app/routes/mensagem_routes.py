from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.mensagem_schema import Mensagem, MensagemCreate
from app.controllers import mensagem_controller
from app.database.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/mensagens", response_model=Mensagem)
def create_mensagem(mensagem: MensagemCreate, db: Session = Depends(get_db)):
    return mensagem_controller.create_mensagem(db, mensagem)

@router.get("/mensagens", response_model=list[Mensagem])
def read_mensagens(db: Session = Depends(get_db)):
    return mensagem_controller.get_mensagens(db)

@router.get("/mensagens/{mensagem_id}", response_model=Mensagem)
def read_mensagem(mensagem_id: int, db: Session = Depends(get_db)):
    mensagem = mensagem_controller.get_mensagem(db, mensagem_id)
    if mensagem is None:
        raise HTTPException(status_code=404, detail="Mensagem não encontrada")
    return mensagem

@router.put("/mensagens/{mensagem_id}", response_model=Mensagem)
def update_mensagem(mensagem_id: int, mensagem: MensagemCreate, db: Session = Depends(get_db)):
    return mensagem_controller.update_mensagem(db, mensagem_id, mensagem.conteudo)

@router.delete("/mensagens/{mensagem_id}")
def delete_mensagem(mensagem_id: int, db: Session = Depends(get_db)):
    return mensagem_controller.delete_mensagem(db, mensagem_id)
