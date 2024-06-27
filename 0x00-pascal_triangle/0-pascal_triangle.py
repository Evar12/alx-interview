def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: ./0-pascal_triangle.py <n>")
    else:
        n = int(sys.argv[1])
        print(pascal_triangle(n))