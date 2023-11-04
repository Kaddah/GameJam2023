
class Level:
    def __init__(self, level_data: dict):
        self.waypoints = []
        for waypoint in level_data["waypoints"]:
            self.waypoints.append((waypoint["x"], waypoint["y"]))


    def getWaypoints(self):
        waypoints = []
        return self.waypoints

