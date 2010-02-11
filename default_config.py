from dogen import regexrouter
from dogen.views import StaticView

host = ""
port = 7777

router = regexrouter.make_router([
        (r"^/(\w+).(html|css|js|png|jpg|gif)$", StaticView)
])
