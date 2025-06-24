from __future__ import annotations

from pydantic import BaseModel


class CreateProductRequest(BaseModel):
    name: str
    expiration_time: int
    physico_chemical_analyses: list[int]
    nutritional_analyses: list[CreateNutritionalAnalysisRequest]
    sensorial_analyses: list[CreateSensorialAnalysisRequest]


class UpdateProductRequest(BaseModel):
    name: str
    expiration_time: int
    physico_chemical_analyses: list[int]
    nutritional_analyses: list[int]
    sensorial_analyses: list[int]


class CreateNutritionalAnalysisRequest(BaseModel):
    nutrient_id: int
    expected_value: float


class CreateSensorialAnalysisRequest(BaseModel):
    name: str
    expected_value: str
