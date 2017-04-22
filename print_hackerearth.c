/* As a beginner to the programming,Mishki came to Hackerearth platform,to become a better programmer. 
She solved some problems and felt very confident.Later being a fan of Hackerearth,she gave a problem to her friends to solve. 
They will be given a string containing only lower case characters (a-z),and they need to find that 
by using the characters of the given string, how many times they can print "hackerearth"(without quotes). 
As they are new to programming world, please help them.

Input:
The first line will consists of one integer N
denoting the length of string.
Next line will contain the string Str
containing only lower case characters.

Output:
Print one integer, denoting the number of times her friends can print "hackerearth" (without quotes). 

Sample Input:
13
aahkcreeatrha

Sample Output:
1
*/
#include <stdio.h>
int main(){
    int n,h=0,a=0,c=0,k=0,e=0,r=0,t=0,count=0;
    scanf("%d",&n);
    char s[n];
    scanf("%s",s);
    for(int i=0;i<n;i++){
        if(s[i]=='h')
            h++;
        else if(s[i]=='a')
            a++;
        else if(s[i]=='c')
            c++;
        else if(s[i]=='k')
            k++;
        else if(s[i]=='e')
            e++;
        else if(s[i]=='r')
            r++;
        else if(s[i]=='t')
            t++;
    }
    while(h>=2 && a>=2 && c>=1 && k>=1 && e>=2 && r>=2 && t>=1){
        h-=2;
        a-=2;
        c-=1;
        k-=1;
        e-=2;
        r-=2;
        t-=1;
        count++;
    }
    printf("%d",count);
    return 0;
}
