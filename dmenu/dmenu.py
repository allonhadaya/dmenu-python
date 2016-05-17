import re
from subprocess import PIPE, Popen
from sys import version_info

# determine the string type for this version of python
if version_info[0] == 3:
    _string_types = str,
else:
    _string_types = basestring,

# used to match the usage error message
_usage = re.compile('usage:', re.I)


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
            "This version of dmenu does not support your usage: %s\n\n%s" %
            (args, usage))


class Dmenu(object):

    def __init__(
            self,
            command='dmenu',
            bottom=None,
            fast=None,
            case_insensitive=None,
            lines=None,
            monitor=None,
            font=None,
            background=None,
            foreground=None,
            background_selected=None,
            foreground_selected=None):
        '''dmenu is a dynamic menu for X, originally designed for dwm. It manages large numbers of user-defined menu items efficiently.

        Args:
            command (Optional[str]): path to the dmenu command.
            bottom (Optional[bool]): dmenu appears at the bottom of the screen.
            fast (Optional[bool]): dmenu grabs the keyboard before reading stdin. This is faster, but will lock up X until stdin reaches end-of-file.
            case_insensitive (Optional[bool]): dmenu matches menu items case insensitively.
            lines (Optional[int]): dmenu lists items vertically, with the given number of lines.
            monitor (Optional[int]): dmenu is displayed on the monitor number supplied. Monitor numbers are starting from 0.
            font (Optional[str]): defines the font or font set used. eg. "fixed" or "Monospace-12:normal" (an xft font)
            background (Optional[str]): defines the normal background color. #RGB, #RRGGBB, and X color names are supported.
            foreground (Optional[str]): defines the normal foreground color.
            background_selected (Optional[str]): defines the selected background color.
            foreground_selected (Optional[str]): defines the selected foreground color.

        Examples:

            >>> from dmenu import Dmenu

            >>> dmenu = Dmenu()
            >>> dmenu.version
            'dmenu-4.5, \xc2\xa9 2006-2012 dmenu engineers, see LICENSE for details'

            >>> dmenu.select(['a', 'b', 'c'], prompt='pick a letter:')
            >>> # <user selects a>
            'a'

            >>> dmenu.select(['a', 'b', 'c'])
            >>> # <user hits escape>
            None

            >>> dmenu.select(['a', 'b', 'c'])
            >>> # <user types their own selection d>
            'd'

            >>> dmenu = Dmenu(monitor=2)
            >>> # <let's assume the installed version of dmenu does not support the monitor argument>
            >>> dmenu.select(['a', 'b', 'c'])
            Traceback (most recent call last):
                DmenuUsageError: This version of dmenu does not support your usage: ['dmenu', '-m', '2']

                usage: dmenu [-b] [-f] [-i] [-l lines] [-p prompt] [-fn font]
                             [-nb color] [-nf color] [-sb color] [-sf color] [-v]
        '''

        # do the argument types check out?
        assert isinstance(command, _string_types), 'command must be a string'
        assert bottom is None or isinstance(bottom, bool), 'bottom must be a bool'
        assert fast is None or isinstance(fast, bool), 'fast must be a bool'
        assert case_insensitive is None or isinstance(case_insensitive, bool), 'case_insensitive must be a bool'
        assert lines is None or isinstance(lines, int), 'lines must be an int'
        assert monitor is None or isinstance(monitor, int), 'monitor must be an int'
        assert font is None or isinstance(font, _string_types), 'font must be a string'
        assert background is None or isinstance(background, _string_types), 'background must be a string'
        assert foreground is None or isinstance(foreground, _string_types), 'foreground must be a string'
        assert background_selected is None or isinstance(background_selected, _string_types), 'background_selected must be a string'
        assert foreground_selected is None or isinstance(foreground_selected, _string_types), 'foreground_selected must be a string'

        self.command = command
        self.bottom = bottom
        self.fast = fast
        self.case_insensitive = case_insensitive
        self.lines = lines
        self.monitor = monitor
        self.font = font
        self.background = background
        self.foreground = foreground
        self.background_selected = background_selected
        self.foreground_selected = foreground_selected

        # version will be filled lazily before the first call
        self._version = None

    @property
    def version(self):
        '''The dmenu command's version message.

        Raises:
            DmenuCommandError: the dmenu command could not provide a version.
        '''

        if self._version is None:

            try:
                proc = Popen([self.command, '-v'], universal_newlines=True, stdout=PIPE, stderr=PIPE)
            except OSError as err:
                raise DmenuCommandError(self.command, err)

            if proc.wait() != 0:
                raise DmenuCommandError(self.command, proc.stderr.read())

            self._version = proc.stdout.read().rstrip('\n')

        return self._version

    def select(self, items, prompt=None):
        '''Present the user with items to select from.

        Args:
            items (Iterable[str]): the items to present to the user.
            prompt (Optional[str]): defines the prompt to be displayed to the left of the input field.

        Raises:
            DmenuCommandError: the dmenu command failed.
            DmenuUsageError: the dmenu command does not support your usage.

        Returns:
            None if user escapes selection; Ohterwise, a string which may or may not be one of the presented items.
        '''

        assert prompt is None or isinstance(prompt, _string_types), 'prompt must be a string'

        args = self._args(prompt)

        try:
            proc = Popen(args, universal_newlines=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        except OSError as err:
            raise DmenuCommandError(self.command, err)

        with proc.stdin:
            for item in items:
                assert isinstance(item, _string_types), "all items must be strings"
                proc.stdin.write('%s\n' % item)

        if proc.wait() == 0:
            # user selection made
            return proc.stdout.read().rstrip('\n')

        stderr = proc.stderr.read()

        # user escape
        if stderr == '':
            return None

        # usage error
        if _usage.match(stderr):
            raise DmenuUsageError(args, stderr)

        # other error
        raise DmenuCommandError(self.command, stderr)

    def _args(self, prompt):

        args = [self.command]

        if self.bottom:
            args.append('-b')

        if self.fast:
            args.append('-f')

        if self.case_insensitive:
            args.append('-i')

        if self.lines is not None:
            args.extend(('-l', str(self.lines)))

        if self.monitor is not None:
            args.extend(('-m', str(self.monitor)))

        if prompt is not None:
            args.extend(('-p', prompt))

        if self.font is not None:
            args.extend(('-fn', self.font))

        if self.background is not None:
            args.extend(('-nb', self.background))

        if self.foreground is not None:
            args.extend(('-nf', self.foreground))

        if self.background_selected is not None:
            args.extend(('-sb', self.background_selected))

        if self.foreground_selected is not None:
            args.extend(('-sf', self.foreground_selected))

        return args
