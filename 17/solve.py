from ortools.constraint_solver import pywrapcp

inputFile = open("input.txt").readlines()
points = [(float(i), float(u)) for i, u in [l.split(",") for l in inputFile]]
distanceMatrix = []

for (x1, y1) in points:
    distanceMatrix.append([((x1 - x2)**2 + (y1 - y2)**2)**0.5 for (x2, y2) in points])


def distance_callback(from_node, to_node):
    return distanceMatrix[from_node][to_node]


routing = pywrapcp.RoutingModel(len(points), 1, 0)
search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
routing.SetArcCostEvaluatorOfAllVehicles(distance_callback)
assignment = routing.SolveWithParameters(search_parameters)

index = routing.Start(0)
maxDist = 0
dist = 0

while not routing.IsEnd(index):
    prevIndex = index
    index = assignment.Value(routing.NextVar(index))
    dist += distanceMatrix[prevIndex][index % len(points)]
    maxDist = max(distanceMatrix[prevIndex][index % len(points)], maxDist)

print(round(dist - maxDist))
