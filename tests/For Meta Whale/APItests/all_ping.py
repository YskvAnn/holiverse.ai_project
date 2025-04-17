import requests
import config

endpoint = f"{config.BASE_URL}/api/v1/ping"

headers = {
    "Authorization": f"Bearer {config.API_TOKEN}",
    "accept": "application/json"
}

# Список методов и ожиданий
methods = [
    ("GET", 200),
    ("POST", 200),
    ("PUT", 200),
    ("PATCH", 200),
    ("DELETE", 200),
    ("HEAD", 200),
]

# Запускаю каждый запрос
for method, expected_status in methods:
    print(f"➡️  Отправка {method} запроса на {endpoint}...")

    response = requests.request(method, endpoint, headers=headers)

    actual_status = response.status_code

    try:
        assert actual_status == expected_status, (
            f"❌ {method} запрос: ожидался статус {expected_status}, но получен {actual_status}"
        )
        print(f"✅ {method} запрос: статус {actual_status} — OK")
    except AssertionError as e:
        print(str(e))

    if method != "HEAD":
        print("Ответ сервера:")
        print(response.text)
    print("—" * 40)
