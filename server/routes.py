from server import api


def base_url(suffix):
    return '/api' + suffix


def init_routes(app_api):
    """
    In this function all routes get initialized
    :param app_api: The restful api.
    :return: None
    """
    app_api.add_resource(api.CloudListResource, base_url('/clouds'))
