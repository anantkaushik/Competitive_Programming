/* You have been given a String S.You need to find and print whether this string is a palindrome or not. 
If yes, print "YES" (without quotes), else print "NO" (without quotes).

Input Format: The first and only line of input contains the String S

Output Format: Print the required answer on a single line. 

Sample Input: aba
Sample Output: YES */
#include <stdio.h>
#include <string.h>
int main(){
    char s[100];
    int flag=1,l;
    scanf("%s",s);
    l=strlen(s);
    for(int i=0;i<=l;i++){
        if(s[i]!=s[strlen(s)-i-1]){
            flag=0;
            break;
        }
        l--;
    }
    if(flag==1)
        printf("YES");
    else
        printf("NO");
    return 0;
}