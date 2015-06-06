# tt2srt
Youtube timed text subtitle file converter

## How to download subtitles from Youtube
### Get XML file
If your browser supports HTML5 videos, open the developer tools and go to the Network tab.
Look for the entry that begins with **timedtext** and open it in a new tab and save it to file.
More at http://www.addictivetips.com/web/3-ways-to-download-subtitles-from-a-youtube-video/

### Convert XML file to SRT format
By command below you will get *test.srt* file as a result.
```bash
python tt2srt.py test.xml
```
