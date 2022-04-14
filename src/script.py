from classes.best_launch import BestLaunch


if __name__ == '__main__':
    best_launch = BestLaunch()
    # need to start threads if multiple scripts
    while True:
        best_launch.run()