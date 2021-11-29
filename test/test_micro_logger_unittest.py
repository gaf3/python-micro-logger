import unittest
import unittest.mock
import micro_logger_unittest

import micro_logger


class TestMockLogger(unittest.TestCase):

    @unittest.mock.patch("micro_logger.getLogger", micro_logger_unittest.MockLogger)
    def setUp(self):

        self.logger = micro_logger.getLogger("unit")

    @unittest.mock.patch("micro_logger.getLogger", micro_logger_unittest.MockLogger)
    def test___init__(self):

        logger = micro_logger.getLogger("test")

        self.assertEqual(logger.name, "test")
        self.assertEqual(logger.events, [])

    def test_clear(self):

        self.logger.events = [1, 2, 3]

        self.logger.clear()

        self.assertEqual(self.logger.events, [])

    def test_event(self):

        self.assertEqual(micro_logger_unittest.MockLogger.event("unit", "test", extra={"a": 1}), {
            "level": "unit",
            "message": "test",
            "a": 1
        })

    def test_log(self):

        self.logger.log("unit", "test", extra={"a": 1})

        self.assertEqual(self.logger.events, [{
            "level": "unit",
            "message": "test",
            "a": 1
        }])

    def test_exception(self):

        self.logger.exception("test", extra={"a": 1})

        self.assertEqual(self.logger.events, [{
            "level": "exception",
            "message": "test",
            "a": 1
        }])

    def test_critical(self):

        self.logger.critical("test", extra={"a": 1})

        self.assertEqual(self.logger.events, [{
            "level": "critical",
            "message": "test",
            "a": 1
        }])

    def test_error(self):

        self.logger.error("test", extra={"a": 1})

        self.assertEqual(self.logger.events, [{
            "level": "error",
            "message": "test",
            "a": 1
        }])

    def test_warning(self):

        self.logger.warning("test", extra={"a": 1})

        self.assertEqual(self.logger.events, [{
            "level": "warning",
            "message": "test",
            "a": 1
        }])

    def test_info(self):

        self.logger.info("test", extra={"a": 1})

        self.assertEqual(self.logger.events, [{
            "level": "info",
            "message": "test",
            "a": 1
        }])

    def test_debug(self):

        self.logger.debug("test", extra={"a": 1})

        self.assertEqual(self.logger.events, [{
            "level": "debug",
            "message": "test",
            "a": 1
        }])


class TestUnitTest(micro_logger_unittest.TestCase):

    @unittest.mock.patch("micro_logger.getLogger", micro_logger_unittest.MockLogger)
    def setUp(self):

        self.logger = micro_logger.getLogger("unit")

    def test_consistent(self):

        # dict

        self.assertTrue(self.consistent({"a": 1}, {"a": 1, "b": 2}))
        self.assertFalse(self.consistent({"a": 2}, {"a": 1, "b": 2}))

        # list

        self.assertTrue(self.consistent([1, 2], [1, 2, 3]))
        self.assertFalse(self.consistent([1, 2, 4], [2, 1]))
        self.assertFalse(self.consistent([1, 2], [2, 1]))

        # else

        self.assertTrue(self.consistent("a", "a"))
        self.assertFalse(self.consistent("a", "b"))

    def test_contains(self):

        self.assertTrue(self.contains({"a": 1}, [{"a": 1, "b": 2}]))
        self.assertFalse(self.contains({"a": 2}, [{"a": 1, "b": 2}]))

    def test_assertConsistent(self):

        self.assertConsistent({"a": 1}, {"a": 1, "b": 2})

        with unittest.mock.patch('micro_logger_unittest.TestCase.assertEqual') as mock_equal:

            self.assertConsistent({"a": 2}, {"a": 1, "b": 2}, "nope")
            mock_equal.assert_called_once_with({"a": 2}, {"a": 1, "b": 2}, "nope")

    def test_assertContains(self):

        self.assertContains({"a": 1}, [{"a": 1, "b": 2}])

        with unittest.mock.patch('micro_logger_unittest.TestCase.assertIn') as mock_in:

            self.assertContains({"a": 2}, [{"a": 1, "b": 2}], "nope")
            mock_in.assert_called_once_with({"a": 2}, [{"a": 1, "b": 2}], "nope")

    def test_assertLogged(self):

        self.logger.info("sure", extra={"a": 1})

        self.assertLogged(self.logger, "info", "sure", extra={"a": 1})
