def includeme(config):
    config.add_renderer('doodad', DoodadRenderer)


class DoodadRenderer(object):
    def __init__(self, info):
        pass

    def __call__(self, value, system):
        pass
