Slack State Flags
---

Add state flags as custom emoji to your Slack. [See illustrations and my write-up here.](https://blog.openstates.org/using-state-flags-as-slack-emoji-4d61f3e2cda8)

### Uploading to Slack

#### By point-and-click

Use a browser extension [like this one](https://chrome.google.com/webstore/detail/neutral-face-emoji-tools/anchoacphlfbdomdlomnbbfhcmcdmjej), and simply drag and drop all the PNGs from `state-flags` into your Slack administrator webpage.

#### By the command line

Use a tool like [`slack-emojinator`](https://github.com/smashwilson/slack-emojinator) to upload the PNGs to Slack as custom emoji:

```bash
git clone https://github.com/smashwilson/slack-emojinator.git
cd slack-emojinator
mkvirtualenv slack-emojinator
pip install -r requirements.txt

# Store your Slack's team name and most recent cookie in environment variables
export SLACK_TEAM=${YOUR_TEAM_NAME}
export SLACK_COOKIE=${YOUR_SLACK_COOKIE}
python upload.py ../state-flags/*
```

### Gathering the flags yourself

I've included the flag PNGs in this repository, so this step isn't necessary. But if you want to see where they came from, or tweak this script for your preferred country, read on!

#### Requirements

- libxml
- Python 3
- `pip install -r requirements`

#### Running

```
$ ./get_flags.py
Downloading flag for Alabama
Downloading flag for Alaska
Downloading flag for American Samoa
Downloading flag for Arizona
Downloading flag for Arkansas
Downloading flag for California
…
```

### Source

Flag images sourced libre from Wikipedia.
