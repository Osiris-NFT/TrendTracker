import os
#### GENERAL ####
"""
# DEBUG
VOLUME_PATH = "data"
PUBLICATION_SVC_URL = "http://0.0.0.0:8000/"
"""
VOLUME_PATH = os.environ["VOLUME_PATH"]
PUBLICATION_SVC_URL = os.environ["PUBLICATION_SVC_URL"]

PUBLICATION_SVC_GET_RECENT_ENDPOINT = "/trend_tracker_get_recent_publications"
PUBLICATION_SVC_GET_MANY_ENDPOINT = "/trend_tracker_get_many_publications"

#### BEST LAUNCH ####
BL_UPDATE_OCCURENCE = 1 # HOUR(S)
BL_PUB_TIME = 3 # HOUR(S)