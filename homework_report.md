# Homework - Laboratory 4

## Objective

The objective was to detect, test and automatically
fix bugs using three AI skills:
- bug-finder
- test-writer
- bug-fixer

## Results

| Function | Difficulty | Bug | Before fix | After fix |
|---|---|---|---|---|
| is_even | Very easy | Wrong operator | FAIL | PASS |
| is_adult | Easy | Boundary condition | FAIL | PASS |
| calculate_average | Medium | Division by zero | FAIL | PASS |
| remove_duplicates | Medium-hard | Order preservation | FAIL | PASS |
| binary_search | Hard | Incorrect loop condition | FAIL | PASS |

## Observations

- All 5 bugs were identified automatically.
- 4 out of 5 generated tests initially detected the bugs.
- The remove_duplicates test required manual correction.
- The bug-fixer skill repaired the functions based on
  the bug reports.

## Conclusion

The AI skills successfully identified and repaired
all five bugs. All five tests passed after the fixes.
The experiment also showed that AI-generated tests
sometimes require human verification.
