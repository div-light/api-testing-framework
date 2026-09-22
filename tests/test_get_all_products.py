
def test_get_all_products(api_client, auth_data):
    token = auth_data["token"]
    headers = {"Authorization" : token}
    response = api_client.post("product/get-all-products", headers=headers)
    data = response.json()
    assert "fetched Successfully" in data["message"]
    assert data['count'] > 0
    for product in data["data"]:
        assert "_id" in product
        assert "productName" in product
        assert "productPrice" in product
        assert product["productPrice"] > 0

        assert isinstance(product["_id"], str)
        assert isinstance(product["productName"], str)
        assert len(product["productName"]) > 0
        assert isinstance(product["productPrice"], int)
        assert len(data["data"]) == data["count"]
        assert product["productStatus"] == True



"""def test_get_all_products_unauthorized(api_client):

    headers = {
        "Authorization": "invalid_token"
    }

    response = api_client.post(
        "product/get-all-products",
        headers=headers
    )

    print(response.status_code)
    print(response.text)"""