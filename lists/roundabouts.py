#Input Specification
#
#The standard input will contain 10 datasets. Each dataset begins with an integer N ( 2 ≤ N ≤ 700 ) , the number of routes.
#The next N lines each contain a series of integers describing a route.
#
#The first integer of each route description is the ID for the route. The second integer R ( 1 ≤ R ≤ 70 )
#is the number of roundabouts along the route. R integers follow which describe the diameter D ( 1 ≤ D ≤ 70 000 )
#of each roundabout along the route.
#Output Specification
#
#For each dataset, output the minimum roundabout diameter along a route followed by a brace-enclosed,
#sorted list of route IDs for the routes that could cause issues.



for i in range(10):
# Get the input
    n_routes = int(input())
    routes_dict = {}
    troubled_routes = []
    # Store the route_id and minimum diameter for each route in a dictionary
    for i in range(n_routes):
        line = input()
        line = list(map(int, line.split(' ')))
        route_id = line[0]
        routes_dict[route_id] = min(line[2:])
    # Find the minimum diameter across all routes
    overall_min = min(routes_dict.values())
    result = str(overall_min) + ' {'
    for route_id in routes_dict.keys():
        if routes_dict[route_id] == overall_min:
            troubled_routes.append(route_id)
    # sort the list of routes with a roundabout that has the min diameter
    troubled_routes.sort()
    for route_id in troubled_routes:
        result = result + str(route_id) + ','
    result = result[:-1] + '}'
    print(result)

