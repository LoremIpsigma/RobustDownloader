(Fairly) Robust file downloader written in Python. First attempt at TDD so the script looks to be structured differently than what one would write for a simple file downloader. Tests are available with the script and can be run as any other python file.

> `  USAGE`

Run the script as a module (python -m RobustDownloader x y) where x and y are the strings of the url and filename respectively.

> `python -m RobustDownloader https://pypi.org/ pypi.html`

This command will download the html of the pypi homepage and store it as the file titled 'pypi.html'.

To run the tests:

>  `$ python tests.py`
