gridSizeX = 8
gridSizeY = gridSizeX

origin = (0.15, 0.15)
distanceX = 0.15
distanceY = distanceX

print("opacha_level_code#map_name:none#game_rules:normal false#general:small#planets:", end="")

for x in range(gridSizeX):
    for y in range(gridSizeY):
        print(f"neutral empty 3 {round(origin[0] + distanceX * x, 3)} {round(origin[1] + distanceY * y, 3)},", end="")
        
print("#links:", end="")

for x in range(gridSizeX):
    for y in range(gridSizeY):
        
        # orthogonal connections
        if (x < gridSizeX - 1):
            print(f"neutral {round(origin[0] + distanceX * x, 3)} {round(origin[1] + distanceY * y, 3)} {round(origin[0] + distanceX * (x + 1), 3)} {round(origin[1] + distanceY * y, 3)},", end="")
        if (y < gridSizeY - 1):
            print(f"neutral {round(origin[0] + distanceX * x, 3)} {round(origin[1] + distanceY * y, 3)} {round(origin[0] + distanceX * x, 3)} {round(origin[1] + distanceY * (y + 1), 3)},", end="")
            
        # angled connections
        if (x < gridSizeX - 1 and y < gridSizeY - 1):
            print(f"neutral {round(origin[0] + distanceX * x, 3)} {round(origin[1] + distanceY * y, 3)} {round(origin[0] + distanceX * (x + 1), 3)} {round(origin[1] + distanceY * (y + 1), 3)},", end="")
        if (x > 0 and x < gridSizeX and y < gridSizeY - 1):
            print(f"neutral {round(origin[0] + distanceX * x, 3)} {round(origin[1] + distanceY * y, 3)} {round(origin[0] + distanceX * (x - 1), 3)} {round(origin[1] + distanceY * (y + 1), 3)},", end="")
            
print("#")
