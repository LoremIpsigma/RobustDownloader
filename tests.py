import unittest
from downloader import *
from unittest import mock
from io import StringIO
from unittest.mock import mock_open

class DownloadingTest(unittest.TestCase):


  def setUp(self):
    self.response_obj = mock.Mock()
    self.response_obj.status_code = 200
    self.response_obj.content = b'Response'

  @mock.patch('requests.get')
  def test_valid_url(self, get_mock):
    get_mock.return_value = self.response_obj
    self.assertEqual(validate_url('url'), self.response_obj)
    get_mock.side_effect = requests.exceptions.MissingSchema
    self.assertRaises(requests.exceptions.MissingSchema, validate_url, 'abc')

  def test_status_code(self):
    self.assertEqual(okstatus(self.response_obj), self.response_obj.status_code)
    self.response_obj.status_code = 300
    self.assertEqual(okstatus(self.response_obj), 'Status Code: 300')

  def test_download_content(self):
    self.assertEqual(buffer_content(self.response_obj), self.response_obj.content)

  @mock.patch('downloader.os.listdir')
  def test_file_creation(self, dir_mock):
    m = mock_open()
    with mock.patch('downloader.open', m):
      dir_mock.return_value = ['filename',]
      self.assertEqual(create_file(self.response_obj, 'filename'),'filename_new')
      dir_mock.return_value = ['unrelated_filename']
      self.assertEqual(create_file(self.response_obj, 'filename'), 'filename')

    

if __name__ == '__main__':
  unittest.main()