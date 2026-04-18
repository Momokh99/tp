import time
import os
from typing import List, Optional

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_array(T, current_i: Optional[int] = None, j: Optional[int] = None, cle=None, highlight_indices: Optional[List] = None):
    if highlight_indices is None:
        highlight_indices = []
    
    max_val = max(T) if T else 1
    n = len(T)
    height = 15
    
    print("\n" + "=" * 50)
    print("          INSERTION SORT VISUALIZATION")
    print("=" * 50)
    print()
    
    for level in range(height, -1, -1):
        line = "    "
        for idx, val in enumerate(T):
            bar_height = int((val / max_val) * height)
            if bar_height >= level:
                if idx == current_i and (j is not None and idx == j + 1):
                    line += f"\033[92m█\033[0m  "
                elif idx == current_i:
                    line += f"\033[91m█\033[0m  "
                elif idx in highlight_indices or (current_i is not None and idx <= current_i):
                    line += f"\033[94m█\033[0m  "
                else:
                    line += f"█  "
            else:
                line += "   "
        print(line)
    
    print("    " + "-" * (len(T) * 4))
    
    indices = "    "
    values = "    "
    markers = "    "
    
    for idx, val in enumerate(T):
        indices += f"{idx}  "
        values += f"{val}  "
        
        if idx == current_i and (j is not None and idx == j + 1):
            markers += "↑  "
        elif idx == current_i:
            markers += "↓  "
        elif idx == j:
            markers += "↑  "
        else:
            markers += "   "
    
    print(indices)
    print(values)
    print(markers)
    
    if cle is not None:
        print(f"\n  cle = {cle}")
    if current_i is not None:
        print(f"  i = {current_i}")
    if j is not None:
        print(f"  j = {j}")
    
    print()

def tri_insert_visual(T):
    T = T.copy()
    n = len(T)
    
    clear_screen()
    print("\n" + "=" * 50)
    print("    📊 INSERTION SORT - STEP BY STEP")
    print("=" * 50)
    print(f"\n  Initial array: {T}")
    print("\n  Legend:")
    print("    \033[91m█\033[0m Red   = Current element (cle)")
    print("    \033[94m█\033[0m Blue  = Sorted portion")
    print("    \033[92m█\033[0m Green = Insertion position")
    input("\n  Press Enter to start...")
    
    for i in range(1, n):
        cle = T[i]
        j = i - 1
        
        clear_screen()
        print_array(T, current_i=i, j=j, cle=cle)
        print(f"\n  📍 Step {i}: Processing element at index {i}")
        print(f"     cle = {cle}")
        print(f"     Comparing with sorted portion [0..{i-1}]")
        input()
        
        while j >= 0 and T[j] > cle:
            clear_screen()
            print_array(T, current_i=i, j=j, cle=cle)
            print(f"\n  ⚡ Comparison: T[{j}] = {T[j]} > cle = {cle} ? YES")
            print(f"     Shifting T[{j}] = {T[j]} to position {j+1}")
            
            T[j + 1] = T[j]
            j -= 1
            
            print(f"\n  After shift: {T}")
            input()
        
        T[j + 1] = cle
        
        clear_screen()
        print_array(T, highlight_indices=list(range(j + 1, i + 1)))
        print(f"\n  ✅ Inserted {cle} at position {j + 1}")
        print(f"  Result: {T}")
        input()
    
    clear_screen()
    print("\n" + "=" * 50)
    print("    🎉 SORTING COMPLETE!")
    print("=" * 50)
    print(f"\n  Final sorted array: {T}")
    print()
    print("  █" * 15)
    for val in T:
        height = int((val / max(T)) * 10)
        bar = "█" * height
        print(f"  {bar} {val}")
    print("  ▔" * 15)
    print()

def tri_insert_fast(T):
    """Fast version without visualization for comparison"""
    T = T.copy()
    for i in range(1, len(T)):
        cle = T[i]
        j = i - 1
        while j >= 0 and T[j] > cle:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = cle
    return T

def demo_ascii_animation():
    """ASCII art animation showing the sorting process"""
    clear_screen()
    
    steps = [
        ("Initial", [12, 11, 13, 5, 6, 1]),
        ("Step 1: cle=11, compare 12>11 → shift", [12, 12, 13, 5, 6, 1]),
        ("Insert 11 at position 0", [11, 12, 13, 5, 6, 1]),
        ("Step 2: cle=13, 12>13? NO → stay", [11, 12, 13, 5, 6, 1]),
        ("Step 3: cle=5, shift 13,12,11", [11, 12, 12, 13, 6, 1]),
        ("Shift 12 → position 2", [11, 11, 12, 13, 6, 1]),
        ("Shift 11 → position 1", [5, 11, 12, 13, 6, 1]),
        ("Insert 5 at position 0", [5, 11, 12, 13, 6, 1]),
        ("Step 4: cle=6, shift 13,12,11", [5, 11, 12, 12, 13, 1]),
        ("Insert 6 at position 1", [5, 6, 11, 12, 13, 1]),
        ("Step 5: cle=1, shift all", [5, 6, 11, 12, 12, 13]),
        ("Insert 1 at position 0 → DONE!", [1, 5, 6, 11, 12, 13]),
    ]
    
    for title, arr in steps:
        clear_screen()
        print("\n" + "╔" + "═" * 48 + "╗")
        print("║         INSERTION SORT - ASCII ANIMATION         ║")
        print("╠" + "═" * 48 + "╣")
        print(f"║  {title:<46}  ║")
        print("╚" + "═" * 48 + "╝")
        print()
        
        max_val = max(arr)
        
        for level in range(13, -1, -1):
            line = "   "
            for val in arr:
                bar_height = int((val / max_val) * 13)
                if bar_height >= level:
                    line += "███ "
                else:
                    line += "    "
            print(line)
        
        print("   " + "┬".join(["───"] * len(arr)))
        print("   " + "│".join([str(v).center(3) for v in arr]))
        print()
        print(f"   Array: {arr}")
        print()
        
        time.sleep(0.8)

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("    📊 INSERTION SORT VISUALIZATION TOOL")
    print("=" * 50)
    print()
    print("  Choose mode:")
    print("    1. Interactive step-by-step (press Enter)")
    print("    2. Fast ASCII animation")
    print()
    print("  [12, 11, 13, 5, 6, 1]")
    print()
    
    choice = input("  Enter choice (1 or 2): ").strip()
    
    if choice == "2":
        demo_ascii_animation()
    else:
        tri_insert_visual([12, 11, 13, 5, 6, 1])
