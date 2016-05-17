from unittest import TestCase

from dmenu import Dmenu, DmenuCommandError


class TestDmenu(TestCase):

    def test_no_arguments(self):
        Dmenu()

    def test_command_string(self):
        Dmenu(command='a string')

    def test_command_non_string(self):
        self.assertRaises(AssertionError, Dmenu, command=['not', 'a', 'string'])

    def test_bottom_boolean(self):
        Dmenu(bottom=True)
        Dmenu(bottom=False)

    def test_bottom_non_boolean(self):
        self.assertRaises(AssertionError, Dmenu, bottom='not a boolean')

    def test_fast_boolean(self):
        Dmenu(fast=True)
        Dmenu(fast=False)

    def test_fast_non_boolean(self):
        self.assertRaises(AssertionError, Dmenu, fast='not a boolean')

    def test_case_insensitive_boolean(self):
        Dmenu(case_insensitive=True)
        Dmenu(case_insensitive=False)

    def test_case_insensitive_non_boolean(self):
        self.assertRaises(AssertionError, Dmenu, case_insensitive='not a boolean')

    def test_lines_int(self):
        Dmenu(lines=0)
        Dmenu(lines=1)

    def test_lines_non_int(self):
        self.assertRaises(AssertionError, Dmenu, lines='not an int')

    def test_monitor_int(self):
        Dmenu(monitor=0)
        Dmenu(monitor=1)

    def test_monitor_non_int(self):
        self.assertRaises(AssertionError, Dmenu, monitor='not an int')

    def test_font_is_string(self):
        Dmenu(font='a string')

    def test_font_non_string(self):
        self.assertRaises(AssertionError, Dmenu, font=['not', 'a', 'string'])

    def test_background_is_string(self):
        Dmenu(background='a string')

    def test_background_non_string(self):
        self.assertRaises(AssertionError, Dmenu, background=['not', 'a', 'string'])

    def test_foreground_is_string(self):
        Dmenu(foreground='a string')

    def test_foreground_non_string(self):
        self.assertRaises(AssertionError, Dmenu, foreground=['not', 'a', 'string'])

    def test_background_selected_is_string(self):
        Dmenu(background_selected='a string')

    def test_background_selected_non_string(self):
        self.assertRaises(AssertionError, Dmenu, background_selected=['not', 'a', 'string'])

    def test_foreground_selected_is_string(self):
        Dmenu(foreground_selected='a string')

    def test_foreground_selected_non_string(self):
        self.assertRaises(AssertionError, Dmenu, foreground_selected=['not', 'a', 'string'])

    def test_version_bad_command(self):
        dmenu = Dmenu(command='not_actually_the_dmenu_command')

        def version():
            dmenu.version

        self.assertRaises(DmenuCommandError, version)
