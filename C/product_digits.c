//Program to find the product of the digits present in the string.
/*
Sample Testcases Input:
2_1
abc2_a_3

Sample Testcases Output:
2
6
*/

#include <stdio.h>
#include <string.h>
void main(){
	char s[100];
    int l,i,c=0;
    long long int p=1;
    scanf("%[^\n]s",s);
    l=strlen(s);
    for(i=0;i<l;i++){
        if(s[i]>47 && s[i]<58){
            p=p*(s[i]-48);
            c=1;
        }
    }
    if(c==1)
        printf("%lld",p);
    else if(c==0)
        printf("%d",0);
}