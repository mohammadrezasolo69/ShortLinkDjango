from apps.statistic.models import Statistic
from apps.statistic.utils import UserAgentParser
from core.configs import app


@app.task
def save_statistic_task(ip, os, browser, language, shortener):
    try:
        Statistic.objects.create(
            ip=ip[0],
            os=os[0],
            browser=browser[0],
            language=language[0],
            shortener=shortener,
        )
    except Exception as e:
        print(e)


def save_redirector_statistic(request, shortener):
    user_agent = UserAgentParser(request)
    ip = user_agent.get_user_ip,
    os = user_agent.get_user_os,
    browser = user_agent.get_user_browser,
    language = user_agent.get_user_language,

    save_statistic_task.delay(ip, os, browser, language, shortener.id)
