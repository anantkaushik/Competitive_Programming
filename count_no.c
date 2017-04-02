// Given a string S , find the total count of numbers present in the digit.
/*INPUT:
The first line contains T , the number of test cases. 
The first line of each and every testc ase will contain a integer N , 
the length of the string . The second line of each and every test case will contain a string S of length N.

OUTPUT:
For each and every testcase , output the total count of numbers present in the string.*/

/*Sample Input:
1
26
sadw96aeafae4awdw2wd100awd

Sample Output:4

Explanation:For the first test case , the string given is "sadw96aeafae4awdw2wd100awd". 
			There are total of 4 numbers in the string - [96,4,2,100]. So , we output 4.*/

#include <stdio.h>

int main(){
    int tcase,l,i,count,j;
    scanf("%d",&tcase);
    while(tcase>0){
        count=0;
        scanf("%d",&l);
        char s[l];
        scanf("%s",s);
        for(i=0;i<l;i++){
            if(s[i]>=48 && s[i]<=57){
                for(j=i;j<l;j++){
                    if(s[j]>=97 && s[j]<=122){
                        count++;
                        i=j;
                        break;
                    }
                    else if(i==l-1)
                        count++;
                }
            }
        }
        printf("%d\n",count);
        tcase--;
    }
    return 0;
}