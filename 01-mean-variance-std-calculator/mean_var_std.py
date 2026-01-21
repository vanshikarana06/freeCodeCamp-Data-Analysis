import numpy as np

def calculate(list):
    # 1. Check if the input list has exactly 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # 2. Convert the list into a 3x3 Numpy array
    # This aligns with the matrix operations you'll see in GATE CSE math
    matrix = np.array(list).reshape(3, 3)

    # 3. Calculate metrics along Axis 0 (Columns), Axis 1 (Rows), and Flattened
    # .tolist() is used because the project requires standard Python lists
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(), 
            matrix.mean(axis=1).tolist(), 
            matrix.mean()
        ],
        'variance': [
            matrix.var(axis=0).tolist(), 
            matrix.var(axis=1).tolist(), 
            matrix.var()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(), 
            matrix.std(axis=1).tolist(), 
            matrix.std()
        ],
        'max': [
            matrix.max(axis=0).tolist(), 
            matrix.max(axis=1).tolist(), 
            matrix.max()
        ],
        'min': [
            matrix.min(axis=0).tolist(), 
            matrix.min(axis=1).tolist(), 
            matrix.min()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(), 
            matrix.sum(axis=1).tolist(), 
            matrix.sum()
        ]
    }

    return calculations