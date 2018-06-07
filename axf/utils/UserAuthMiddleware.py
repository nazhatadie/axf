from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from datetime import datetime
from index.models import userMdel, Userticket


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return None

        users = Userticket.objects.filter(ticket=ticket)
        if users:
            out_time = users[0].deadline.replace(tzinfo=None)
            now_time = datetime.utcnow()
        if out_time > now_time:
            request.user = users[0].user
        else:
            users.delete()
