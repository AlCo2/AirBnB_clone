#!/usr/bin/python3
"""
unittest for console
"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class testConsole(unittest.TestCase):
    """ test console """

    def test_quit(self):
        """ test quit """
        self.assertTrue(HBNBCommand().onecmd('quit'))

    def test_EOF(self):
        """ test EOF """
        self.assertTrue(HBNBCommand().onecmd('EOF'))

    def test_help(self):
        """ help command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")

    def test_create(self):
        """ create command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create user")

    def test_show(self):
        """ show command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 123")

    def test_update(self):
        """ update command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 123 name 'somename'")

    def test_all(self):
        """ all command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")

    def test_destroy(self):
        """ destory command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 123")
