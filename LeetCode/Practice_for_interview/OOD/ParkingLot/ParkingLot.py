'''
1. parking spots, compact, large, handicap
2. park, exit
3. ticket of the parking lot for drivers.
4. calculate the fee 
5. cannot exceed the capacity

'''



# from abc import ABC, abstractmethod


class ParkingLot:
    def __init__(self) -> None:
        # self.capacity = capacity
        self.compact_mp = {}
        self.large_mp = {}
        self.handicap_mp = {}
        self.ticket_mp = {}
        self.compact_spot = 100
        self.large_spot = 100
        self.handicap_spot = 100
    
    def enterParkingLot(self, type):
        if self.checkFull(type):
            raise Exception("Full capacity!")
        
        parkSpot = self.getParkingSpot(type)
        parkSpot.park(self, parkSpot)
        
        ticket = Tickets()
        ticket.setEnter



    def exitParkingLot(self):
        pass
    
    def checkFull(self, type):
        if type == 'Large':
            return self.large_spot <= 0 
        elif type == 'handicap_spot':
            return self.handicap_spot <= 0
        else:
            raise Exception("Invalid type")


    def getParkingSpot(self, type):
        return HandicapSpot()





class ParkingSpot():
    def __init__(self):
        pass
    
    def park(self, parkingLot: ParkingLot, parkSpot: CompactSpot):
        pass



    


class CompactSpot(ParkingSpot):
    def __init__(self):
        super().__init__()

class LargeSpot(ParkingLot):
    def __init__(self):
        super().__init__()

class HandicapSpot(ParkingLot):
    def __init__(self):
        super().__init__()



class RiatioStrategy:
    def __init__(self) -> None:
        pass
    def apply(self):
        pass

class StandardStrategy(RiatioStrategy):
    def __init__(self) -> None:
        self.hourlyRatio = 10

    def apply(self, duration):
        return self.hourlyRatio * duration

class HolidayStrategy(RiatioStrategy):
    def __init__(self) -> None:
        self.hourlyRatio = 0

    def apply(self, duration):
        # return self.hourlyRatio * duration
        return 0
        

class Tickets:
    def __init__(self, enterTime, type, strategy: RiatioStrategy) -> None:
        self.enterTime = enterTime
        self.endTime = None
        self.type = type
        self.stratgy = strategy

    def calculateRatio(self):
        duration = self.endTime - self.enterTime
        return self.stratgy.apply(duration)




