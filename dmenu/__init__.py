'''A dmenu wrapper.

dmenu is a dynamic menu for X, originally designed for dwm. It manages large
numbers of user-defined menu items efficiently.

Examples:

    >>> import dmenu
    >>> menu = dmenu.Dmenu()

    >>> menu.version
    'dmenu-4.5, \xc2\xa9 2006-2012 dmenu engineers, see LICENSE for details'

    >>> menu.select(['a', 'b', 'c'], prompt='pick a letter:')
    'a'  # user selected a

    >>> menu.select(['a', 'b', 'c'])
    None  # user hit escape

    >>> menu.select(['a', 'b', 'c'])
    'd'  # user typed their own selection, d

    >>> menu = dmenu.Dmenu(command='not_a_valid_dmenu')
    >>> menu.select(['a', 'b', 'c'])
    Traceback (most recent call last):
      ...
    dmenu.errors.DmenuCommandError: The provided dmenu command could not be used (not_a_valid_dmenu): [Errno 2] No such file or directory

    >>> menu = dmenu.Dmenu(monitor=2)
    >>> menu.select(['a', 'b', 'c'])
    Traceback (most recent call last):
      ...
    dmenu.errors.DmenuUsageError: This version of dmenu does not support your usage:

    ['dmenu', '-m', '2']

    usage: dmenu [-b] [-f] [-i] [-l lines] [-p prompt] [-fn font]
                 [-nb color] [-nf color] [-sb color] [-sf color] [-v]
'''
from .dmenu import Dmenu
from .errors import DmenuError, DmenuCommandError, DmenuUsageError
