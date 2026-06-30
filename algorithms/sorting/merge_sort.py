import os
import sys
import time

os.system('')

RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
BLUE = '\033[94m'
WHITE = '\033[97m'
RED = '\033[91m'


def get_color(i):
    pal = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    return pal[i % len(pal)]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def render_bars(array, label='', highlight=None):
    max_val = max(array) if array else 1
    width = os.get_terminal_size().columns
    bar_max = max(8, min(20, width // 2 - 10))
    if label:
        print(f'\n  {BOLD}{CYAN}{label}{RESET}')
    for idx, val in enumerate(array):
        bar_len = int((val / max_val) * bar_max) if max_val else 0
        bar = '█' * bar_len
        color = get_color(idx)
        marker = f'  {BOLD}{color}▶ {RESET}' if (highlight and idx in highlight) else f'  {DIM}  {RESET}'
        print(f'{marker}{color}{bar}{RESET} {BOLD}{WHITE}{val:>4}{RESET}')


def print_split(array, mid):
    print(f'\n  {BOLD}{MAGENTA}  ✂ SPLIT  {RESET}{DIM}mid = {mid}{RESET}')
    render_bars(array[:mid], 'left')
    render_bars(array[mid:], 'right')


def print_merge(left, right, merged):
    print(f'\n  {BOLD}{GREEN}  ◆ MERGE  {RESET}{DIM}{left} ⊕ {right}{RESET}')
    render_bars(left, 'left')
    render_bars(right, 'right')
    render_bars(merged, '→ merged')


def merge_sort_visual(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_part = array[:mid]
    right_part = array[mid:]
    time.sleep(0.4)
    print_split(array, mid)
    sorted_left = merge_sort_visual(left_part)
    sorted_right = merge_sort_visual(right_part)
    i = j = k = 0
    merged = []
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] <= sorted_right[j]:
            merged.append(sorted_left[i])
            i += 1
        else:
            merged.append(sorted_right[j])
            j += 1
        k += 1
    while i < len(sorted_left):
        merged.append(sorted_left[i])
        i += 1
        k += 1
    while j < len(sorted_right):
        merged.append(sorted_right[j])
        j += 1
        k += 1
    time.sleep(0.4)
    print_merge(sorted_left, sorted_right, merged)
    return merged


def get_user_array():
    print(f'\n  {BOLD}{BLUE}╔{"═" * 50}╗{RESET}')
    print(f'  {BOLD}{BLUE}║{RESET}  {CYAN}Merge Sort Visualizer{RESET}{" " * 30}{BOLD}{BLUE}║{RESET}')
    print(f'  {BOLD}{BLUE}╚{"═" * 50}╝{RESET}\n')
    while True:
        raw = input(f'  {BOLD}{YELLOW}?{RESET} Enter comma-separated numbers: ').strip()
        if not raw:
            print(f'  {RED}✗{RESET} Input cannot be empty.\n')
            continue
        try:
            parts = raw.replace('，', ',').split(',')
            arr = [int(p.strip()) for p in parts if p.strip()]
            if len(arr) < 2:
                print(f'  {RED}✗{RESET} Enter at least 2 numbers.\n')
                continue
            return arr
        except ValueError:
            print(f'  {RED}✗{RESET} Invalid numbers. Use commas: 9,3,7,1,5\n')


def main():
    clear_screen()
    array = get_user_array()
    print(f'\n  {BOLD}{YELLOW}╔{"═" * 50}╗{RESET}')
    print(f'  {BOLD}{YELLOW}║{RESET}  {WHITE}Starting Merge Sort on:{RESET}  {BOLD}[{" ".join(str(x) for x in array)}]{RESET}  {BOLD}{YELLOW}║{RESET}')
    print(f'  {BOLD}{YELLOW}╚{"═" * 50}╝{RESET}')
    input(f'\n  {BOLD}{GREEN}▶{RESET} Press Enter to start... ')
    clear_screen()
    sorted_arr = merge_sort_visual(array)
    print(f'\n  {BOLD}{GREEN}╔{"═" * 50}╗{RESET}')
    print(f'  {BOLD}{GREEN}║{RESET}  {WHITE}✓ SORTED{RESET}{" " * 39}{BOLD}{GREEN}║{RESET}')
    print(f'  {BOLD}{GREEN}║{RESET}  {BOLD}[{" ".join(str(x) for x in sorted_arr)}]{RESET}{" " * 26}{BOLD}{GREEN}║{RESET}')
    print(f'  {BOLD}{GREEN}╚{"═" * 50}╝{RESET}')
    render_bars(sorted_arr, 'final')
    print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n  {RED}✗{RESET} Interrupted.\n')
        sys.exit(0)













# =============================================================
#  SIMPLIFIED VERSION  (no visuals, just the algorithm)
# =============================================================

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


# =============================================================
#  HINTS for the simplified version
# =============================================================
#
#  SPLIT → SORT → MERGE
#
#  1. Split the array in half recursively until each piece has
#     one element (a single element is always sorted).
#
#  2. On the way back up, merge each pair of sorted halves by
#     comparing the front of each and picking the smaller value.
#
#  Variable roles:
#    i  =  current index in left  half
#    j  =  current index in right half
#    k  =  where the next element goes in the original array
#
#  The first while does the main compare-and-pick work.
#  The last two whiles catch whatever is left over when one
#  side runs out.
#
#  Trace:  merge_sort([6, 2, 8, 1])
#    split → [6, 2]  [8, 1]
#    split → [6] [2] [8] [1]
#    merge → [2, 6] [1, 8]
#    merge → [1, 2, 6, 8]
# =============================================================
