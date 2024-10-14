
def mean(numbers):

    return sum(numbers) / len(numbers)  # Return the mean value.

def median(numbers):

    numbers.sort()

    if len(numbers) % 2 == 0:
        median1 = numbers[len(numbers) // 2]  # The higher index of the two middle values.
        median2 = numbers[len(numbers) // 2 - 1]  # The lower index of the two middle values.
        mymedian = (median1 + median2) / 2  # Average of the two middle values.
    else:
        mymedian = numbers[len(numbers) // 2]  # The middle value for lists with an odd number of elements.

    # Return the calculated median value.
    return mymedian