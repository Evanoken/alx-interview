def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    copy = 1  # Number of characters currently in the clipboard
    total = 1  # Total number of characters in the file

    while total < n:
        # Check if n is divisible by the current total, if so, update the copy count
        if n % total == 0:
            copy = total
        total += copy  # Paste the characters from the clipboard to the file
        operations += 1  # Increment the operations count

    return operations
