def quicksort(dataset, key):
    if len(dataset) <= 1:
        return dataset
    else:
        pivot = dataset[0]
        less = [x for x in dataset[1:] if x.get(key) <= pivot.get(key)]
        greater = [x for x in dataset[1:] if x.get(key) > pivot.get(key)]

        return quicksort(less, key) + [pivot] + quicksort(greater, key)
