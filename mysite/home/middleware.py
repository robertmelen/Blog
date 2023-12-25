from wagtail import hooks
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
    





class MyCookieProcessingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Will only add cookies if the request does not have them already
        trigger = request.headers.get("HX-Trigger")

        if trigger == "accept":
            if not request.COOKIES.get('htmxaccepted'):
                request.COOKIES['htmxaccepted'] = True

        elif trigger == "decline":
            print("decline trigger")
            if not request.COOKIES.get('htmxdecline'):
                response = HttpResponse()
                response.set_cookie('htmxdecline', True)
                return response

    def __call__(self, request):
        response = self.get_response(request)

        return response
    
        
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
    
    def __call__(self, request):
         
        
         response = self.get_response(request)

         trigger = request.headers.get("HX-Trigger")

         if trigger == "accept":
            print("accept trigger")
            if not request.COOKIES.get('htmxaccepted'):
                response.set_cookie('htmxacceptedmiddleware', True)
                response["HX-Refresh"] = "true"

         elif trigger == "decline":
            print("decline trigger")
            if not request.COOKIES.get('htmxdecline'):
                 response.set_cookie('htmxdeclinedmiddleware', True)
                
                 response["HX-Refresh"] = "true"
                 
                 

        # Code to be executed for each request/response after
        # the view is called.
        
         return response