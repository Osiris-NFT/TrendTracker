import os

#### GENERAL ####
VOLUME_PATH = os.environ["VOLUME_PATH"]
PUBLICATION_SVC_URL = "http://" + os.environ["PUBLICATION_SVC_URL"]
PUBLICATION_SVC_PORT = os.environ["PUBLICATION_SVC_PORT"]

PUBLICATION_SVC_GET_RECENT_ENDPOINT = "/trend_tracker_get_recent_publications"
PUBLICATION_SVC_GET_MANY_ENDPOINT = "/trend_tracker_get_many_publications"

#### BEST LAUNCH ####
BL_UPDATE_OCCURRENCE = 1  # HOUR(S)
BL_PUB_TIME = 3  # HOUR(S)
SECONDS_TO_SLEEP_OFFSET = 1  # SECOND(S)
