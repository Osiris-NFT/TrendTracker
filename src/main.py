import requests
from fastapi import FastAPI
from classes.best_launch import BestLaunch

app = FastAPI()

if __name__ == '__main__':
    best_lauch = BestLaunch()
    # need to start threads if multiple scripts
    
    best_lauch.run()