'''A dmenu wrapper.

dmenu is a dynamic menu for X, originally designed for dwm. It manages large numbers of user-defined menu items efficiently.'''

from .dmenu import show, version, DmenuError, DmenuCommandError, DmenuUsageError

__version__ = '0.2.1'
