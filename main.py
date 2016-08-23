import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), '/Users/africansalami/templates')

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

import webapp2


hidden_html= """
<input type="hidden" name="food" value="%s">
"""

item_html = "<li>%s</li>"

shopping_list_html = """
<br>
<br>
<h2>Shopping List</h2>
<ul>
%s
</ul>
"""

# class Handler(webapp2.RequestHandler):
#      def get(self):
#          self.response.write('Hello world!')

class Handler(webapp2.RequestHandler):
        def write(self, *a, **kw):
            self.response.out.write(*a, **kw)
            
        def render_str(self, template, **params):
                t = jinja_env.get_template(template)
                return t.render(params)

        def render(self, template, **kw):
                self.write(self.render_str(template, **kw))

class MainPage(Handler):
        def get(self):
                self.render("shopping_list.html")
#         output = form_html
#         output_hidden = ""
# 
#         items = self.request.get_all("food")
#         #if any items are entered (if anyone types in a food)
#         #apply the following string formatting
#         if items:
#                 output_items = ""
#                 for item in items:
#                         #here we build up a list of the hidden items
#                         #and store in output_hidden
#                         output_hidden += hidden_html % item
#                         #here he build up a list of the list items
#                         #and store in output items
#                         output_items += item_html % item
#                 #here we put the saved food list into the shopping list
#                 output_shopping = shopping_list_html % output_items
#                 #here we put the shopping list at the end of the output,
#                 #no idea what is happening here really...
#                 output += output_shopping
#         #here we substitute our hidden list into our output??
#         output = output % output_hidden
#         #here we display the list out to the user
#         self.write(output)

app = webapp2.WSGIApplication([('/', MainPage)
                               ],
                              debug=True)

# app = webapp2.WSGIApplication([
#     ('/', Handler)
# ], debug=True)
