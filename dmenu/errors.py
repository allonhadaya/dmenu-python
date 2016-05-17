class DmenuError(Exception):
    '''The base class for dmenu errors.'''
    pass


class DmenuCommandError(DmenuError):
    def __init__(self, command, error):
        super(DmenuCommandError, self).__init__(
            'The provided dmenu command could not be used (%s): %s' % (
                command,
                error))


class DmenuUsageError(DmenuError):
    def __init__(self, args, usage):
        super(DmenuUsageError, self).__init__(
            "This version of dmenu does not support your usage:\n\n%s\n\n%s" %
            (args, usage))
