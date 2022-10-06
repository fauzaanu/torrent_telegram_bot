# Torrent Telegram Bot

## Multiple API's are utilized inorder to make everything work.
1. Rapid API - Webtor.io (starting at $2/month)
2. Rebrandly - Free Plan - Just to hide the long unfriendly URL's returned by Webtor
3. Not really an API - We scrape the first search page of https://ext.torrentbay.to/

## API KEYS
API Keys have been removed for security. They are found on all the outer python files
1. Bot.py has the telegram bot api key -- Get that from bot father - Line 80
2. main.py has the rapid api key: Search for 'X-RapidAPI-Key' and give it your key
3. shorten.py has the rebrandly API key - make a free account to  obtain it

## Selenium
SLEZ is a class i wrote to make things simpler and easier. 
The search_torrents function inside of torrent_search/main is very important when running on windows vs an ubunutu server

In windows not much problems would occur. but in ubunutu:
- [x] make sure you are not the root user.
- [x] Make sure you do not run the bot in sudo mode
- [x] There is no need for a virtual display really
- [x] for any reason if you get an Error right after SLEZ starts the driver download, there is a chance that it did not complete it fully so it would be best to delete that manually

I have not used virtualenv but it is most recommended to start one. (for the whole project)

## INSTALLATION
the outer requirements.txt file has all you would need - so do a 

```python 
pip install -r requirements.txt
```

## RUNNING
The bot is not tested at all. There ~~maybe~~ definitely are a lot of problems that happen and a lot of improvements that can be done to improve the user-experience. That in mind, to run you just do a python3 bot.py
