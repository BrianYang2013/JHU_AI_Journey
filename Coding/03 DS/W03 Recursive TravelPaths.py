num_cities = 3
city_names = []
distances = []

def travel_paths(curr_path, need_to_visit):
    if len(curr_path) == num_cities:  # Base case: Visited all cities
        total_distance = 0
        for i in range(len(curr_path)):
            print(city_names[curr_path[i]], '  ', end=' ')

            if i > 0:
                total_distance += distances[curr_path[i-1]][curr_path[i]]

        print('=', total_distance)
    else:  # Recursive case: Travel to each city
        for i in range(len(need_to_visit)):
            # Visit city
            city = need_to_visit[i]
            need_to_visit.pop(i)
            curr_path.append(city)

            travel_paths(curr_path, need_to_visit)

            need_to_visit.insert(i, city)
            curr_path.pop()

distances.append([0])
distances[0].append(960)  # Boston-Chicago
distances[0].append(2960) # Boston-Los Angeles
distances.append([960])   # Chicago Boston
distances[1].append(0)
distances[1].append(2011) # Chicago-Los Angeles
distances.append([2960])  # Los Angeles-Boston
distances[2].append(2011) # Los Angeles-Chicago
distances[2].append(0)

city_names = ["Boston", "Chicago", "Los Angeles"]

path = []
need_to_visit = [0, 1, 2] # (Need to visit all 3 cities)
travel_paths(path, need_to_visit)