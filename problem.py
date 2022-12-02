#include<bits/stdc++.h>
using namespace std;
int boards[11][11];
bool isPossible(int row,int col,int n)
{
    //Same column
    for(int i=row-1;i>=0;i--)
    {
        if(boards[i][col]==1)
        return false;
    }
    //Upper Left diagonal
    for(int i=row-1,j=col-1;i>=0&&j>=0;i--,j--)
    {
        if(boards[i][j]==1)
        return false;
    }
    //Upper right diagonal
    for(int i=row-1,j=col+1;i>=0&&j<n;i--,j++)
    {
        if(boards[i][j]==1)
        return false;
    }
    return true;
}
void nQueensPlaced(int n,int row)
{
    //Base Condition
    if(row==n)
    {
        //if my row becomes equal to n that means all the queens have been placed on right positions
        //Now you have to just print them
        //And return
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            cout<<boards[i][j]<<" ";
        }
        cout<<endl;
    }
    for(int j=0;j<n;j++)
    {
        if(isPossible(row,j,n))
        {
            boards[row][j]=1;
            nQueensPlaced(n,row+1);
            boards[row][j]=0;
        }
    }
    return;
}
int main()
{
    int n;
    cin>>n;
    nQueensPlaced(n,0);
}