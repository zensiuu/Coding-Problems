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


def render_bars(array, label='', key_idx=-1, shift_idx=-1):
    max_val = max(array) if array else 1
    width = os.get_terminal_size().columns
    bar_max = max(8, min(18, width // 2 - 10))
    if label:
        print(f'\n  {BOLD}{CYAN}{label}{RESET}')
    for idx, val in enumerate(array):
        bar_len = int((val / max_val) * bar_max) if max_val else 0
        bar = '█' * bar_len
        if idx == key_idx:
            marker, color = f'{BOLD}{GREEN}▶{RESET} ', f'{BOLD}{GREEN}'
        elif idx == shift_idx:
            marker, color = f'{BOLD}{YELLOW}◀{RESET} ', f'{BOLD}{YELLOW}'
        else:
            marker, color = '  ', get_color(idx)
        print(f'  {marker}{color}{bar}{RESET} {WHITE}{val:>4}{RESET}')


def get_user_array():
    print(f'\n  {BOLD}{BLUE}╔{"═" * 54}╗{RESET}')
    print(f'  {BOLD}{BLUE}║{RESET}  {CYAN}Insertion Sort Visualizer{RESET}{" " * 27}{BOLD}{BLUE}║{RESET}')
    print(f'  {BOLD}{BLUE}╚{"═" * 54}╝{RESET}\n')
    while True:
        raw = input(f'  {BOLD}{YELLOW}?{RESET} Enter numbers (comma-separated): ').strip()
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
            print(f'  {RED}✗{RESET} Invalid numbers. Use commas: 8,3,5,1\n')


def insertion_sort_visual(arr):
    n = len(arr)
    print(f'\n  {BOLD}{BLUE}Starting:{RESET}  {BOLD}[{" ".join(str(x) for x in arr)}]{RESET}')
    input(f'\n  {BOLD}{GREEN}▶{RESET} Press Enter to begin... ')
    clear_screen()

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        print(f'\n  {BOLD}{YELLOW}Step i = {i}{RESET}  {DIM}key = {key}, sorted = [0…{j}]{RESET}')
        render_bars(arr, f'Before placing key = {key}', key_idx=i)
        time.sleep(0.4)

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            print(f'  {DIM}arr[{j}] ({arr[j]}) > key → shift right{RESET}')
            render_bars(arr, f'Shifting ...', key_idx=i, shift_idx=j)
            time.sleep(0.3)
            j -= 1

        arr[j + 1] = key
        render_bars(arr, f'Placed key = {key} at [{j + 1}]', key_idx=j + 1)
        time.sleep(0.5)

    return arr


def main():
    clear_screen()
    arr = get_user_array()
    sorted_arr = arr[:]
    insertion_sort_visual(sorted_arr)
    print(f'\n  {BOLD}{GREEN}╔{"═" * 54}╗{RESET}')
    print(f'  {BOLD}{GREEN}║{RESET}  {WHITE}✓ SORTED{RESET}{" " * 43}{BOLD}{GREEN}║{RESET}')
    print(f'  {BOLD}{GREEN}║{RESET}  {BOLD}[{" ".join(str(x) for x in sorted_arr)}]{RESET}{" " * 30}{BOLD}{GREEN}║{RESET}')
    print(f'  {BOLD}{GREEN}╚{"═" * 54}╝{RESET}')
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

def insertionSort(array):

    for i in range(1, len(array)):

        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:

            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array


# =============================================================
#  HINTS for the simplified version
# =============================================================
#
#  Pretend you're sorting a hand of playing cards:
#
#    1. The left side (indices 0 … i-1) is always SORTED.
#    2. Pick the next unsorted card:  key = array[i]
#    3. Slide left while you see cards BIGGER than key —
#       shift each one right to make room.
#    4. Drop key into the empty spot you just opened.
#
#  Variable roles:
#    i   =  boundary between sorted (left) and unsorted (right)
#    key =  the element we are placing right now
#    j   =  walks leftwards, comparing and shifting
#
#  Trace:  [8, 3, 5, 1]
#    i=1  key=3  shift 8→  place 3 → [3, 8, 5, 1]
#    i=2  key=5  shift 8→  place 5 → [3, 5, 8, 1]
#    i=3  key=1  shift 8,5,3→ place 1 → [1, 3, 5, 8]
#
#  Best case (already sorted): O(n)
#  Worst case (reversed):      O(n²)
#  Great for small or nearly-sorted data.
# =============================================================
