import datetime
import os
import json
import requests
from .settings import *
import time

class BestLaunch:
    last_update: datetime
    next_uptade: datetime


    def __init__(self):
        try:
            os.makedirs(VOLUME_PATH)
        except FileExistsError:
            pass
        if not self._data_exist():
            print("Not data found, requesting publications and setting up next update...")
            self._get_recent_publications()
        else:
            print("Data found, setting up next update...")
        self._set_next_update()
        print("BestLauch init done.")


    def _data_exist(self) -> bool:
        if os.path.exists(os.path.join(VOLUME_PATH, "best_launch_old.json")):
            return True
        else:
            return False
    
    
    def _set_next_update(self):
        now = datetime.datetime.now()
        self.next_uptade = datetime.datetime(now.year, now.month, now.day, now.hour, 0, 0, 0) + datetime.timedelta(hours=BL_UPDATE_OCCURENCE)
        print("Next update set for:" + str(self.next_uptade))

    def _get_recent_publications(self):
        result = requests.get(PUBLICATION_SVC_URL + PUBLICATION_SVC_GET_RECENT_ENDPOINT, {'hours_time_delta': BL_PUB_TIME})
        file = json.loads(result.text)
        print("Init data for next update, number of publications: " +str(len(file)))
        with open(os.path.join(VOLUME_PATH, "best_launch_old.json"), 'w') as f:
            f.write(json.dumps(file))
            f.close()
    
    
    def _get_many_publications(self, old_json: dict):
        param: str = ""
        i=0
        for key in old_json.keys():
            if i > 0:
                param += ","+key
            else:
                param += key
            i+=1
        result = requests.get(PUBLICATION_SVC_URL + PUBLICATION_SVC_GET_MANY_ENDPOINT, {'id_list_str': param})
        return json.loads(result.text)


    def _load_recent_publications(self) -> dict:
        with open(os.path.join(VOLUME_PATH, "best_launch_old.json"), 'r') as f:
            json_file = json.load(f)
        return json_file


    def _parse_best_launch(self):
        old_json = self._load_recent_publications()
        new_json = self._get_many_publications(old_json)
        dif = {}
        for key in old_json.keys():
            if key in new_json.keys():
                dif[key] = new_json[key] - old_json[key]
        
        sorted_dif = dict(sorted(dif.items(), key=lambda x: x[1]))
        data_to_store = []

        for key in sorted_dif.keys():
            data_to_store.append(key)
        data_to_store.reverse()
    
        with open(os.path.join(VOLUME_PATH, "best_launch_result.json"), 'w') as f:
            f.write(json.dumps({"best_launch": data_to_store}))
        print("Data parsed and list of best launched publications stored.")


    def run(self):
        delta = self.next_uptade - datetime.datetime.now()
        time_to_sleep = delta.seconds
        print("Time to sleep until next update: " + str(time_to_sleep) + " seconds.")
        #time.sleep(time_to_sleep)
        self._parse_best_launch()
        self._get_recent_publications()
        self._set_next_update()