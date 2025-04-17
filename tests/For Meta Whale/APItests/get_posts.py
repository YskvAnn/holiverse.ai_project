import requests
import config

url = f"{config.BASE_URL}/api/v1/posts"

headers = {
    "Authorization": f"Bearer {config.API_TOKEN}",
    "accept": "application/json"
}

params = [
    ("page", 1),
    ("category_ids[]", 1),  # ← Обрати внимание на []
    ("category_topic", "events")
]

response = requests.get(url, headers=headers, params=params)

assert response.status_code == 200, (
    f"❌ GET /posts: ожидался статус 200, но получен {response.status_code}\n"
    f"Ответ сервера: {response.text}"
)

print("✅ GET /posts: статус 200 — тест пройден!")
print("Response body:")
print(response.text)
