import requests
import unittest

class TestPageStatus(unittest.TestCase):

    def test_page_status_200(self):
        url = "https://w-dex.ai/swap"
        try:
            response = requests.get(url, timeout=10)
            self.assertEqual(response.status_code, 200, f"Ожидался статус 200, но получен {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.fail(f"Ошибка при открытии страницы {url}: {e}")

if __name__ == "__main__":
    unittest.main()