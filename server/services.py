import copy
from server.helper import get_aiven_clouds, filter_valid_schema, calculate_geo_distance
from marshmallow import Schema, fields


class CloudSchema(Schema):
    cloud_description = fields.Str()
    cloud_name = fields.Str()
    geo_latitude = fields.Float()
    geo_longitude = fields.Float()
    geo_region = fields.Str()


class CloudListService:
    def __init__(self):
        self.cloud_list = []

    def fetch_aiven_clouds(self):
        self.cloud_list = filter_valid_schema(get_aiven_clouds(), CloudSchema)

    def get_cloud_list(self, args):

        if len(self.cloud_list) == 0:
            self.fetch_aiven_clouds()

        provider = args["provider"]
        lat = args["lat"]
        lng = args["lng"]
        cloud_list = copy.deepcopy(self.cloud_list)

        if provider:
            cloud_list = filter_by_provider(cloud_list, provider)
        if lat and lng:
            cloud_list = sort_by_distance(cloud_list, [lat, lng])

        return cloud_list


def filter_by_provider(data, provider):
    """
    Filter List of Cloud objects by provider
    :param data:
    :param provider:
    :return: Filtered List of Cloud objects
    """
    return [cloud for cloud in data if cloud["cloud_name"].split("-")[0] == provider]


def sort_by_distance(data, origin):
    """
    Sort Array of Cloud objects by Geo-Distance
    :param data:
    :param origin:
    :return: Sorted List of Cloud objects
    """
    lat, lng = origin
    for cloud in data:
        cloud["distance"] = calculate_geo_distance(
            [float(lat), float(lng)],
            [cloud["geo_latitude"], cloud["geo_longitude"]]
        )
    return sorted(data, key=lambda x: x["distance"])


cloud_list_service = CloudListService()
