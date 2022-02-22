# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['popcorn_time_api']

package_data = \
{'': ['*']}

install_requires = \
['Pygments>=2.11,<3.0',
 'aiohttp>=3.8.1,<4.0.0',
 'astroid>=2.9,<3.0',
 'bleach>=4.1,<5.0',
 'certifi>=2021.10,<2022.0',
 'charset-normalizer>=2.0,<3.0',
 'colorama>=0.4,<0.5',
 'docutils>=0.18,<0.19',
 'idna>=3.3,<4.0',
 'importlib-metadata>=4.10,<5.0',
 'isort>=5.10,<6.0',
 'keyring>=23.5,<24.0',
 'lazy-object-proxy>=1.7,<2.0',
 'mccabe>=0.6,<0.7',
 'packaging>=21.3,<22.0',
 'pkginfo>=1.8,<2.0',
 'platformdirs>=2.4,<3.0',
 'pylint>=2.12,<3.0',
 'pyparsing>=3.0,<4.0',
 'pywin32-ctypes>=0.2,<0.3',
 'readme-renderer>=32.0,<33.0',
 'rfc3986>=1.5,<2.0',
 'six>=1.16,<2.0',
 'toml>=0.10,<0.11',
 'tqdm>=4.62,<5.0',
 'twine>=3.7,<4.0',
 'urllib3>=1.26,<2.0',
 'webencodings>=0.5,<0.6',
 'wrapt>=1.13,<2.0',
 'zipp>=3.7,<4.0']

setup_kwargs = {
    'name': 'popcorn-time-api',
    'version': '0.3.0',
    'description': 'Interact with the Popcorn Time API with python',
    'long_description': '# Popcorn Time API ![Version](https://img.shields.io/badge/Version-v0.2.0-orange?style=flat-square&url=https://github.com/DEADSEC-SECURITY/popcorn-time-api/blob/main/CHANGELOG.md) ![Python_Version](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square) ![License](https://img.shields.io/badge/License-MIT-red?style=flat-square) ![Donate](https://img.shields.io/badge/Donate-Crypto-yellow?style=flat-square) [![CodeQL](https://github.com/DEADSEC-SECURITY/popcorn-time-api/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/DEADSEC-SECURITY/popcorn-time-api/actions/workflows/codeql-analysis.yml) [![Downloads](https://pepy.tech/badge/popcorn-time)](https://pepy.tech/project/popcorn-time) [![Downloads](https://pepy.tech/badge/popcorn-time/month)](https://pepy.tech/project/popcorn-time)\n \n## 📝 CONTRIBUTIONS\n\nBefore doing any contribution read <a href="https://github.com/DEADSEC-SECURITY/popcorn-time-api/blob/main/CONTRIBUTING.md">CONTRIBUTING</a>.\n\n## 📧 CONTACT\n\nEmail: amng835@gmail.com\n\nGeneral Discord: https://discord.gg/dFD5HHa\n\nDeveloper Discord: https://discord.gg/rxNNHYN9EQ\n\n## 📥 INSTALLING\n<a href="https://pypi.org/project/popcorn-time">Latest PyPI stable release</a>\n```bash\npip install popcorn-time\n```\n\n## ⚙ HOW TO USE\n```python\nfrom popcorntime import PopcornTime\npopAPI = PopcornTime()\n```\n\n## 🤝 PARAMETERS\n### CLASS PARAMETERS\n- **debug** : bool, optional\n  - Enable for debug mode (Default: False)\n- **min_peers** : int, optional\n  - Minimum number of peers to select torrent (Default: 0)\n- **min_seeds** : int, optional\n  - Minimum number of seeds to select torrent (Default: 0)\n### FUNCTION PARAMETERS\n- #### FUNCTION `set_logging_level`\n  - **level** : int, required\n    - Set the logging level\n    - Accepted values:\n      - 0: DEBUG\n      - 1: INFO\n      - 2: WARNING\n      - 3: ERROR\n      - 4: CRITICAL\n      - 5: NOTSET\n- #### FUNCTION `set_base_url`\n  - **url** : str, required\n    - Set the base url for the API\n- #### FUNCTION `set_base_url`\n  - **url** : str, required\n    - Set the base url for the API\n- #### FUNCTION `set_min_seeds`\n  - **value** : int, required\n    - Minimum number of seeds to select torrent\n- #### FUNCTION `get_server_status`\n  - Returns the server status in json format\n- #### FUNCTION `get_shows_stats`\n  - Returns the show stats in json format\n- #### FUNCTION `get_shows_page`\n  - **page** : (int, str), required\n  - Returns the shows page in json format\n- #### FUNCTION `get_movies_stats`\n  - Returns the movies stats in json format\n- #### FUNCTION `get_movies_page`\n  - **page** : (int, str), required\n  - Returns the movies page in json format\n- #### FUNCTION `get_show`\n  - **show_id** : (int, str), required\n    - IMDB ID of the show\n  - Returns the show data in json format\n- #### FUNCTION `get_movie`\n  - **movie_id** : (int, str), required\n    - IMDB ID of the movie\n  - Returns the movie data in json format\n- #### FUNCTION `get_random_show`\n  - Returns the show in json format\n- #### FUNCTION `get_random_movie`\n  - Returns the movie in json format\n- #### FUNCTION `get_best_torrent`\n  - **torrents** : dict, required\n    - The dictionary of torrents provided by the API (get_show or get_movie)\n  - **min_quality** : int, optional\n    - Minimum quality to select torrent (Default: \'1080\')\n  - **revert_to_default** : bool, optional\n    - Revert to default item if no torrents are found (Default: False)\n  - Returns the best torrent is json format\n\n## Legal Notice\nThis SDK is not meant to be used for illegal purposes, use it at your own risk and check your local regulations first.\n',
    'author': 'DeadSec-Security',
    'author_email': 'amng835@gmail.com',
    'maintainer': 'TheDoctorAI',
    'maintainer_email': '49969231+thedoctorai@users.noreply.github.com',
    'url': 'https://github.com/DEADSEC-SECURITY/popcorn-time-api',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
