from utilities.assertions import assert_status_code

def test_view_orders(api_client, auth_data):

    token = auth_data["token"]
    userId = auth_data["userId"]

    headers = {"Authorization" : token}


    order_response = api_client.get(f"order/get-orders-for-customer/{userId}", headers=headers)
    assert_status_code(order_response, 200)
    
    order_data = order_response.json()
    

    assert order_data['data'][0]['orderById'] == userId, "Both ids should match"
    assert len(order_data['data'][0]['orderById']) > 0
    assert isinstance(order_data['data'][0]['orderById'], str)