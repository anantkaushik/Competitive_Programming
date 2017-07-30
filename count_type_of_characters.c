/* Given a string S, write a program to count the occurrence of Lowercase characters, Uppercase characters, Special characters and Numeric values in the string.

Input:
First line of input contains a single integer T which denotes the number of test cases. Then T test cases follows. First line of each 
test case contains a string S.
Output:
For each test case, print four lines. In the first line print the count of upper case letters, in the second line print the count of 
lower case letters, in the third line print the count of numbers and in the fourth line print the count of special characters present in the string S.
Note: The strings doesnot contains whitespaces.

Sample Input:
2
#GeeKs01fOr@gEEks07
*GeEkS4GeEkS*
Sample Output:
5
8
4
2
6
4
1
2
*/
#include <stdio.h>
#include <string.h>
int main() {
	int t;
	scanf("%d",&t);
	while(t>0){
	    char s[100000];
	    scanf("%s",s);
	    int lc=0,uc=0,sc=0,nc=0;
	    for (int i=0; i<strlen(s); i++){
	        if(s[i]>=65 && s[i]<=90)
	            uc++;
	        else if(s[i]>=48 && s[i]<=57)
	            nc++;
	        else if(s[i]>=97 && s[i]<=122)
	            lc++;
	        else
	            sc++;
	    }
	    printf("%d \n%d \n%d \n%d \n",uc,lc,nc,sc);
	    t--;
	}
	return 0;
}