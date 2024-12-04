files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip() for x in f.readlines()]
    grid= {(y, x): c for y, line in enumerate(data) for x, c in enumerate(line)}

def run(grid):
    ds = [(dy,dx) for dy in [-1,0,1] for dx in [-1,0,1] if (dx!=0 or dy!=0)]
    pos = ["MS", "SM"]
    p1 = p2 = 0

    for y,x in grid:
        words = []
        if grid[(y,x)] == 'A':
            ld = grid.get((y+1, x+1), '') + grid.get((y-1, x-1), '')
            rd = grid.get((y-1, x+1), '') + grid.get((y+1, x-1), '')
            p2 += ld in pos and rd in pos
        if grid[(y,x)] == 'X':
            for dx, dy in ds:
                word = "".join(grid.get((y+i*dy, x+i*dx), '') for i in range(len('XMAS')))
                p1 += word =='XMAS'        
    return p1, p2

print("Part 1&2: ", run(grid))