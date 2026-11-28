from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Hotelske rezervacije API")


class ZahtjevCijene(BaseModel):
    noci: int = Field(ge=1, le=30)
    cijena_noci: float = Field(gt=0, le=1000000)
    popust: float = Field(default=0.0, ge=0, le=1)


class OdgovorCijene(BaseModel):
    iznos: float


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/cijena", response_model=OdgovorCijene)
def izracunaj(z: ZahtjevCijene) -> OdgovorCijene:
    osnovna_cijena = z.noci * z.cijena_noci
    popust_iznos = osnovna_cijena * z.popust
    ukupno = osnovna_cijena - popust_iznos
    return OdgovorCijene(iznos=round(ukupno, 2))
