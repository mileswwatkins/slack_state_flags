#!/usr/bin/env python

import os
import re
import shutil

import lxml.html
import requests
import us


FLAGS_URL = 'https://en.wikipedia.org/wiki/Flags_of_the_U.S._states_and_territories'
html = requests.get(FLAGS_URL).text
doc = lxml.html.fromstring(html)
doc.make_links_absolute(FLAGS_URL)

STATES_XPATH = '//span[@id="Current_state_flags"]/parent::h2/following-sibling::table[1]//img[contains(@src, "Flag_of")]'
TERRITORIES_XPATH = '//span[@id="Current_federal_district_and_territory_flags"]/parent::h2/following-sibling::table[1]//img[contains(@src, "Flag_of")]'
flag_elems = doc.xpath(STATES_XPATH) + doc.xpath(TERRITORIES_XPATH)

# Given a max dimension, you can change a Wikipedia-rendered SVG-as-PNG URL
# to your desired size
MAX_SLACK_IMAGE_DIMENSION = 128
flags = {
    e.attrib['alt']: re.sub(r'\/\d+px', '/{}px'.format(MAX_SLACK_IMAGE_DIMENSION), e.attrib['src'])
    for e in flag_elems
}

DIRECTORY = 'state-flags'
states = [s for s in us.STATES_AND_TERRITORIES if s not in us.OBSOLETE]
for state in states:
    print("Downloading flag for {}".format(state.name))

    filename = 'flag-us-{}.png'.format(state.abbr.lower())
    png_url = None
    for name, url in flags.items():
        if state.name in name:
            png_url = url
            break
    else:
        raise ValueError("Did not find flag for {}".format(state.name))

    flag_stream = requests.get(png_url, stream=True)
    with open(os.path.join(DIRECTORY, filename), 'wb') as flag_file:
        shutil.copyfileobj(flag_stream.raw, flag_file)
    del flag_stream
