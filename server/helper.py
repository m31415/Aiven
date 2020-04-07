import requests
import math
from requests import RequestException
from server.errors import InternalServerError
from marshmallow import ValidationError

aiven_cloud_list_url = "https://api.aiven.io/v1/clouds"


def get_aiven_clouds():

    result = requests.get(
        url=aiven_cloud_list_url,
    )

    check_for_error(result)

    return result.json()["clouds"]


def filter_valid_schema(data, schema):
    """
    Return filtered Array of Objects by validation with given schema
    :param data: Array of objects
    :param schema: Schema to validate
    :return: Array of validated Objects
    """
    result = []
    try:
        result = schema(many=True).load(data)
    except ValidationError as err:
        print(err.messages)
    return result


def check_for_error(result):
    """
    Check if request for errors
    :param result:
    :return:
    """
    try:
        result.raise_for_status()
    except RequestException as e:
        raise InternalServerError(
            'Unable to contact contract aiven-API. Error: ' + str(e.response.text)
        )


def calculate_geo_distance(origin, destination):
    """
    Calculate Geo-Distance by Haversine formula (https://en.wikipedia.org/wiki/Haversine_formula)
    **Credits:
        https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
    :param origin:
    :param destination:
    :return:
    """
    r = 6373.0

    [lat1, lon1] = origin
    [lat2, lon2] = destination
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlon = lon2 - lon1

    dlat = lat2 - lat1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return r * c
