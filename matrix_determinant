def determinant(matrix):
    deter_ans = 0
    
    if(len(matrix) == 1):
        return matrix[0][0]

    else:
        for i in range(len(matrix)):
            new_matrix = []
            for j in range(1, len(matrix)):
                row = []
                for k in range(len(matrix)):
                    if(k!=i):
                        row.append(matrix[j][k])
                new_matrix.append(row)
            if(i%2 == 0):
                deter_ans += determinant(new_matrix)*matrix[0][i]
            else:
                deter_ans -= determinant(new_matrix)*matrix[0][i]
    return deter_ans
