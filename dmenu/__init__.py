'''A dmenu wrapper.

dmenu is a dynamic menu for X, originally designed for dwm. It manages large numbers of user-defined menu items efficiently.

Examples:

    show:

    >>> import dmenu
    >>> menu = dmenu.Dmenu()

    >>> menu.show(['a', 'b', 'c'])
    'a'  # user selected a

    >>> menu.show(['a', 'b', 'c'], prompt='pick a letter')
    'b'  # user selected b

    >>> menu.show(['a', 'b', 'c'])
    None  # user hit escape

    >>> menu.show(['a', 'b', 'c'])
    'd'  # user typed their own selection, d

    version:

    >>> import dmenu
    >>> menu = dmenu.Dmenu()
    >>> menu.version
    'dmenu-4.5, \xc2\xa9 2006-2012 dmenu engineers, see LICENSE for details'

    CommandError:

    >>> import dmenu
    >>> menu = dmenu.Dmenu(command='not_a_valid_dmenu')
    >>> menu.show(['a', 'b', 'c'])
    Traceback (most recent call last):
      ...
    dmenu.dmenu.DmenuCommandError: The provided dmenu command could not be used (['not_a_valid_dmenu']): [Errno 2] No such file or directory: 'not_a_valid_dmenu'

    UsageError:

    >>> import dmenu
    >>> menu = dmenu.Dmenu(monitor=2)
    >>> menu.show(['a', 'b', 'c'])
    Traceback (most recent call last):
      ...
    dmenu.dmenu.DmenuUsageError: This version of dmenu does not support your usage (['dmenu', '-m', '2']):
    usage: dmenu [-b] [-f] [-i] [-l lines] [-p prompt] [-fn font]
                 [-nb color] [-nf color] [-sb color] [-sf color] [-v]
'''
from .dmenu import Dmenu, DmenuError, DmenuCommandError, DmenuUsageError
