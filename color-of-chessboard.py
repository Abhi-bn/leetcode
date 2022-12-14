class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        both = list(coordinates)
        a = ord(both[0]) - 96
        b = int(both[1])
        if a % 2 == 0 and b % 2 == 1:
            return True
        if a % 2 == 1 and b % 2 == 0:
            return True
        return False
