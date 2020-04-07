from unittest.mock import patch
from .base import BaseTest
import json

clouds = [
    {
        "cloud_description": "Africa, South Africa - Azure: South Africa North",
        "cloud_name": "azure-south-africa-north",
        "geo_latitude": -26.198,
        "geo_longitude": 28.03,
        "geo_region": "africa"
    },
    {
        "cloud_description": "Asia, Bahrain - Amazon Web Services: Bahrain",
        "cloud_name": "aws-me-south-1",
        "geo_latitude": 26.07,
        "geo_longitude": 50.55,
        "geo_region": "south asia"
    },
    {
        "cloud_description": "Asia, Hong Kong - Amazon Web Services: Hong Kong",
        "cloud_name": "aws-ap-east-1",
        "geo_latitude": 22.5,
        "geo_longitude": 114,
        "geo_region": "east asia"
    },
    {
        "cloud_description": "Asia, Hong Kong - Azure: East Asia",
        "cloud_name": "azure-eastasia",
        "geo_latitude": 22.5,
        "geo_longitude": 114,
        "geo_region": "southeast asia"
     }
]


class ApiTest(BaseTest):

    @patch('server.services.get_aiven_clouds')
    def test_get_cloud_list(self, aiven_mock):
        aiven_mock.return_value = clouds
        result = json.loads(self.test_client.get("/api/clouds").data)

        assert len(result) == 4

    @patch('server.services.get_aiven_clouds')
    def test_get_cloud_list_with_provider_filter(self, aiven_mock):
        aiven_mock.return_value = clouds
        result = json.loads(self.test_client.get("/api/clouds?provider=azure").data)

        assert len(result) == 2
        assert result[0]["cloud_description"] == "Africa, South Africa - Azure: South Africa North"
        assert result[1]["cloud_description"] == "Asia, Hong Kong - Azure: East Asia"

    @patch('server.services.get_aiven_clouds')
    def test_get_cloud_list_with_distance_sort(self, aiven_mock):
        aiven_mock.return_value = clouds
        result = json.loads(self.test_client.get("/api/clouds?lat=52.520008&lng=13.404954").data)

        assert len(result) == 4
        assert result[0]["cloud_description"] == "Asia, Bahrain - Amazon Web Services: Bahrain"
        assert round(result[0]["distance"]) == 4264

    @patch('server.services.get_aiven_clouds')
    def test_get_cloud_list_with_distance_sort_and_provider_filter(self, aiven_mock):
        aiven_mock.return_value = clouds
        result = json.loads(self.test_client.get("/api/clouds?provider=azure&lat=52.520008&lng=13.404954").data)

        assert len(result) == 2
        assert result[0]["cloud_description"] == "Asia, Hong Kong - Azure: East Asia"
        assert round(result[0]["distance"]) == 8725

    @patch('server.services.get_aiven_clouds')
    def test_get_cloud_list_with_wrong_param(self, aiven_mock):
        aiven_mock.return_value = clouds
        result = self.test_client.get("/api/clouds?provi=azure")

        assert result.status_code == 400
