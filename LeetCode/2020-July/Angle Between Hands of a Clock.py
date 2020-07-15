class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ONE_BLOCK = 6        
        ang_m = minutes * ONE_BLOCK
        ONE_QUARTER = 30
        percentage = minutes/60
        ang_h = hour * ONE_QUARTER + ONE_QUARTER * percentage

        res = ( 360-abs(ang_h-ang_m) if abs(ang_h-ang_m)>180 else abs(ang_h-ang_m))
