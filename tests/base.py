from unittest import TestCase
from server.serverfactory import ServerFactory


class BaseTest(TestCase):
    FACTORY = ServerFactory

    @classmethod
    def setUpClass(cls):
        cls.factory = cls.FACTORY()
        cls.app = cls.factory.up()
        cls.api = cls.factory.api
        cls.test_client = cls.app.test_client()
