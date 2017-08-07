/* Given a binary string of 0 and 1, write a program to check that the given string is valid or not. The given string is valid when there is 
no zero is present in between 1’s. For example, 1111, 0000111110, 1111000 are valid strings but 01010011, 01010, 101 are not.

Input:
First line of input contains a single integer T which denotes the number of test cases. Then T test cases follows. 
First line of each test case contains a binary string.
Output:
For each test case print "VALID" without quotes if the string is valid otherwise print "INVALID" without quotes if the string is invalid.

Sample Input:
3
100
1110001
00011
Sample Output:
VALID
INVALID
VALID
*/
#include <stdio.h>
#include <string.h>
int main() {
	int t;
	scanf("%d",&t);
	while(t>0){
	    char s[100000];
	    int count1=0,count0=0,flag=0;
	    scanf("%s",s);
	    for ( int i=0 ; i<strlen(s) ; i++){
	        if( s[i]==49 && count1==0 ){
	            count1=1;
	            flag=1;
	        }
	        else if ( s[i]==48 && count1==1 )
	            count0=1;
	        else if( s[i]==49 && count1==1 && count0==1 )
	            count1=2;
	    }
	    if ( count1==1 || flag==0 )
	        printf("VALID\n");
	    else
	        printf("INVALID\n");
	    t--;
	}
	return 0;
}