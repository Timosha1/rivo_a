import requests

url = "https://backend.rivo.xyz/overview/balances/no-chain/address/0xd278A92a2bED505A67987D2d597Afd2AB160bB3a"

def test_total_balance():
    api_response = requests.get(url)
    assert api_response.status_code == 200, f"Expected status code 200 but got {api_response.status_code}"
    data_from_api = api_response.json()
    total_balance = data_from_api.get("totalBalance", None)

    # Проверяем, что totalBalance не равно нулю и существует
    assert total_balance is not None, "totalBalance is missing in the response"
    assert total_balance != 0, f"totalBalance is 0: {total_balance}"