`mareau` is a Python utility for analyzing data from API's in various
contexts. The primary goal is to perform rudimentary market research and
analysis based on organic traffic from people and public API's.


## Installing

    pip3 install --user --upgrade https://github.com/jcmdln/mareau/archive/master.zip


## Running

    $ mareau
    Usage: mareau [OPTIONS] COMMAND [ARGS]...

    Options:
      -v, --version  Show the version and exit.
      -h, --help     Show this message and exit.

    Commands:
      reddit  Interact with Reddit
      sheets  Interact with Google Sheets
    $ mareau reddit -h
    Usage: mareau reddit [OPTIONS]

    Options:
      -i, --client_id TEXT      Oauth2 client id
      -s, --client_secret TEXT  Oauth2 client secret
      -r, --subreddit TEXT      Target subreddit
      -u, --user_agent TEXT     Useragent
      -h, --help                Show this message and exit.
    $ mareau reddit \
      -u 'useragent' \
      -i 'client_id' -s 'client_secret' \
      -r 'subreddit'


## ToDo

- Analysis
  - Export API data to Google Sheets
    - Require a blank Google Sheet for custom formatting
- Comments
  - Build CSV of user, comment, replies, timestamp
  - Build a list of comments containing words from custom dictionaries
- Projections
  - WIP
- Statistics
  - WIP
- Trending
  - WIP
