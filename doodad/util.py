def classtree_map(root_class):
    """
    >>> class Root(object):
    ...     __module__ = 'fake'
    >>> class Sub(Root):
    ...     __module__ = 'fake'
    >>> class SubSub(Sub):
    ...     __module__ = 'fake'
    >>> ctm = classtree_map(Root)
    >>> for k in sorted(ctm.keys()):
    ...     print((k, ctm[k]))
    ('fake.Root', <class 'fake.Root'>)
    ('fake.Sub', <class 'fake.Sub'>)
    ('fake.SubSub', <class 'fake.SubSub'>)
    """
    classes = set([root_class])
    tocheck = set([root_class])
    while tocheck:
        parent = tocheck.pop()
        subs = parent.__subclasses__()
        classes.update(subs)
        tocheck.update(subs)

    return {'{}.{}'.format(cls.__module__, cls.__name__): cls
            for cls in classes}
