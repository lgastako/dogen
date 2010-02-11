import logging
import optparse

from wsgiref import simple_server

import app

logger = logging.getLogger(__name__)


def instantiate_config(config_module_name):
    return __import__(config_module_name)


def main():
    parser = optparse.OptionParser()
    parser.add_option("--host")
    parser.add_option("-p", "--port")
    parser.add_option("--config", default="dogen.defaultconfig")
    options, _args = parser.parse_args()

    config = instantiate_config(options.config)
    application = app.make_application(config)

    host = options.host or config.host
    port = options.port or config.port

    server = simple_server.make_server(host, port, application)
    server.serve_forever()


if __name__ == '__main__':
    main()
