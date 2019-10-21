def findSum(n, r,c, lim, grid):
    for i in range(lim):
        for j in range(lim):
            if grid[r][i] + grid[j][c] == n: return True

    return False



def main():
    n = int(input())
    grid = []
    
    for i in range(n):
        grid.append([ int(n) for n in input().split()])
    
    
    for r in range(n):
        for c in range(n):
            if  grid[r][c] == 1: continue
            if not findSum(grid[r][c], r, c, n,grid):
                print("No")
                return
    print("Yes")

if __name__ == "__main__":
    main()