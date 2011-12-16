import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Jschain(webapp.RequestHandler):
    def get(self):
        template_values={
            'use_jquery':False,
            'title':'A simple javascript function chaining demo'
        }
        path = os.path.join(os.path.dirname(__file__), 'demos/jschain/index.html')
        self.response.out.write(template.render(path, template_values))

class Chkbox(webapp.RequestHandler):
    def get(self):
        template_values={
            'use_jquery':True,
            'title':'Submit data in array format'
        }
        path = os.path.join(os.path.dirname(__file__), 'demos/chkbox/index.html')
        self.response.out.write(template.render(path, template_values))
    def post(self):
        d=self.request.get_all( 'list[]' )
        self.response.out.write(d)

class Jpost(webapp.RequestHandler):
    def get(self):
        template_values={
            'use_jquery':True,
            'title':'A mistake to avoid when using jQuery.ajax() function'
        }
        path = os.path.join(os.path.dirname(__file__), 'demos/jpost/index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        u=self.request.get('username')
        p=self.request.get('password')
	out="username=%s\npassword=%s" % (u,p)
		
        self.response.out.write(out)

application = webapp.WSGIApplication(
    [
        ('/demos/jschain', Jschain),
        ('/demos/chkbox', Chkbox),
        ('/demos/jpost', Jpost),
], debug=False)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
