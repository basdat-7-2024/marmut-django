def user_profile(request):
    return {
        'is_login': request.session.get('is_login'),
        
    }