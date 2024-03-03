def repeatedly_converting_to_from_numpy_arrays():
    nums = list(range(256 * 256 * 256))
    arr = np.array(nums)  # 1.01s

    m = max(nums)  # .16s
    m = np.max(arr)  # .01s
    m = arr.max()  # .01s
    m = max(arr)  # .73s
