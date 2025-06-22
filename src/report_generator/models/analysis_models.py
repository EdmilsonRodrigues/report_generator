from typing import Annotated

from sqlmodel import Field, Relationship, SQLModel


class PhysicoChemicalAnalysisBase(SQLModel):
    name: str
    unity: str


class PhysicoChemicalAnalysisModel(PhysicoChemicalAnalysisBase, table=True):
    __tablename__ = 'physico_chemical_analysis'
    id: Annotated[int | None, Field(primary_key=True)] = None


class PhysicoChemicalAnalysisSimple(PhysicoChemicalAnalysisBase):
    id: int


class PhysicoChemicalAnalysisDetailed(PhysicoChemicalAnalysisBase):
    id: int


class NutritionalAnalysisBase(SQLModel):
    expected_value: float
    nutrient_id: Annotated[
        int | None, Field(foreign_key='nutrient.id', ondelete='CASCADE')
    ] = None


class NutritionalAnalysisModel(NutritionalAnalysisBase, table=True):
    __tablename__ = 'nutritional_analysis'
    id: Annotated[int | None, Field(primary_key=True)] = None
    product_id: Annotated[
        int | None, Field(foreign_key='product.id', ondelete='CASCADE')
    ] = None


class NutritionalAnalysisSimple(NutritionalAnalysisBase):
    id: int


class NutritionalAnalysisDetailed(NutritionalAnalysisBase):
    id: int
    nutrient: Annotated[
        'NutrientModel', Relationship(back_populates='nutritional_analyses')
    ]


class SensorialAnalysisBase(SQLModel):
    expected_value: float
    name: str


class SensorialAnalysisModel(SensorialAnalysisBase, table=True):
    __tablename__ = 'sensorial_analysis'
    id: Annotated[int | None, Field(primary_key=True)] = None
    product_id: Annotated[
        int | None, Field(foreign_key='product.id', ondelete='CASCADE')
    ] = None


class SensorialAnalysisSimple(SensorialAnalysisBase):
    id: int


class SensorialAnalysisDetailed(SensorialAnalysisBase):
    id: int


class NutrientBase(SQLModel):
    name: str
    unit: str


class NutrientModel(NutrientBase, table=True):
    __tablename__ = 'nutrient'
    id: Annotated[int | None, Field(primary_key=True)] = None


class NutrientSimple(NutrientBase):
    id: int

    nutritional_analyses: Annotated[
        list[NutritionalAnalysisModel],
        Relationship(back_populates='nutrient', cascade_delete=True),
    ]
