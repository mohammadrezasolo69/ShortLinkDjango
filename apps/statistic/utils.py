import httpagentparser
from django.utils.translation import get_language_from_request


class UserAgentParser(object):
    def __init__(self, request):
        self.request = request
        self.user_agent = self.request.META.get('HTTP_USER_AGENT')
        self.parser = httpagentparser.detect(self.user_agent)

    @property
    def get_user_os(self):
        try:
            return self.parser['os']['name']
        except:
            return 'Unknown'

    @property
    def get_user_browser(self):
        try:
            return self.parser['browser']['name']
        except:
            return 'Unknown'

    @property
    def get_user_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    @property
    def get_user_language(self):
        return get_language_from_request(self.request)


