/*You are given a string S. Count the number of occurrences of all the digits in the string S.
Input: First line contains string S.
Output: For each digit starting from 0 to 9, print the count of their occurrences in the string S.
So,print 10 lines, each line containing 2 space separated integers. 
First integer i and second integer count of occurrence of i. See sample output for clarification. 

Sample Input:
77150
Sapmle Output:
0 1
1 1
2 0
3 0
4 0
5 1
6 0
7 2
8 0
9 0
*/
#include <stdio.h>
#include <string.h>
int main(){
   char s[100];
   gets(s);
   int i=0,a[10]={0};
   for(i=0;i<strlen(s);i++){
        a[s[i]-48]+=1;
   }
   for(i=0;i<10;i++){
       printf("%d %d\n",i,a[i]);
   }
    return 0;
}