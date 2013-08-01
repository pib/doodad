class WithChildren(object):
    """
    >>> class BadChild(WithChildren):
    ...     pass
    ...
    >>> c = BadChild()
    >>> c.to_dict()
    Traceback (most recent call last):
    ...
    AssertionError: subclasses must override _child_type
    """

    _child_type = None

    def __init__(self, *children):
        for child in children:
            assert isinstance(child, self._child_type)
        self._children = children

    def to_dict(self):
        assert self._child_type, 'subclasses must override _child_type'
        return {self._children_key: [c.to_dict() for c in self._children]}

    @property
    def _children_key(self):
        return self._child_type.__name__.lower() + 's'


class Doodad(object):
    def to_dict(self):
        return {'type': 'Doodad'}


class Column(WithChildren):
    _child_type = Doodad

    def __init__(self, *children, **kwargs):
        super(Column, self).__init__(*children)
        self.rows = kwargs.get('rows', [])

    def to_dict(self):
        d = super(Column, self).to_dict()
        d['rows'] = [r.to_dict() for r in self.rows]
        return d


class Row(WithChildren):
    _child_type = Column


class Layout(WithChildren):
    _child_type = Row
