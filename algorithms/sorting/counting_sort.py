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


def print_count_table(count_arr, highlight=None):
    max_c = max(count_arr) if count_arr else 1
    print(f'\n  {BOLD}{CYAN}Count array:{RESET}')
    header = '  idx:'
    bar_line = '  bar:'
    val_line = '  val:'
    for i in range(len(count_arr)):
        c = count_arr[i]
        col = get_color(i) if c > 0 else DIM
        marker = f'{BOLD}{GREEN}▶{RESET}' if highlight == i else '   '
        header += f' {col}{i:>3}{RESET}'
        bar_line += f' {col}{"█" * min(c, 6):>3}{RESET}'
        val_line += f' {col}{c:>3}{RESET}'
    print(f'  {marker}{header}')
    print(f'     {bar_line}')
    print(f'     {val_line}')


def get_user_array():
    print(f'\n  {BOLD}{BLUE}╔{"═" * 54}╗{RESET}')
    print(f'  {BOLD}{BLUE}║{RESET}  {CYAN}Counting Sort Visualizer{RESET}{" " * 28}{BOLD}{BLUE}║{RESET}')
    print(f'  {BOLD}{BLUE}╚{"═" * 54}╝{RESET}\n')
    while True:
        raw = input(f'  {BOLD}{YELLOW}?{RESET} Enter non-negative integers (comma-separated): ').strip()
        if not raw:
            print(f'  {RED}✗{RESET} Input cannot be empty.\n')
            continue
        try:
            parts = raw.replace('，', ',').split(',')
            arr = [int(p.strip()) for p in parts if p.strip()]
            if any(v < 0 for v in arr):
                print(f'  {RED}✗{RESET} Counting sort needs non-negative numbers.\n')
                continue
            if len(arr) < 2:
                print(f'  {RED}✗{RESET} Enter at least 2 numbers.\n')
                continue
            return arr
        except ValueError:
            print(f'  {RED}✗{RESET} Invalid numbers. Use commas: 2,5,3,0,2\n')


def count_sort_visual(arr):
    n = len(arr)
    maxval = max(arr)

    print(f'\n  {BOLD}{MAGENTA}PHASE 1{RESET} — Count frequencies\n')
    cntArr = [0] * (maxval + 1)
    for v in arr:
        cntArr[v] += 1
        print(f'  value {BOLD}{v}{RESET} → cnt[{v}] = {BOLD}{cntArr[v]}{RESET}')
        print_count_table(cntArr, v)
        time.sleep(0.2)

    print(f'\n  {BOLD}{MAGENTA}PHASE 2{RESET} — Prefix sums (cumulative positions)\n')
    for i in range(1, maxval + 1):
        old = cntArr[i]
        cntArr[i] += cntArr[i - 1]
        print(f'  cnt[{i}] = {old} + {cntArr[i - 1]} = {BOLD}{cntArr[i]}{RESET}')
        print_count_table(cntArr, i)
        time.sleep(0.2)

    print(f'\n  {BOLD}{MAGENTA}PHASE 3{RESET} — Place elements (right to left, stable)\n')
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        v = arr[i]
        pos = cntArr[v] - 1
        print(f'  arr[{i}] = {v}  →  ans[{pos}] = {v}  (cnt[{v}] was {cntArr[v]}, now {cntArr[v] - 1})')
        ans[pos] = v
        cntArr[v] -= 1
        time.sleep(0.25)

    return ans


def main():
    clear_screen()
    arr = get_user_array()
    print(f'\n  {BOLD}{YELLOW}╔{"═" * 54}╗{RESET}')
    print(f'  {BOLD}{YELLOW}║{RESET}  {WHITE}Input:{RESET}  {BOLD}[{" ".join(str(x) for x in arr)}]{RESET}          {BOLD}{YELLOW}║{RESET}')
    print(f'  {BOLD}{YELLOW}║{RESET}  {WHITE}Range:{RESET}  0 to {BOLD}{max(arr)}{RESET}                    {BOLD}{YELLOW}║{RESET}')
    print(f'  {BOLD}{YELLOW}╚{"═" * 54}╝{RESET}')
    input(f'\n  {BOLD}{GREEN}▶{RESET} Press Enter to start... ')
    clear_screen()
    sorted_arr = count_sort_visual(arr)
    print(f'\n  {BOLD}{GREEN}╔{"═" * 54}╗{RESET}')
    print(f'  {BOLD}{GREEN}║{RESET}  {WHITE}✓ SORTED{RESET}{" " * 43}{BOLD}{GREEN}║{RESET}')
    print(f'  {BOLD}{GREEN}║{RESET}  {BOLD}[{" ".join(str(x) for x in sorted_arr)}]{RESET}{" " * 30}{BOLD}{GREEN}║{RESET}')
    print(f'  {BOLD}{GREEN}╚{"═" * 54}╝{RESET}')
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

def count_sort(arr):
    if not arr:
        return []

    n = len(arr)
    maxval = max(arr)

    cntArr = [0] * (maxval + 1)

    for v in arr:
        cntArr[v] += 1

    for i in range(1, maxval + 1):
        cntArr[i] += cntArr[i - 1]

    ans = [0] * n
    for i in range(n - 1, -1, -1):
        v = arr[i]
        ans[cntArr[v] - 1] = v
        cntArr[v] -= 1

    return ans


# =============================================================
#  HINTS for the simplified version
# =============================================================
#
#  Phase 1 — COUNT
#    For each value v in the input, do  cnt[v] += 1.
#    Now cnt[v] = "v appears this many times".
#
#  Phase 2 — PREFIX SUM
#    Turn cnt into cumulative counts:  cnt[i] += cnt[i - 1].
#    Now cnt[v] = "last position of v in sorted output + 1".
#
#  Phase 3 — PLACE (right-to-left = stable)
#    For each value v (reading input BACKWARDS):
#      pos = cnt[v] - 1      ← where v goes
#      ans[pos] = v
#      cnt[v] -= 1            ← so the next same value gets the slot left of it
#
#  Trace:  [2, 5, 3, 0, 2]
#    cnt = [1, 0, 2, 1, 0, 1]
#    cnt = [1, 1, 3, 4, 4, 5]
#    place:  2→ans[2], 0→ans[0], 3→ans[3], 5→ans[4], 2→ans[1]
#    result: [0, 2, 2, 3, 5]
#
#  Only works with non-negative integers.
#  Time = O(n + k)  where k = max value.
# =============================================================
