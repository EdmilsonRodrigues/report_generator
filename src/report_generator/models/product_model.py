from typing import Annotated

from sqlmodel import Field, Relationship, SQLModel

from report_generator.models.analysis_models import (
    NutritionalAnalysisModel,
    PhysicoChemicalAnalysisModel,
    SensorialAnalysisModel,
)
from report_generator.models.links import ProductPhysicoChemicalAnalysisLink


class BaseProduct(SQLModel):
    name: str
    expiration_time: int


class ProductModel(BaseProduct, table=True):
    __tablename__ = 'product'

    id: Annotated[int | None, Field(primary_key=True)] = None


class SimpleProduct(BaseProduct):
    id: int


class DetailedProduct(BaseProduct):
    id: int
    physico_chemical_analyses: Annotated[
        list[PhysicoChemicalAnalysisModel],
        Relationship(
            back_populates='products',
            link_model=ProductPhysicoChemicalAnalysisLink,
            cascade_delete=True,
        ),
    ]
    nutritional_analyses: Annotated[
        list[NutritionalAnalysisModel],
        Relationship(back_populates='product', cascade_delete=True),
    ]
    sensorial_analyses: Annotated[
        list[SensorialAnalysisModel],
        Relationship(back_populates='product', cascade_delete=True),
    ]
