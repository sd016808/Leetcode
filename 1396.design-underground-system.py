#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.stationMap = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customers:
            self.customers[id] = {"startStation":[], "endStation":[]}
        
        self.customers[id]["startStation"].append((stationName, t))

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.customers[id]["startStation"][-1]
        if (start[0], stationName) not in self.stationMap:
            self.stationMap[start[0], stationName] = []

        self.stationMap[start[0], stationName].append(t - start[1])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.stationMap:
            return 0

        return sum(self.stationMap[(startStation, endStation)]) / len(self.stationMap[(startStation, endStation)])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

