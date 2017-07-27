/* Given a string S , write a program to check if all the characters of the string are same or not.
Input:
The first line of input contains a single integer T which denotes the number of test cases. Then T test cases follows. 
First line of each test case contains a string S.
Output:
For each test case print "YES" without quotes if all the characters of the string S are same otherwise print "NO".

Sample Input:
2
geeks
gggg

Sample Output:
NO
YES  */
#include <stdio.h>
#include <string.h>
int main() {
	int t;
	scanf("%d",&t);
	while(t>0){
	    char s[10000];
	    scanf("%s",s);
	    int flag=0;
	    for(int i=1 ; i<strlen(s) ; i++) {
	        if(s[i]!=s[0]){
	            flag=1;
	            break;
	        }
	    }
	    printf("%s\n",(flag>0?"NO":"YES"));
	    t--;
	}
	return 0;
}