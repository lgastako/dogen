class Renderer(object):

    def acquire_template(self, template_key):
        raise NotImplementedError

    def render(self, data, template):
        raise NotImplementedError


class ExampleView(DefaultView):
    def 
