from dogen.renderers.jinja2 import Jinja2Renderer
from dogen.renderers.plain import PlainTextRenderer

RENDERERS = {"text/html": Jinja2Renderer(),
             "text/plain": PlainTextRenderer()}


class DefaultRendererSelector(object):
    def select_renderer(self, request, response):
        return RENDERERS[response.headers.content_type]

default_renderer_selector = DefaultRendererSelector()
