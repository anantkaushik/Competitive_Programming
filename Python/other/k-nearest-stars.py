"""
Given coordinates of stars in a galaxy and coordinate of planet. 
Find the nearest K stars to the given planet. Assume the number of stars are large.
coordinate - (x, y, z)
"""
def find_nearest_stars(planet, stars, K):
    if not stars:
        return []

    heap = []

    for star in stars:
        d = calculate_distance(planet, star)
        if len(heap) < K:
            heapq.heappush(heap, (-d, star))
        else:
            heapq.heappushpop(heap, (-d, star))

    res = []
    for _, star in heap:
        res.append(star)

    return res


def calculate_distance(planet, star):
    return math.sqrt((planet[0] - star[0]) ** 2 + (planet[1] - star[1]) ** 2 + (planet[2] - star[2]) ** 2)
