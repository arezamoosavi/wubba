import uuid

from nameko.rpc import rpc
from nameko_redis import Redis


class HelloService:
    name = "hello_service"

    redis = Redis("testing")

    @rpc
    def get(self, username, _id):
        return " Hello {} with id {}".format(username, _id)

    @rpc
    def create(self, username):
        _id = uuid.uuid4().hex
        self.redis.set(_id, username)
        return _id
