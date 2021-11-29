"""
Module for unittesting the microservice logger
"""

#pylint: disable=unused-argument,invalid-name

import unittest

class MockLogger:
    """
    Class for mock and checking logging. Use as a patch.
    """

    def __init__(self, name):
        """
        Keep track of the name and clear the events
        """

        self.name = name
        self.clear()

    def clear(self):
        """
        Clears the events. Good between tests
        """

        self.events = []

    @staticmethod
    def event(level, message, extra=None):
        """
        Create and event structure
        """

        event = {
            "level": level,
            "message": message
        }

        if extra:
            event.update(extra)

        return event

    def log(self, level, message, extra=None, **kwargs):
        """
        Log something at a level with extra
        """

        self.events.append(self.event(level, message, extra))

    def exception(self, message, extra=None, **kwargs):
        """
        Log an exception
        """

        self.log("exception", message, extra)

    def critical(self, message, extra=None, **kwargs):
        """
        Log a critical
        """

        self.log("critical", message, extra)

    def error(self, message, extra=None, **kwargs):
        """
        Log an error
        """

        self.log("error", message, extra)

    def warning(self, message, extra=None, **kwargs):
        """
        Log a warning
        """

        self.log("warning", message, extra)

    def info(self, message, extra=None, **kwargs):
        """
        Log an info
        """

        self.log("info", message, extra)

    def debug(self, message, extra=None, **kwargs):
        """
        Log a debug
        """

        self.log("debug", message, extra)


class TestCase(unittest.TestCase):
    """
    Extended unittest.TestCase with asserts used with micro logging
    """

    maxDiff = None

    def consistent(self, first, second):
        """
        A loose equals for checking only the parts of dictionares and lists you care about
        {"a": 1} is consistent with {"a": 1, "b": 2} while {"a": 2} is not
        [1,2] is consistent with [1,2,3] but [1,2,4] is not. Neither is [2,1]
        """

        if isinstance(first, dict) and isinstance(second, dict):

            for first_key, first_item in first.items():
                if first_key not in second or not self.consistent(first_item, second[first_key]):
                    return False

        elif isinstance(first, list) and isinstance(second, list):

            second_index = 0

            for first_item in first:

                found = False

                for second_index, second_item in enumerate(second[second_index:]):
                    if self.consistent(first_item, second_item):
                        found = True
                        break

                if not found:
                    return False

        else:

            return first == second

        return True

    def contains(self, member, container):
        """
        Checks to see if members is conistent with an item within container
        """

        for item in container:
            if self.consistent(member, item):
                return True

        return False

    def assertConsistent(self, first, second, message=None):
        """
        Asserts first is consistent with second
        """

        if not self.consistent(first, second):
            self.assertEqual(first, second, message)

    def assertContains(self, member, container, message=None):
        """
        Asserts member is contained within second
        """

        if not self.contains(member, container):
            self.assertIn(member, container, message)

    def assertLogged(self, logger, level, message, extra=None):
        """
        Assert event is contained within the logger's events
        """

        self.assertContains(MockLogger.event(level, message, extra), logger.events)
