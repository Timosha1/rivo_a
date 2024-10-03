import requests

url = "https://data.rivo.xyz/v1/userdata/0xd278A92a2bED505A67987D2d597Afd2AB160bB3a/pnl_rivo?period=1month"

def test_pnl_data():
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    data = response.json()

    assert isinstance(data, list), "Response data is not a list"

    required_fields = [
        "chain_name", "currency_address", "currency_ticker", "currency_name", "pnl", "pnl_percent"
    ]

    for item in data:
        for field in required_fields:
            assert field in item, f"Missing field: {field} in item {item}"
            assert item[field] != "", f"Field {field} is empty in item {item}"

        assert item["pnl"] != 0, f"pnl is 0 in item {item}"
        assert item["pnl_percent"] != 0, f"pnl_percent is 0 in item {item}"
