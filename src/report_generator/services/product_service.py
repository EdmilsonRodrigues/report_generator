from report_generator.dtos.products_dtos import CreateProductRequest
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

    def create_product(self, product_request: CreateProductRequest):
        product = ProductModel(
            name=product_request.name,
            physico_chemical_analyses=product_request.physico_chemical_anaylyses,
            expiration_time=product_request.expiration_time,
        )

        product = self.product_repository.create(product)

        # breakpoint()

        nutritional_analysis_models = [
            NutritionalAnalysisModel(
                product_id=product.id,
                nutrient_id=nutritional_analysis.nutrient_id,
                expected_value=nutritional_analysis.expected_value,
            )
            for nutritional_analysis in product_request.nutritional_analysis
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
            for sensorial_analysis in product_request.sensorial_analysis
        ]

        self.sensorial_analysis_repository.create_many(
            sensorial_analysis_models
        )

        return product
