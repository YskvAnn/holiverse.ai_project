import requests
import config

id = 64025
url = f"{config.BASE_URL}/api/v1/tickets/{id}"

headers = {
    "Authorization": f"Bearer {config.API_TOKEN}",
    "accept": "application/json"
}
response = requests.get(url, headers=headers)

assert response.status_code == 200, f"❌ Ожидался статус 200, но получен {response.status_code}"

# Если всё ок — вывожу))
print("✅ Статус 200 — тест пройден!")
print("Response body:")
print(response.text)