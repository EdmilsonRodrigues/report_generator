from typing import Annotated

from sqlmodel import Field, SQLModel


class ProductPhysicoChemicalAnalysisLink(SQLModel, table=True):
    product_id: Annotated[
        int | None, Field(foreign_key='product.id', primary_key=True)
    ] = None
    physico_chemical_analysis_id: Annotated[
        int | None,
        Field(foreign_key='physico_chemical_analysis.id', primary_key=True),
    ] = None
