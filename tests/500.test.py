import requests
import unittest

class TestPageStatus(unittest.TestCase):

    def test_page_status_200(self):
        url = "https://a.metaforce.app/news-portal/en"  # Укажите нужный URL для тестирования
        response = requests.get(url)

        # Проверяем, что статус код ответа равен 200
        self.assertEqual(response.status_code, 200, f"Ожидался статус 200, но получен {response.status_code}")

    def test_page_is_accessible(self):
        url = "https://a.metaforce.app/news-portal/en"  # Укажите нужный URL для тестирования
        try:
            response = requests.get(url)
            # Проверяем, что статус код ответа равен 200
            self.assertEqual(response.status_code, 200)
        except requests.exceptions.RequestException as e:
            self.fail(f"Ошибка при открытии страницы {url}: {e}")

if __name__ == "__main__":
    unittest.main()
