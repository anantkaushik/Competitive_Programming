/* Given a number, write a program to find a maximum number that can be formed using all of the digits of this number.

Input:
The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. The first line of each test case contains the number N.

Output:
Print the largest number that can be formed using the digits of the given number. Print the answer for each test case in a new line.

Sample Input:
2
38293367
1203465

Sample Output:
98763332
6543210 
*/
#include<stdio.h>
#include<string.h>
int main(){
    int t;
    scanf("%d",&t);
    while ( t>0 ) {
        char s[1000000];
        long long int a[58],i;
        scanf("%s",s);
        for(i=0;i<58;i++)
            a[i]=0;
        for (i=0 ; i<strlen(s) ; i++ ) {
            a[s[i]]++;
        }
        int count = 9;
        for (int j=57 ; j>=47 ; j--) {
            if((a[j])>0);
                for(i=a[j] ; i>=1 ; i--)
                    printf("%d",count);
            count--;
        }
        printf("\n");
        t--;
    }
	return 0;
}