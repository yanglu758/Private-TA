import webapp2
from constants import jinja
from google.appengine.api import users


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        title = "Private TA Home"
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        template_values = {
            'title': title,
            'url': url,
            'url_linktext': url_linktext,
        }
        template = jinja.JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

