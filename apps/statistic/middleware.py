from apps.statistic.utils import UserAgentParser


class UserAgentMiddleware(object):
    def __init__(self, get_response=None):
        if get_response is not None:
            self.get_response = get_response

    def __call__(self, request):
        request.user_agent = UserAgentParser(request)
        response = self.get_response(request)
        return response