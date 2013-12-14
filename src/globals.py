import logging

inf = logging.info
war = logging.warning
err = logging.error
cri = logging.critical

SHARDS_PER_COUNTER = 10
MC_CACHE_TIME = 2419200 #seconds (28 days)
DS_CACHE_TIME = 90 #days

MIN_ICON_LENGTH = 100
MAX_ICON_LENGTH = 200000
EMPTY_ICON_LENGTH = 1150

ICON_MIMETYPES = [
  "image/x-icon",
  "image/vnd.microsoft.icon",
  "image/ico",
  "image/icon",
  "text/ico",
  "application/ico",
  "image/x-ms-bmp",
  "image/x-bmp",
  "image/gif",
  "image/png",
  "image/jpeg",
  None,
]

ICON_MIMETYPE_BLACKLIST = [
  "application/xml",
  "text/html",
]

# Surpresses the index and test pages
HEADLESS = False

COUNTERS = [
  "favIconsServed",
  "favIconsServedDefault",
  "cacheNone",
  "cacheMC",
  "cacheDS",
]

IPHONE_IOS7 = "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53"
CHROME_MAC = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
