def make_it_zero():
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])  
    index = 1
    results = []

    for _ in range(t):
        n = int(data[index])  
        index += 1
        a = list(map(int, data[index:index + n])) 
        index += n

        if n % 2 == 0:  
            results.append("2")           
            results.append(f"1 {n}")      
            results.append(f"1 {n}")      
        else:
            results.append("4")
            results.append(f"1 {n - 1}")
            results.append(f"1 {n - 1}")
            results.append(f"{n - 1} {n}")
            results.append(f"{n - 1} {n}")

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    make_it_zero()