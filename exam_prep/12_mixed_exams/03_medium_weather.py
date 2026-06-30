"""
MIXED EXAMS - MEDIUM 2: Weather Data Analysis
Hint: combine arrays + files + records

A file "temperatures.txt" has daily temperatures, one per line:
  22.5
  24.0
  19.5
  ...

Write a function analyze_temps(filename) that returns a dict with:
  - "min": minimum temperature
  - "max": maximum temperature
  - "avg": average temperature (float)
  - "above_avg_count": number of days above average

If file is empty, return {}.

Examples:
  analyze_temps("temps.txt") -> {"min":19.5,"max":24.0,"avg":22.0,...}
"""

def analyze_temps(filename):
    pass


if __name__ == "__main__":
    import os
    fname = "_test_temps.txt"
    with open(fname, "w") as f:
        f.write("22.5\n24.0\n19.5\n")
    result = analyze_temps(fname)
    assert result["min"] == 19.5
    assert result["max"] == 24.0
    assert result["avg"] == (22.5+24.0+19.5)/3
    assert result["above_avg_count"] == 1
    os.remove(fname)
    print("All tests passed!")
