/* You are given a string whose length is even, and each character of the string is either 'a', 'b' or '/' 
Your task is to replace each occurrence of '/' in string with either 'a' or 'b' such that the string becomes a palindrome.
You are also given two integers, aCost and bCost. Replacing '/' with 'a' costs aCost, and replacing '/' with 'b' costs bCost.
Return the minimum cost of replacing '/' by 'a' and 'b' such that the string turns into a palindrome. 
If it is impossible to obtain a palindrome, return -1.
Input Format: First line of input will contain the number of test cases. For each test case, there will be of three lines, 
the first line is the string whose palindrome is to be constructed, the second is the aCost and the third is the bCost
Example:
1
aba/bab/
4
6
Returns: 10
The only way to produce a palindrome is to replace 4th character of string with 'b' and 8th character with 'a'. 
The first replacement costs 4, the second costs 6, so the total cost is 4+6=10.

SAMPLE INPUT
1
baba//aaa/ab//
72
23

SAMPLE OUTPUT
213
*/
#include <stdio.h>
#include <string.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t>0){
        char s[10000],temp;
        scanf("%s",s);
        int ac,bc;
        long int l,sum=0;
        l=strlen(s);
        scanf("%d %d",&ac,&bc);
        for(int i=0;i<l/2;i++){
            if(s[i]=='/' || s[l-i-1]=='/'){
                if(s[i]=='/')
                    temp=s[l-i-1];
                else
                    temp=s[i];
                switch(temp){
                    case 'a':
                        sum+=ac;
                        break;
                    case 'b':
                        sum+=bc;
                        break;
                    case '/':
                        sum+=2*(ac<bc?ac:bc);
                        break;
                }
            }
            else if(s[i]!=s[l-i-1]){
                sum=-1;
                break;
            }
        }
        printf("%ld\n",sum);
        t--;
    }
    return 0;
}