from unittest import main, TestCase
from mock import patch

from config import GlobalParams, Singleton


class TestGlobalParams(TestCase):

    @patch("config.GlobalParams.get_yml_file")
    def test___init__(self, mock_read_yml):
        mock_read_yml.return_value = {"one": 1, "two": 2}
        test = GlobalParams()
        self.assertEqual({'one': 1, 'two': 2}, test)

        test_two = GlobalParams()
        self.assertEqual(id(test), id(test_two))
        Singleton._instances = {}

    @patch("config.yaml")
    @patch("config.open")
    @patch("config.sys")
    def test_get_yml_file(self, mock_sys, mock_open, mock_yaml):
        mock_sys.argv = ["test.yml"]
        out_come = GlobalParams.get_yml_file()

        self.assertEqual(mock_yaml.load.return_value, out_come)
        mock_open.assert_called_once_with("test.yml")
        mock_yaml.load.assert_called_once_with(mock_open.return_value.__enter__.return_value,
                                               Loader=mock_yaml.FullLoader)


if __name__ == '__main__':
    main()
