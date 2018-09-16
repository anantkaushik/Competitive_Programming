/* Jack is awesome. His friends call him little Einstein. To test him, his friends gave him a string. 
They told him to add the string with its reverse string and follow these rules:
Every ith character of string will be added to every ith character of reverse string.
Both string will contain only lower case alphabets(a-z).
Eg:- a+a=b,a+c=d,z+a=a (Refer to sample test cases for more details)

Input: First line contains a value N denoting number of test cases. Next N lines contains string str.
Output: For every string str output the string that Jack's friends wants from him.

Sample Input: 
4
hello
codeapocalypse
programming
world

Sample Output:
wqxqw
hhtdmqrrqmdthh
wfxtebetxfw
aajaa   */
#include <stdio.h>
#include <string.h>
int main(){
    int t;
    scanf("%d",&t);
    for(int j=0;j<t;j++){
        char s[100000];
        int sum=0,l;
        scanf("%s",s);
        l=strlen(s);
        for(int i=0;i<l;i++){
            sum=s[i]+ s[l-1-i]-192;
            if(sum>26)
                sum-=26;
            printf("%c",sum+96);
        }
        printf("\n");
    }
    return 0;
}