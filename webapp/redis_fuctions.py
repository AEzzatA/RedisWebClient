from typing import Union
from redis import Redis
from webapp.models import RedisServer


class RWCConnectionError(Exception):
    pass


class Connector:
    def __init__(self, server: RedisServer, custom_db: Union[int, None] = None):
        self.server = server

    def __enter__(self):
        try:
            self.conn = Redis(
                host=self.server.host,
                port=self.server.port,
                db=custom_db or self.server.db,
                password=self.server.password,
                decode_responses=True,
            )
        except Exception as err:
            raise RWCConnectionError(f"{err}")

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class ListKV:
    def __init__(self, path: str):
        self.path = path