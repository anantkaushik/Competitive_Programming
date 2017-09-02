/* Akash and Vishal are quite fond of travelling. They mostly travel by railways. 
They were travelling in a train one day and they got interested in the seating arrangement of their compartment. 
The compartment looked something like: 
LINK: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/ 

So they got interested to know the seat number facing them and the seat type facing them. The seats are denoted as follows :
Window Seat : WS
Middle Seat : MS
Aisle Seat : AS
You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.

INPUT: First line of input will consist of a single integer T denoting number of test-cases. 
Each test-case consists of a single integer N denoting the seat-number.

OUTPUT: For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.
Sample Input: 
2
18
40
Sample Output:
19 WS
45 AS */
#include <stdio.h>
int main(){
    int t,n,i,temp;
    scanf("%d",&t);
    while(t>0){
        scanf("%d",&n);
        temp=n%12;
        switch(temp){
            case 0: 
                n-=11;
                printf("%d WS\n",n);
                break;
            case 1:
                n+=11;
                printf("%d WS\n",n);
                break;
            case 2:
                n+=9;
                printf("%d MS\n",n);
                break;
            case 3:
                n+=7;
                printf("%d AS\n",n);
                break;
            case 4:
                n+=5;
                printf("%d AS\n",n);
                break;
            case 5:
                n+=3;
                printf("%d MS\n",n);
                break;
            case 6:
                n+=1;
                printf("%d WS\n",n);
                break;
            case 7:
                n-=1;
                printf("%d WS\n",n);
                break;
            case 8:
                n-=3;
                printf("%d MS\n",n);
                break;
            case 9:
                n-=5;
                printf("%d AS\n",n);
                break;
            case 10:
                n-=7;
                printf("%d AS\n",n);
                break;
            case 11:
                n-=9;
                printf("%d MS\n",n);
                break;
        }
        t--;
    }
    return 0;
}
