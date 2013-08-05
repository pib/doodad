from .util import classtree_map


class Doodad(object):
    _div_classname = 'doodad'

    def __init__(self, **attrs):
        self.extra_class = ''
        self._attrs = attrs

    def __str__(self):
        return self.to_str()

    def to_str(self, extra_class=''):
       return '<div class="{}">{}</div>'.format(
            self._div_classes(extra_class), self._div_content())

    def _div_classes(self, extra_class):
        classes = self._div_classname
        for cls in extra_class, self.extra_class:
            if cls:
                classes = ' '.join((cls, classes))
        return classes

    def _div_content(self):
        return ''

    def to_dict(self):
        d = {'type': self.type_name()}
        d.update(self._attrs)
        return d

    @classmethod
    def type_name(cls):
        return '{}.{}'.format(cls.__module__, cls.__name__)

    @classmethod
    def from_dict(cls, source):
        type_name = source['type']
        if type_name == cls.type_name():
            return cls(**source)
        else:
            classmap = classtree_map(Doodad)
            return classmap[type_name].from_dict(source)


class Container(Doodad):
    _div_classname = 'container'

    _child_superclass = Doodad

    def __init__(self, *children, **attrs):
        super(Container, self).__init__(**attrs)

        for child in children:
            assert isinstance(child, self._child_superclass)
        self._children = children

    def _div_content(self):
        return ''.join(str(c) for c in self._children)

    def to_dict(self):
        doodad_dict = super(Container, self).to_dict()
        doodad_dict.update({'children': [c.to_dict() for c in self._children]})
        return doodad_dict

    @classmethod
    def from_dict(cls, source):
        classmap = classtree_map(Doodad)

        source = source.copy()
        children = [classmap[child['type']].from_dict(child)
                    for child in source.pop('children', [])]

        return classmap[source['type']](*children, **source)


class Column(Container):
    _div_classname = 'columns'


class Row(Container):
    _div_classname = 'row'
    _child_superclass = Column

    def _div_content(self):
        column_size = (12 // len(self._children)) if self._children else 12

        return ''.join(c.to_str(extra_class='large-{}'.format(column_size))
                       for c in self._children)
