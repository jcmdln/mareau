`markan` is a Python utility for performing market analysis by grabbing
data from an API to then be imported and stylized as a Google Sheet.
This allows for grabbing essential stats and/or information from an
endpoint to build rich reports using the graphing and charting tools
within Google Sheets which may be easily shared.

Python 3 is the primary supported version, though additional work to
support Python 2 as well as the Pypy variants will be performed.


## ToDo

- Analysis
  - Export API data to Google Sheets
    - Require a blank Google Sheet for custom formatting
    - Users should be able to define which sheet they want to use
    - Split all data into quarterly sections with the first page being
      the complete overview
- Comments
  - Build local set of sqlite databases in their own namespaces
  - Build a list of comments containing words from custom dictionaries
- Google Sheets
  - Create or update a Google Sheet with the


## Installing

    $ pip install --user --upgrade https://github.com/jcmdln/markan/archive/master.zip
    $ markan
    Usage: markan [OPTIONS] COMMAND [ARGS]...

    Options:
      -v, --version  Show the version and exit.
      -h, --help     Show this message and exit.

    Commands:
      reddit  Interact with Reddit
      sheets  Interact with Google Sheets
