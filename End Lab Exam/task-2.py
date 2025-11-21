import requests
import json

def get_weather(city_name):
    """
    Fetch the current temperature for a given city using a weather API.

    Args:
        city_name (str): Name of the city (e.g., "Hyderabad")

    Returns:
        float: Temperature value if successful.
        None: If any error occurs.

    Errors Handled:
        - Non-200 HTTP status codes
        - Connection timeout
        - JSON decoding issues
    """

    url = f"https://api.weather.example.com/current?city={city_name}"

    try:
        # Sending request with timeout of 5 seconds
        response = requests.get(url, timeout=5)

        # Check for non-200 status codes
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return None

        try:
            data = response.json()
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON response")
            return None

        # Extract temperature
        temperature = data.get("temperature")
        if temperature is None:
            print("Error: 'temperature' not found in response")
            return None

        return temperature

    except requests.Timeout:
        print("Error: Request timed out")
        return None

    except requests.ConnectionError:
        print("Error: Failed to connect to API")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None



# ------------------ TEST CASES ------------------

import unittest
from unittest.mock import patch, MagicMock

class TestGetWeather(unittest.TestCase):

    @patch("requests.get")
    def test_success(self, mock_get):
        # Fake API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"temperature": 28.5}
        mock_get.return_value = mock_response

        self.assertEqual(get_weather("Delhi"), 28.5)

    @patch("requests.get")
    def test_status_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        self.assertIsNone(get_weather("UnknownCity"))

    @patch("requests.get")
    def test_json_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.side_effect = json.JSONDecodeError("msg", "doc", 0)
        mock_get.return_value = mock_response

        self.assertIsNone(get_weather("Mumbai"))

    @patch("requests.get", side_effect=requests.Timeout)
    def test_timeout(self, mock_get):
        self.assertIsNone(get_weather("Hyderabad"))

    @patch("requests.get", side_effect=requests.ConnectionError)
    def test_connection_error(self, mock_get):
        self.assertIsNone(get_weather("Chennai"))


if __name__ == "__main__":
    unittest.main()
