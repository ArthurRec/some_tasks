def water_volume(height: list) -> int:
    if len(height) < 3:
        return 0

    left_max: int = height[0]
    right_max: int = height[-1]
    left = 1
    right = len(height) - 2
    trapped_water = 0

    while left <= right:
        if left_max < right_max:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                trapped_water += left_max - height[left]
            left += 1

        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                trapped_water += right_max - height[right]
            right -= 1

    return trapped_water