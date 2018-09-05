from pyramid.view import view_config
from pyramid_home_automation import stop_water


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'pyramid_home_automation'}

@view_config(route_name='stop_water', renderer='templates/stop_water_template.pt')
def stop_water(request):
    send_message()
    return {}

