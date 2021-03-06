[![Build Status](https://travis-ci.org/clbarnes/CATMAID-synapsesuggestor.svg?branch=master)](https://travis-ci.org/clbarnes/CATMAID-synapsesuggestor)
[![Coverage Status](https://coveralls.io/repos/github/clbarnes/CATMAID-synapsesuggestor/badge.svg?branch=master)](https://coveralls.io/github/clbarnes/CATMAID-synapsesuggestor?branch=master)

WORK IN PROGRESS

# CATMAID-synapsesuggestor

synapsesuggestor is a django application which acts as a drop-in
extension for [CATMAID](http://www.catmaid.org). It contains API
endpoints and static files for:

- [ ] Creating synapse detection jobs
- [x] Adding the results to the catmaid database
- [ ] Viewing and analysing the results

## Quick start

1. Install synapsesuggestor in whichever python environment is running
CATMAID with `pip install -e path/to/this/directory`

2. Run `python manage.py migrate` to create the synapsesuggestor models.

3. Run `python manage.py collectstatic -l` to pick up
synapsesuggestor's static files.
