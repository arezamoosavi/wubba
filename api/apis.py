import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class ApiService:
    name = "api"

    hello_rpc = RpcProxy("hello_service")

    @http("GET", "/hi/<string:username>")
    def get_airport(self, request, username):
        _id = self.hello_rpc.create(username)
        msg = self.hello_rpc.get(username, _id)

        return json.dumps({"Messege ": msg})
