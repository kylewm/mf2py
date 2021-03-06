import sys
import bs4

if sys.version < '3':
    text_type = unicode
    binary_type = str
else:
    text_type = str
    binary_type = bytes
    basestring = str


def get_attr(el, attr, check_name=None):
    """Get the attribute of an element if it exists and is not empty.

    Args:
      el (bs4.element.Tag): a DOM element
      attr (string): the attribute to get
      check_name (string or list, optional): a list/tuple of strings or single
        string, that must match the element's tag name

    Returns:
      string: the attribute's value
    """
    if check_name is None:
        return el.get(attr)
    if isinstance(check_name, basestring) and el.name == check_name:
        return el.get(attr)
    if isinstance(check_name, (tuple, list)) and el.name in check_name:
        return el.get(attr)


def get_children(node):
    """An iterator over the immediate children tags of this tag"""
    for child in node.contents:
        if isinstance(child, bs4.Tag):
            yield child

def get_descendents(node):
    for child in get_children(node):
        yield child
        for desc in get_descendents(child):
            yield desc
