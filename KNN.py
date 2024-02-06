import math
from collections import Counter
def euclidean_distance(vector1, vector2):
   squared_distance = sum((x - y)**2 for x, y in zip(vector1, vector2))
   distance = math.sqrt(squared_distance)
   return distance
class KNN:
    def __init__(self, k=3):
        self.k = k
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    def predict(self, X):
        y_pred = [self.predict1(x) for x in X]
        return y_pred
    def predict1(self, x):
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        k_indices = sorted(range(len(distances)), key=lambda i: distances[i])[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        common = Counter(k_nearest_labels).most_common(1)
        return common[0][0]
def enter_dataset():
    X_train = []
    y_train = []
    num_samples = int(input("enter num of samples in the dataset: "))
    for i in range(num_samples):
        sample = input(f"enter features of sample {i+1}: ").strip().split()
        X_train.append([float(feature) for feature in sample[:-1]])
        y_train.append(int(sample[-1]))
    return X_train, y_train
def main():
    X_train, y_train = enter_dataset()
    k = int(input("enter the value of k for k-NN: "))
    classifier = KNN(k=k)
    classifier.fit(X_train, y_train)
    num_test_samples = int(input("enter num of test samples: "))
    X_test = []
    for i in range(num_test_samples):
        sample = input(f"enter features of test sample {i+1}: ").strip().split()
        X_test.append([float(feature) for feature in sample])
    predictions = classifier.predict(X_test)
    print("predictions:", predictions)
if __name__ == "__main__":
    main()
