import unittest
from impresso.echo import echo


class TestEcho(unittest.TestCase):
    def test_echo(self):
        self.assertEqual(echo("Hello, World!"), "Echo: Hello, World!")


if __name__ == "__main__":
    unittest.main()
