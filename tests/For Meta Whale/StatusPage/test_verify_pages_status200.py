import unittest
import requests

class TestPageStatuses(unittest.TestCase):

    def setUp(self):
        # Список URL-ов для проверки
        self.urls = [
            "https://b.metaforce.app/Home",
            "https://b.metaforce.app/TS",
            "https://uv.holiverse.ai/pages/overview"
        ]

    def test_pages_status_200(self):
        for url in self.urls:
            with self.subTest(url=url):
                response = requests.get(url)
                self.assertEqual(response.status_code, 200, f"Ошибка на странице {url}: Статус {response.status_code}")

if __name__ == '__main__':
    unittest.main()
