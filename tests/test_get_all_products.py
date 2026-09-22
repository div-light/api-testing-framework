from utilities.schema_validator import validate_schema
from utilities.product_schema import product_schema
from utilities.logger import logger


def test_get_all_products(api_client, auth_data):
    response = api_client.post(
        "product/get-all-products",
        headers={"Authorization": auth_data["token"]}
    )

    logger.info(f"the response is {response.json()}")

    validate_schema(response.json(), product_schema)