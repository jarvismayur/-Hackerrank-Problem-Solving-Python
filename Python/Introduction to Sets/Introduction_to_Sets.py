def average(array):
    # your code goes here
    plant_set = set(array)
    avg = sum(plant_set) / len(plant_set)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)