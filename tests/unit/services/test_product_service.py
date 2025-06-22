import pytest

from report_generator.services.product_service import ProductService


@pytest.fixture
def product_service(fake_repository):
    return ProductService(
        product_repository=fake_repository(),
        nutritional_analysis_repository=fake_repository(),
        sensorial_analysis_repository=fake_repository(),
        physico_chemical_analysis_repository=fake_repository(),
    )


def test_create_product(create_product_factory, product_service):
    product = create_product_factory()
    assert product_service.product_repository.get_count() == 0

    product = product_service.create_product(product)

    assert product_service.product_repository.get_count() == 1
