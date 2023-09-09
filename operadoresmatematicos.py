a = 7
b = 2
c = 4
d = 14

# 1. A + B - C;
total = a + b - c
print(f"O total do item 1 é {total}")

# 2. A * B / C;
total = a * b / c
print(f"O total do item 2 é {total: .2f}")

# 3. C + 22 * D;
total = c + 22 / d
print(f"O total do item 3 é {total: .2f}")

# 4. A + B * C + D;
total = a+ b * c + d
print(f"O total do item 4 é {total}")

# 5. (A + B) * (C + D);
total = (a + b) * (c + d)
print(f"O total do item 5 é {total}")

# 6. (D / A) / (B / C);
total = (d / a) / (b / c)
print(f"O total do item 6 é {total: .2f}")

# 7. 10 ** A;
total = 10 ** a
print(f"O total do item 7 é {total}")

# 8. 58 % A;
total = 58 % a
print(f"O total do item 8 é {total}")

# 9. (A + B + C * D) / (B - C * (B - C))
total = (a + b + c * d) / (b - c * (b - c))
print(f"O total do item 9 é {total: .2f}")

# 10. (A + B + C * D) / (B - C * (B - C)) + 10 ** A
total = (a + b + c * d) / (b - c * (b - c)) + 10 ** a
print(f"O total do item 10 é {total: .2f}")
