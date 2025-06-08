def backtrack(weights, capacity, start, bins, min_bins) -> int:
    if start == len(weights):
        min_bins = min(min_bins, len(bins))
        return bins, min_bins
    
    for i in range(len(bins)):
        if bins[i] + weights[start] <= capacity:
            bins[i] += weights[start]
            bins, min_bins = backtrack(weights, capacity, start + 1, bins, min_bins)
            bins[i] -= weights[start] 
    
    bins.append(weights[start])
    bins, min_bins = backtrack(weights, capacity, start + 1, bins, min_bins)
    bins.pop()
    return bins, min_bins


def bin_packing_subset(weights, capacity) -> int:
    min_bins = float("inf")
    bins = []
    bins, min_bins = backtrack(weights, capacity, 0, bins, min_bins)
    return min_bins

    

if __name__ == "__main__":
    print(bin_packing_subset([4, 5, 2, 1, 3], 6)) #? Expected 3