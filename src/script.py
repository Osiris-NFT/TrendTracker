import requests
from classes.best_launch import BestLaunch
if __name__ == '__main__':
    best_lauch = BestLaunch()
    # need to start threads if multiple scripts
    while True:
        best_lauch.run()