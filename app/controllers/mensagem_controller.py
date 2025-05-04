from sqlalchemy.orm import Session
from app.models.mensagem_model import Mensagem
from app.schemas.mensagem_schema import MensagemCreate

def get_mensagens(db: Session):
    return db.query(Mensagem).all()

def get_mensagem(db: Session, mensagem_id: int):
    return db.query(Mensagem).filter(Mensagem.id == mensagem_id).first()

def create_mensagem(db: Session, mensagem: MensagemCreate):
    db_mensagem = Mensagem(conteudo=mensagem.conteudo)
    db.add(db_mensagem)
    db.commit()
    db.refresh(db_mensagem)
    return db_mensagem

def update_mensagem(db: Session, mensagem_id: int, conteudo: str):
    db_mensagem = get_mensagem(db, mensagem_id)
    if db_mensagem:
        db_mensagem.conteudo = conteudo
        db.commit()
        db.refresh(db_mensagem)
    return db_mensagem

def delete_mensagem(db: Session, mensagem_id: int):
    db_mensagem = get_mensagem(db, mensagem_id)
    if db_mensagem:
        db.delete(db_mensagem)
        db.commit()
    return db_mensagem
