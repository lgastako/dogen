class View(object):

    def __init__(self, renderer_selector, template_key_generator):
        self.renderer_selector = renderer_selector
        self.template_key_generator = template_key_generator

    def select_responder(self, request):
        try:
            return getattr(self, request.method.lower())
        except AttributeError:
            raise # TODO: Handle more gracefully

    def select_renderer(self, request, response):
        return self.renderer_selector.select_renderer(request, response)

    def generate_template_key(self, request):
        return self.template_key_generator.generate_template_key(request)

    def acquire_template(self, renderer, template_key):
        return renderer.acquire_template(template_key)

    def get(self, request):
        pass

    def post(self, request):
        return self.get(request)

    def delete(self, request):
        raise NotImplementedError

    def put(self, request):
        raise NotImplementedError

    def head(self, request):
        return self.get(request)

    def process(self, request, response):
        responder = self.select_responder(request)
        response = responder()

        renderer = self.select_renderer(request, response)
        template_key = self.generate_template_key(request)
        template = self.acquire_template(renderer, template_key)
        response.body = renderer.render(data, template)
        return response


class StaticView(View):
    pass
