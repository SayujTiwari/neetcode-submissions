class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        slowest_arrival = 0

        for pos, speed in cars:
            arrival_time = (target - pos) / speed

            if arrival_time > slowest_arrival:
                fleets += 1
                slowest_arrival = arrival_time
        
        return fleets



