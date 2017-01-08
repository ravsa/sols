#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std; 
#define N 9
bool sudoku(int grid[N][N]);

bool usedincol(int grid[N][N], int col, int num){
    for (int row = 0; row < N; row++)
        if(grid[row][col] == num)
            return true;
    return false;
}

bool usedinrow(int grid[N][N], int row, int num){
    for (int col = 0; col < N; col++)
        if(grid[row][col] == num)
            return true;
    return false;
}

bool usedinbox(int grid[N][N], int startrow, int startcol, int num){
    for (int row = 0; row < 3 ; row++)
        for (int col = 0; col < 3; col++)
            if(grid[startrow+row][startcol+col] == num)
                return true;
    return false;
}

bool is_safe(int grid[N][N], int row, int col, int num){
    return (!usedinrow(grid, row, num) && 
            !usedincol(grid, col, num) && 
            !usedinbox(grid, row - row%3, col - col%3, num));
}

int not_assigned(int grid[N][N], int &row, int &col){
    for (row  = 0; row  < N; row++ )
        for (col  = 0; col  < N; col++ )
            if(grid[row][col]==0)
                return true;
    return false;
}
bool sudoku(int grid[N][N]){
    int row, col;
    if(!not_assigned(grid, row, col))
        return true;
    for (int num = 1;num  <= 9; num++) {
        if(is_safe(grid, row, col, num)) {
            grid[row][col] = num;
        if(sudoku(grid))
            return true;
        grid[row][col] = 0;
        }
    }
    return false;
}
int static grid[N][N];
int main()
{
    grid[0][0] = 9;
    if(sudoku(grid))
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << grid[i][j] << "\t";
            }
            cout <<  endl;
        }
    return 0;
}
