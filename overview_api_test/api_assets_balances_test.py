import requests

url = "https://backend.rivo.xyz/assets/balances/0xd278A92a2bED505A67987D2d597Afd2AB160bB3a"

def test_assets_balances():
    api_response = requests.get(url)
    assert api_response.status_code == 200, f"Expected status code 200 but got {api_response.status_code}"