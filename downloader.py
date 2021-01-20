import requests
import glob
import os
import tarfile
import zipfile
import gzip
import sys

def validate_url(url):
  try:
    response = requests.get(url)
    return response
  except:
    e = sys.exc_info()[0]
    raise e

def okstatus(response):
  if response.status_code == 200:
    return 200
  else:
    return f'Status Code: {response.status_code}'

def buffer_content(response):
    content = response.content
    return response.content

def create_file(buffered, filename):
  if filename in os.listdir():
    new_filename = filename + '_new'
    with open(new_filename, 'wb') as f:
      f.write(buffered)
    return new_filename
  else:
    with open(filename, 'wb') as f:
      f.write(buffered)
    return filename


if __name__ == '__main__':

  url = sys.argv[1]
  filename = sys.argv[2]
  #while True:
    #url = input('Enter URL:')
    #filename = input('Enter destination filename:')

  validation = validate_url(url)
  status = okstatus(validation)
  if status == 200:
    buffer = buffer_content(validation)
    print(create_file(buffer, filename))
  else:
    print(status)
