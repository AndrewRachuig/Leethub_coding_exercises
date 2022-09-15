class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(row):
            '''
            Checks for validity of a given input row.
            
            Parameters: row - a given row from a sudoku puzzle.
            
            Returns:    True if row is valid.
                        False if row is not valid.
            '''
            
            row =[i for i in row if i != "."]
            if len(row) == len(set(row)):
                pass
            else:
                return False
        
        columns = list(zip(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))
            
        def make_subbox(row, col):
            '''
            Makes a sub_box using the starting row and column position.

            Parameters: row - the index of the starting row
                        column - the index of the starting column

            Returns: a sub_box as a single one dimensional array.
            '''
            one_d_array = []
            for i in range(3):
                for j in range(3):
                    one_d_array.append(board[col+i][row+j])
            return one_d_array
        
        sub_boxes = [make_subbox(0,0), make_subbox(3,0), make_subbox(6,0),
                    make_subbox(0,3), make_subbox(3,3), make_subbox(6,3),
                    make_subbox(0,6), make_subbox(3,6), make_subbox(6,6)]
            
        for i in board:
            if check_row(i) == False:
                return False
            else:
                pass
            
        for i in columns:
            if check_row(i) == False:
                return False
            else:
                pass
            
        
        for i in sub_boxes:
            if check_row(i) == False:
                return False
            else:
                pass
                
        return True