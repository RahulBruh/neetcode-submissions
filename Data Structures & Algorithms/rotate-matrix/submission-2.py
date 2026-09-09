class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix)-1
        top, bottom = 0, len(matrix)-1

        while l < r:
            for i in range(r-l):

                topLeft = matrix[top][l+i]

                #change top left
                matrix[top][l+i] = matrix[bottom-i][l]

                # change bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                #change bottom right

                matrix[bottom][r-i] = matrix[top+i][r]

                #change top right, using save var
                matrix[top+i][r] = topLeft
            l += 1
            r -= 1
            top += 1
            bottom -= 1
        





