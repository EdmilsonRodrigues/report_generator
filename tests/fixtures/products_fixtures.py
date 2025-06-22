import factory
import pytest

from report_generator.dtos.products_dtos import (
    CreateNutritionalAnalysisRequest,
    CreateProductRequest,
    CreateSensorialAnalysisRequest,
)
from report_generator.models.product_model import ProductModel


class CreateNutritionalAnalysisFactory(factory.Factory):
    class Meta:
        model = CreateNutritionalAnalysisRequest

    nutrient_id = factory.Faker('pyint', min_value=1)
    expected_value = factory.Faker(
        'pyfloat', min_value=0, left_digits=3, right_digits=3
    )


class CreateSensorialAnalysisFactory(factory.Factory):
    class Meta:
        model = CreateSensorialAnalysisRequest

    name = factory.Faker('word')
    expected_value = factory.Faker('word')


class CreateProductFactory(factory.Factory):
    class Meta:
        model = CreateProductRequest

    name = factory.Faker('word')
    expiration_time = factory.Faker('pyint', min_value=1, max_value=24)
    physico_chemical_anaylyses = factory.List([
        factory.Faker('pyint', min_value=1) for _ in range(4)
    ])
    nutritional_analysis = factory.List([
        CreateNutritionalAnalysisFactory() for _ in range(10)
    ])
    sensorial_analysis = factory.List([
        CreateSensorialAnalysisFactory() for _ in range(4)
    ])


class ProductFactory(factory.Factory):
    class Meta:
        model = ProductModel

    name = factory.Faker('word')
    expiration_time = factory.Faker('pyint', min_value=1, max_value=24)


@pytest.fixture
def create_product_factory():
    return CreateProductFactory


@pytest.fixture
def product_factory():
    return ProductFactory
