from django.shortcuts import render_to_response


def handler404(request, exception=None):
    template_name = 'main/404.html'
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler403(request, exception=None):
    template_name = 'main/403.html'
    response = render_to_response(template_name)
    response.status_code = 403
    return response


def handler500(request, exception=None):
    template_name = 'main/500.html'
    response = render_to_response(template_name)
    response.status_code= 500
    return response


def handler400(request, exception=None):
    template_name = 'main/400.html'
    response = render_to_response(template_name)
    response.status_code = 400
    return response
