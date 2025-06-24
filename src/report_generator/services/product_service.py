from report_generator.dtos.products_dtos import (
    CreateProductRequest,
    UpdateProductRequest,
)
from report_generator.models.analysis_models import (
    NutritionalAnalysisModel,
    SensorialAnalysisModel,
)
from report_generator.models.model_protocols import Repository
from report_generator.models.product_model import ProductModel


class ProductService:
    def __init__(
        self,
        product_repository: Repository,
        nutritional_analysis_repository: Repository,
        sensorial_analysis_repository: Repository,
        physico_chemical_analysis_repository: Repository,
    ):
        self.product_repository = product_repository
        self.nutritional_analysis_repository = nutritional_analysis_repository
        self.sensorial_analysis_repository = sensorial_analysis_repository
        self.physico_chemical_analysis_repository = (
            physico_chemical_analysis_repository
        )

    def get_products(self, limit: int = 10, offset: int = 0):
        """
        Fetch products limited by limit and after an offset

        :param limit: The limit of products to fetch
        :type limit: int
        :param offset: How many products to skip
        :type offset: int
        :returns: The fetched products


        """
        return self.product_repository.get_many(limit=limit, offset=offset)

    def get_product(self, product_id: int):
        """
        Fetch a product by its id

        :param product_id: The id of the product to fetch
        :type product_id: int
        :returns: The fetched product

        """
        return self.product_repository.get(product_id)

    def create_product(self, product_request: CreateProductRequest):
        """
        Creates a product and its analyses from a product request and returns
        the created product.

        :param product_request: the product request
        :type product_request: CreateProductRequest

        :returns: the created product

        """
        product_model = ProductModel(
            name=product_request.name,
            physico_chemical_analyses=product_request.physico_chemical_analyses,
            expiration_time=product_request.expiration_time,
        )

        product = self.product_repository.create(product_model)

        nutritional_analysis_models = [
            NutritionalAnalysisModel(
                product_id=product.id,
                nutrient_id=nutritional_analysis.nutrient_id,
                expected_value=nutritional_analysis.expected_value,
            )
            for nutritional_analysis in product_request.nutritional_analyses
        ]

        self.nutritional_analysis_repository.create_many(
            nutritional_analysis_models
        )

        sensorial_analysis_models = [
            SensorialAnalysisModel(
                product_id=product.id,
                name=sensorial_analysis.name,
                expected_value=sensorial_analysis.expected_value,
            )
            for sensorial_analysis in product_request.sensorial_analyses
        ]

        self.sensorial_analysis_repository.create_many(
            sensorial_analysis_models
        )

        return product

    def update_product(
        self, product_id: int, update_request: UpdateProductRequest
    ):
        nutritional_analyses = update_request.nutritional_analyses
        sensorial_analyses = update_request.sensorial_analyses

        product = self.product_repository.get(product_id)
        original_nutritional_analyses = set(
            self.nutritional_analysis_repository.get_many_by_field(
                'product_id', product_id
            )
        )
        original_sensorial_analyses = set(
            self.sensorial_analysis_repository.get_many_by_field(
                'product_id', product_id
            )
        )

        unneeded_nutritional_analyses = (
            original_nutritional_analyses.difference(nutritional_analyses)
        )
        unneeded_sensorial_analyses = original_sensorial_analyses.difference(
            sensorial_analyses
        )

        self.nutritional_analysis_repository.delete_many(
            unneeded_nutritional_analyses
        )
        self.sensorial_analysis_repository.delete_many(
            unneeded_sensorial_analyses
        )

        return self.product_repository.update(
            product.id,
            {
                k: v
                for k, v in product.model_dump().items()
                if k in ProductModel.model_fields
            },
        )

    def delete_product(self, product_id: int):
        """
        Deletes a product by its product id

        :param product_id: The id for the product to be deleted
        :type product_id: int
        :returns: None
        """
        self.product_repository.delete(product_id)
