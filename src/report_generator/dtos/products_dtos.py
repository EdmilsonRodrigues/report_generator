from __future__ import annotations

from pydantic import BaseModel


class CreateProductRequest(BaseModel):
    name: str
    expiration_time: int
    physico_chemical_anaylyses: list[int]
    nutritional_analysis: list[CreateNutritionalAnalysisRequest]
    sensorial_analysis: list[CreateSensorialAnalysisRequest]


class CreateNutritionalAnalysisRequest(BaseModel):
    nutrient_id: int
    expected_value: float


class CreateSensorialAnalysisRequest(BaseModel):
    name: str
    expected_value: str
