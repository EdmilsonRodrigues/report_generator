import pytest

from report_generator.services.product_service import ProductService


@pytest.fixture
def product_service(fake_repository) -> ProductService:
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


def test_delete_product(product_service, product_factory):
    product = product_factory()
    product_service.product_repository.create(product)

    assert product_service.product_repository.get_count() == 1

    product_service.delete_product(product.id)

    assert product_service.product_repository.get_count() == 0


def test_get_product(product_service, product_factory):
    product = product_factory()
    product_service.product_repository.create(product)

    product_received = product_service.get_product(product.id)
    product.id = product_received.id

    assert product == product_received


def test_get_all_products(product_service, product_factory, faker):
    BATCH_SIZE = faker.pyint(min_value=10, max_value=99)
    products = product_factory.create_batch(BATCH_SIZE)
    limit = faker.pyint(min_value=1, max_value=BATCH_SIZE)
    offset = faker.pyint(min_value=0, max_value=(BATCH_SIZE - limit))

    product_service.product_repository.create_many(products)

    products_received = product_service.get_products(
        limit=limit, offset=offset
    )

    assert products[offset : offset + limit] == products_received


def test_update_products(
    product_service, product_factory, update_product_factory, faker
):
    product = product_factory()
    update_product_request = update_product_factory()

    product_service.product_repository.create(product)

    updated_product = product_service.update_product(
        product.id, update_product_request
    )

    assert updated_product == product_service.product_repository.get(
        product.id
    )
