import numpy as np
import tkinter as tk
from tkinter import messagebox
# initialize a 9x9 sudoku puzzle filled with zeros
sudoku = np.zeros((9,9), dtype=int)


# check if a number can be placed in a given row, column, and 3x3 box
def is_valid(row, col, num, sudoku):
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num or sudoku[3*(row//3)+i//3][3*(col//3)+i%3] == num:
            return False
    return True


# recursively solve the sudoku puzzle using backtracking
def solve(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(row, col, num, sudoku):
                        sudoku[row][col] = num
                        if solve(sudoku) is not None:
                            return sudoku
                        sudoku[row][col] = 0
                return None
    return sudoku


# solve a given sudoku puzzle using the solve() function
def sudoku_solver(sudoku):
    # check for duplicates in input puzzle
    for i in range(9):
      row = [sudoku[i][j] for j in range(9) if sudoku[i][j] != 0]
      col = [sudoku[j][i] for j in range(9) if sudoku[j][i] != 0]
      box = [sudoku[3*(i//3)+j//3][3*(i%3)+j%3] for j in range(9) if sudoku[3*(i//3)+j//3][3*(i%3)+j%3] != 0]
    
      if len(set(row)) != len(row) or len(set(col)) != len(col) or len(set(box)) != len(box):
            print("Invalid input puzzle: duplicate numbers detected.")
            sudoku = -1 * np.ones((9, 9), dtype=int)
            return sudoku
    
    # solve the puzzle
    solved = solve(sudoku)
    if solved is None:
        print("No solution exists.")
        sudoku = -1 * np.ones((9, 9), dtype=int)
        return sudoku
    else:
        return solved


def solve_button_click():
  # Get input from entry fields and convert to 2D array
  sudoku_input = []
  for i in range(9):
      row = []
      for j in range(9):
          value = entry_fields[i][j].get()
          if value == "":
              row.append(0)
          else:
              row.append(int(value))
      sudoku_input.append(row)

  # Solve Sudoku
  solved_sudoku = sudoku_solver(np.array(sudoku_input))

  # Update GUI with solution
  if np.array_equal(solved_sudoku, -1 * np.ones((9, 9), dtype=int)):
      messagebox.showerror("Error", "Invalid input puzzle: duplicate numbers detected.")
  elif np.array_equal(solved_sudoku, np.zeros((9, 9), dtype=int)):
      messagebox.showerror("Error", "No solution exists.")
  else:
      for i in range(9):
          for j in range(9):
              entry_fields[i][j].delete(0, tk.END)
              entry_fields[i][j].insert(0, str(solved_sudoku[i][j]))

# Reset and empty the all slot to 0
def reset_button_click():
  for i in range(9):
      for j in range(9):
          entry_fields[i][j].delete(0, tk.END)


def generate_easy_click():
  # Generate a random valid Sudoku puzzle (Easy version)
  puzzle = generate_easy_puzzle()

  # Update GUI with generated puzzle
  for i in range(9):
      for j in range(9):
          if puzzle[i][j] != 0:
              entry_fields[i][j].delete(0, tk.END)
              entry_fields[i][j].insert(0, str(puzzle[i][j]))
          else:
              entry_fields[i][j].delete(0, tk.END)


def generate_medium_click():
  # Generate a random valid Sudoku puzzle (Medium version)
  puzzle = generate_medium_puzzle()

  # Update GUI with generated puzzle
  for i in range(9):
      for j in range(9):
          if puzzle[i][j] != 0:
              entry_fields[i][j].delete(0, tk.END)
              entry_fields[i][j].insert(0, str(puzzle[i][j]))
          else:
              entry_fields[i][j].delete(0, tk.END)


def generate_hard_click():
  # Generate a random valid Sudoku puzzle (Hard version)
  puzzle = generate_hard_puzzle()

  # Update GUI with generated puzzle
  for i in range(9):
      for j in range(9):
          if puzzle[i][j] != 0:
              entry_fields[i][j].delete(0, tk.END)
              entry_fields[i][j].insert(0, str(puzzle[i][j]))
          else:
              entry_fields[i][j].delete(0, tk.END)


def generate_easy_puzzle():
  # Generate a easy Sudoku solution
  sudoku_solution = np.zeros((9, 9), dtype=int)
  solve(sudoku_solution)
  
  # Remove numbers to create a puzzle
  puzzle = sudoku_solution.copy()
  for _ in range(40):  # Adjust the number of cells to be cleared as per difficulty
      row, col = np.random.randint(9), np.random.randint(9)
      puzzle[row][col] = 0
  
  return puzzle


def generate_medium_puzzle():
# Generate a medium Sudoku solution
  sudoku_solution = np.zeros((9, 9), dtype=int)
  solve(sudoku_solution)
  
  # Remove numbers to create a puzzle
  puzzle = sudoku_solution.copy()
  for _ in range(75):  # Adjust the number of cells to be cleared as per difficulty
      row, col = np.random.randint(9), np.random.randint(9)
      puzzle[row][col] = 0
  
  return puzzle


def generate_hard_puzzle():
# Generate a hard Sudoku solution
  sudoku_solution = np.zeros((9, 9), dtype=int)
  solve(sudoku_solution)
  
  # Remove numbers to create a puzzle
  puzzle = sudoku_solution.copy()
  for _ in range(140):  # Adjust the number of cells to be cleared as per difficulty
      row, col = np.random.randint(9), np.random.randint(9)
      puzzle[row][col] = 0
  
  return puzzle


# Create GUI
root = tk.Tk()
root.title("Sudoku Solver")

entry_fields = []
for i in range(9):
  row_entries = []
  for j in range(9):
      entry = tk.Entry(root, width=3)
      entry.grid(row=i, column=j)
      row_entries.append(entry)
  entry_fields.append(row_entries)

solve_button = tk.Button(root, text="Solve", command=solve_button_click)
solve_button.grid(row=9, column=3, columnspan=2)

reset_button = tk.Button(root, text="Reset", command=reset_button_click)
reset_button.grid(row=9, column=6, columnspan=2)

generate_label = tk.Label(root, text="Generate:")
generate_label.grid(row=10, column=0, columnspan=2)

generate_easy = tk.Button(root, text="Easy", command=generate_easy_click)
generate_easy.grid(row=10, column=2, columnspan=2)

generate_medium = tk.Button(root, text="Medium", command=generate_medium_click)
generate_medium.grid(row=10, column=4, columnspan=3)

generate_hard = tk.Button(root, text="Hard", command=generate_hard_click)
generate_hard.grid(row=10, column=7, columnspan=2)

root.mainloop()