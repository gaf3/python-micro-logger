# python-micro-logger

A JSON logger made for microservices.

# Usage

```python
import micro_logger

# This overrides the root looger as well

logger = micro_logger.getLogger("my-service")

logger.info("sure", extra={"a": 1})
```

# Testing

```python
import micro_logger_unittest

import micro_logger

# Use this class as a base

class TestUnitTest(micro_logger_unittest.TestCase):

    # Override for all tests

    @unittest.mock.patch("micro_logger.getLogger", micro_logger_unittest.MockLogger)
    def setUp(self):

        self.logger = micro_logger.getLogger("unit")

    # Any test can check for logging

    def test_assertLogged(self):

        self.logger.info("sure", extra={"a": 1})

        self.assertLogged(self.logger, "info", "sure", extra={"a": 1})
```

# Actions

Everyting is done through Docker. No python code is executed locally.

- `make build` - Build a local image to use (do this first)
- `make test` - Run tests
- `make debug` - Run tests with step through debugging. Will pause until the 'micro-logger' debugger is started.
- `make lint`- Run the linter (uses test/.pylintc)
- `make setup` - Verifies this repo can be installed as a Python package
- `make tag` - Tags this commit with the version in Makefile
- `make untag` - Untags this commit
