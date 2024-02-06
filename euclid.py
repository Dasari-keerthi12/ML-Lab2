import math
def euclidean_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors should have the same dimension")
    squared_distance = sum((x - y)**2 for x, y in zip(vector1, vector2))
    distance = math.sqrt(squared_distance)
    return distance
def manhattan_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors should have the same dimension")
    distance = sum(abs(x - y) for x, y in zip(vector1, vector2))
    return distance
def enter_vector():
    vector_str = input("Enter a vector as numbers: ")
    vector = [float(x) for x in vector_str.split()]
    return vector
vec_1 = enter_vector()
vec_2 = enter_vector()
euclidean_dist = euclidean_distance(vec_1, vec_2)
manhattan_dist = manhattan_distance(vec_1, vec_2)
print(f"Euclidean Distance: {euclidean_dist}")
print(f"Manhattan Distance: {manhattan_dist}")
