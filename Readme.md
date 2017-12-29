`mareau` is a Python utility for analyzing data from API's in various
contexts. The primary goal is to perform rudimentary market research and
analysis based on organic traffic from people and public API's.


## Installing

    pip3 install --user --upgrade https://github.com/jcmdln/mareau/archive/master.zip


## Running

    mareau reddit \
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
