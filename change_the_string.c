/* Given a string S, the task is to change the string according to the condition; If the first letter in a string is capital letter then change 
the full string to capital letters, else change the full string to small letters.
Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a string S.
Output:
For each test case, print the changed string in a new line.

Sample Input:
2
geEkS
FoR
Sample Output:
geeks
FOR
*/
#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while ( t>0 ) {
        char s[10000];
        scanf("%s",s);
        for ( int i=0 ; s[i]!='\0' ; i++){
            if (s[0]<91) {
                if (s[i]>90) 
                    s[i]-=32;
            }
            else {
                if (s[i]<91)
                    s[i]+=32;
            }
        }
        printf("%s\n",s);
        t--;
    }
	return 0;
}