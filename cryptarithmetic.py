from constraint import Problem, AllDifferentConstraint

def solve_cryptarithmetic(puzzle):
    problem = Problem()

    # Extract unique letters from the puzzle
    letters = set(puzzle.replace(' ', ''))

    # Add variables and their domains
    for letter in letters:
        problem.addVariable(letter, range(10))  # Each letter can be 0-9

    # Convert the words to integers
    words = puzzle.split()
    for word in words[:-2]:
        problem.addConstraint(AllDifferentConstraint(), [c for c in word])  # All letters in a word must be different

    # Add constraint for the sum
    addend1 = words[-3]
    addend2 = words[-2]
    sum_result = words[-1]
    problem.addConstraint(lambda a, b, s: a + b == s, [addend1[0], addend2[0], sum_result[0]])

    # Solve the problem
    solutions = problem.getSolutions()

    # Return the first solution
    if solutions:
        return solutions[0]
    else:
        return None

# Example of usage:
puzzle = "SEND + MORE = MONEY"
solution = solve_cryptarithmetic(puzzle)
if solution:
    print("Solution found:")
    print(solution)
else:
    print("No solution found.")
