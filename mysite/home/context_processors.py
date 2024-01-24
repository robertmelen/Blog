

def visited_before(request):
    visited_before = 'visited_before' in request.session
    request.session['visited_before'] = True
    return {'visited_before': visited_before}




