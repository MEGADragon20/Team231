def survivedRobotsHealths(positions: list[int], healths: list[int], directions: str) -> list[int]:
    while True:
        lastone = ""
        for i in directions:
            if lastone != i and lastone != "":
                return healths
            lastone = i
    



        for i in range(len(positions)):
            for j in range(len(positions)):
                if positions[i-1] == positions[j-1] and i != j:
                    if healths[i-1] > healths[j-1]:
                        healths[i-1] -= 1
                        healths.pop(j-1)
                        positions.pop(j-1)
                        directions.pop(i-1)

                    
            if directions[i] == "L":
                positions[i] -= 1
            elif directions[i] == "R":
                positions[i] += 1
            

survivedRobotsHealths(positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR")