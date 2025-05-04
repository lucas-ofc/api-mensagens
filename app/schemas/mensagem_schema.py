from pydantic import BaseModel

class MensagemBase(BaseModel):
    conteudo: str

class MensagemCreate(MensagemBase):
    pass

class Mensagem(MensagemBase):
    id: int

    class Config:
        from_attributes = True
