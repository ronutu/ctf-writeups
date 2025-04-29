def is_palindrom(num: int) -> bool:
    return str(num) == str(num)[::-1]


max_pal = 0
best_a = best_b = 0

for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        prod = a * b
        if prod <= max_pal:
            break
        if is_palindrom(prod):
            max_pal, best_a, best_b = prod, a, b
            break

print(f"Maximum palindromic product: {max_pal} = {best_a} × {best_b}")