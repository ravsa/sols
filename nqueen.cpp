#include <cstdio>
#include <iostream>
#define N 8
using namespace std;

void printSolution(char board[N][N])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
            cout << board[i][j]<<'\t';
        cout << endl;
    }
}

bool is_safe(char board[N][N], int row, int col){
    int i, j;
    for (i = 0; i < col; ++i) {
        if(board[row][i]!='_')
            return false;
    }
    for (i=row, j=col; i>=0 && j>=0; --i, --j){
        if(board[i][j]!='_')
            return false;
    }
    for (i=row, j=col; i<N && j>=0;++i, --j){
        if(board[i][j]!='_')
            return false;
    }
    return true;
}

bool qsolve(char board[N][N], int col){
    if(col>=N)
        return true;
    for (int i = 0; i < N; ++i) {
        if(is_safe(board, i, col)){
            board[i][col] = 'q';
            if(qsolve(board, col+1))
                return true;
            board[i][col] = '_';
        }
    }
    return false;
}

int main()
{
    static char board[N][N];
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            board[i][j] = '_';
        }
    }
    qsolve(board, 0);
    printSolution(board);
    return 0;
}
