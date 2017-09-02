/* Today, Monk went for a walk in a garden. There are many trees in the garden and each tree has an English alphabet on it. 
While Monk was walking, he noticed that all trees with vowels on it are not in good state. He decided to take care of them. 
So, he asked you to tell him the count of such trees in the garden.
Note : The following letters are vowels: 'A', 'E', 'I', 'O', 'U' ,'a','e','i','o' and 'u'.

Input: The first line consists of an integer T denoting the number of test cases.
	   Each test case consists of only one string, each character of string denoting the alphabet 
	   (may be lowercase or uppercase) on a tree in the garden.
Output: For each test case, print the count in a new line.

SAMPLE INPUT:
2
nBBZLaosnm
JHkIsnZtTL

SAMPLE OUTPUT:
2
1

Explanation: In test case 1, a and o are the only vowels. So, count=2 */
#include <stdio.h>
#include <string.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t>0){
        char a[100000];
        int l,count=0;
        scanf("%s",a);
        l=strlen(a);
        for(int i=0;i<l;i++){
            if(a[i] =='A' || a[i] =='E' || a[i] =='I' || a[i] =='O' || a[i] =='U')
                count++;
            else if(a[i] =='a' || a[i] =='e' || a[i] =='i' || a[i] =='o' || a[i] =='u')
                count++;
        }
        printf("%d\n",count);
        t--;
    }
    return 0;
} 