from .util import classtree_map


class Doodad(object):
    def to_dict(self):
        return {'type': self.type_name()}

    @classmethod
    def type_name(cls):
        return '{}.{}'.format(cls.__module__, cls.__name__)

    @classmethod
    def from_dict(cls, source):
        type_name = source['type']
        if type_name == cls.type_name():
            return cls()
        else:
            classmap = classtree_map(Doodad)
            return classmap[type_name].from_dict(source)


class Container(Doodad):
    def __init__(self, *children):
        for child in children:
            assert isinstance(child, Doodad)
        self._children = children

    def to_dict(self):
        doodad_dict = super(Container, self).to_dict()
        doodad_dict.update({'children': [c.to_dict() for c in self._children]})
        return doodad_dict

    @classmethod
    def from_dict(cls, source):
        classmap = classtree_map(Doodad)

        source = source.copy()
        children = [classmap[child['type']].from_dict(child)
                    for child in source.get('children', [])]

        return classmap[source['type']](*children)


class Column(Container):
    pass


class Row(Container):
    pass


class Layout(Container):
    pass
