def binary_serach(arr, key, low, high):
  if high >= low:
    mid = (low + high) // 2
    if arr[mid] == key:
      print(key, 'found at', mid)
      return
    elif arr[mid] > key:
      return binary_serach(arr, key, low, mid)
    else:
      return binary_serach(arr, key, mid + 1, high)
  else:
    print(key, 'not found')

if __name__ == "__main__":
  arr = list(map(int, input('Enter your array: ').split()))
  arr.sort()
  key = int(input('Enter your key: '))
  binary_serach(arr, key, 0, len(arr) - 1)