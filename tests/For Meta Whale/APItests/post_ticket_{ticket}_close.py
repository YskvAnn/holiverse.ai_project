import requests
import config

# Чтение ID тикета из файла
with open("ticket_id.txt", "r") as file:
    ticket = int(file.read().strip())  # Читаем и преобразуем в целое число

url = f"{config.BASE_URL}/api/v1/ticket/{ticket}/close"

headers = {
    "Authorization": f"Bearer {config.API_TOKEN}",
    "accept": "application/json"
}

# Отправляем запрос на закрытие тикета
response = requests.post(url, headers=headers)

# Проверка статуса ответа
assert response.status_code == 200, f"❌ Ожидался статус 200, но получен {response.status_code}"

# Если все ок — выводим успешное сообщение
print("✅ Статус 200 — тест пройден!")
print("Response body:")
print(response.text)
