from flask_restful import Resource, reqparse
from server import services


class CloudListResource(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('provider', default=None, type=str, help='Filter by Provider')
        parser.add_argument('lat', default=None, type=str, help='Latitude')
        parser.add_argument("lng", default=None, type=str, help='Longitude')

        args = parser.parse_args(strict=True)

        return services.cloud_list_service.get_cloud_list(args)
