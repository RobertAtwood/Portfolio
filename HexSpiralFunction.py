import math
import matplotlib.pyplot as plt

def generate_hex_spiral(sp_gap, ch_gap,side_length):
    """
    Generate points for a hexagonal spiral pattern.
    
    Parameters:
    sp_gap (float): Spiral gap in mm
    ch_gap (float): Channel gap in mm
    
    Returns:
    list: pointsArray containing (x, y) coordinates of the spiral
    """
    # Fixed parameters (can be made inputs if desired)
  # mm
    channel_depth = 0.125 * 25.4  # Convert inches to mm (unused in current logic)
    Hex_H = side_length * math.sin(math.radians(60))
    total_gap = ch_gap + sp_gap
    spiral_num = math.floor(Hex_H / total_gap)
    length_Add = total_gap / (6 * math.sin(math.radians(60)))
    L0 = L0 = total_gap*1.1  # mm
    x0 = L0
    y0 = 0
    Li = L0  # Initial segment length
    
    # Initialize points array
    pointsArray = [(0, 0), (x0, y0)]
    
    # Generate spiral points
    for xi in range(1, spiral_num):
        x1 = pointsArray[6 * (xi - 1) + 1][0]
        y1 = pointsArray[6 * (xi - 1) + 1][1]
        
        x2 = x1 - Li * math.cos(math.radians(60))
        y2 = y1 + Li * math.sin(math.radians(60))
        pointsArray.append((x2, y2))
        Li += length_Add
        
        x3 = x2 - Li
        y3 = y2
        pointsArray.append((x3, y3))
        Li += length_Add
        
        x4 = x3 - Li * math.cos(math.radians(60))
        y4 = y3 - Li * math.sin(math.radians(60))
        pointsArray.append((x4, y4))
        Li += length_Add
        
        x5 = x4 + Li * math.cos(math.radians(60))
        y5 = y4 - Li * math.sin(math.radians(60))
        pointsArray.append((x5, y5))
        Li += length_Add
        
        x6 = x5 + Li
        y6 = y5
        pointsArray.append((x6, y6))
        Li += length_Add
        
        x7 = x6 + Li * math.cos(math.radians(60))
        y7 = y6 + Li * math.sin(math.radians(60))
        pointsArray.append((x7, y7))
        Li += length_Add
    
    return pointsArray
