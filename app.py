from webob import Request
from webob import Response

from dogen.renderers import default_renderer_selector
from dogen.renderers import default_template_key_generator

VIEW_CACHE = {}

DEFAULT_RENDERER_SELETOR = default_renderer_selector

DEFAULT_TEMPLATE_KEY_GENERATOR = default_template_key_generator


def find_or_create_cached_view(view_class, renderer_selector,
                               template_key_generator):
    # TODO: Ensure we're using the full module name/path as the key
    # (which we probably aren't right now).
    key = view_class.__name__
    view = VIEW_CACHE.get(key)
    if not view:
        view = view_class(renderer_selector, template_key_generator)
        VIEW_CACHE[key] = view
    return view


def make_application(config):

    renderer_selector = getattr(config, "renderer_selector",
                                DEFAULT_RENDERER_SELETOR)

    template_key_generator = getattr(config, "template_key_generator",
                                     DEFAULT_TEMPLATE_KEY_GENERATOR)

    def application(environ, start_response):
        request = Request(environ)

        view_class = config.router.select_view_class(request)
        view = find_or_create_cached_view(view_class, renderer_selector,
                                          template_key_generator)
        response = view.process(request)
        start_response(response.status, response.headerlist)
        return response.app_iter

    return application
