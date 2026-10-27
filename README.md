# AI & Prompt Engineering - Module 2: AI-Assisted Programming

Small practice repository for the Module 2 assignments. Each folder is self-contained
and can be run with only Python 3.10+ and (for the C files) `gcc`.

## Structure

| Folder | Contents |
|---|---|
| `c_programs/` | Original C programs: factorial, Fibonacci, struct-based student records |
| `python/` | The same three programs converted to Python |
| `leetcode/` | Two Easy LeetCode solutions: Two Sum (#1), Valid Parentheses (#20) |
| `debugging/` | A buggy gradebook script, the fixed version, and unit tests |
| `.cursorrules` | Project rules for the Cursor IDE |

## Running

```bash
# C programs
gcc -Wall -Wextra c_programs/factorial.c -o factorial && ./factorial

# Python conversions
python python/factorial.py
python python/fibonacci.py
python python/student_struct.py

# LeetCode solutions (each file runs its own asserts)
python leetcode/two_sum.py
python leetcode/valid_parentheses.py

# Debugging exercise: tests pass on the fixed module
cd debugging && python -m unittest -v test_gradebook
# ...and fail on the buggy one
GRADEBOOK=buggy_gradebook python -m unittest test_gradebook
```

## The debugging exercise

`buggy_gradebook.py` has five bugs: division by zero on an empty list, a mutable default
argument, exclusive grade boundaries (`>` instead of `>=`), an off-by-one loop in
`highest()`, and removing items from a list while iterating over it. The 12 tests in
`test_gradebook.py` fail on the buggy version (5 failures, 2 errors) and all pass on
`gradebook.py`.

## AI usage

Code, this README and the commit messages were drafted with an AI assistant and then
run and checked locally. Output of the C and Python versions was compared and matches
(only a trailing space differs in the Fibonacci line).
