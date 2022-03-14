import unittest
import unittest.mock

import logging
import micro_logger

class TestMicroLogger(unittest.TestCase):

    def test_logger(self):

        custom = micro_logger.getLogger("unit-test")

        self.assertEqual(custom.name, "unit-test")
        self.assertEqual(custom.level, logging.WARNING)

        root = logging.getLogger()
        self.assertEqual(root.name, "root")
        self.assertEqual(root.level, logging.WARNING)
        self.assertEqual(len(root.handlers), 1)
        self.assertEqual(root.handlers[0].__class__.__name__, "StreamHandler")
        self.assertEqual(root.handlers[0].formatter.__class__.__name__, "JsonFormatter")
        self.assertEqual(root.handlers[0].formatter._fmt, "%(created)f %(asctime)s %(name)s %(levelname)s %(pathname)s %(funcName)s %(lineno)d %(message)s")
        self.assertEqual(root.handlers[0].formatter.datefmt, "%Y-%m-%d %H:%M:%S %Z")

        custom = micro_logger.getLogger("test-unit", level="INFO", root_level=False)

        self.assertEqual(custom.name, "test-unit")
        self.assertEqual(custom.level, logging.INFO)

        root = logging.getLogger()
        self.assertEqual(root.name, "root")
        self.assertEqual(root.level, logging.WARNING)
        self.assertEqual(root.handlers[0].formatter.datefmt, "%Y-%m-%d %H:%M:%S %Z")
