def user_profile(request):
    return {
        'user_is_login': request.session.get('is_login'),
        'user_role': request.session.get('role'),
        'boolean_premium': request.session.get('premium'),
    }