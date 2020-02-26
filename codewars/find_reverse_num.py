def reverse(n):
    reverse = 0
    def find_rev(n, reverse):
        if n <= 0:
            return reverse
        else:
            reverse = (reverse * 10) + (n%10)
            new_n = n // 10
            return find_rev(new_n, reverse)
    return find_rev(n, reverse)

print(reverse(1234))

