from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
import uuid



class VisitorMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'visitor_id' not in request.COOKIES:
            # If the visitor does not have an ID, create one and set the session variable
            visitor_id = str(uuid.uuid4())
            request.session['needs_cookie'] = True
            request.visitor_id = visitor_id
        else:
            request.visitor_id = request.COOKIES['visitor_id']
            # No need to set a cookie, so set the session variable to False
            request.session['needs_cookie'] = False

        return None
    


            
        