/*Given an array of n values. Print a number which had maximum number of zeroes. If their are no zeroes then print -1.
Note: If there are multiple numbers with same (max) number of zeroes then print the Maximum number among them.
Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case consists of an integer n. 
The next line consists of n spaced integers.
Output:
Print the number with maximum number of zeroes.

Sample Input:
1
5
10 20 3000 9999 200
Sample Output:
3000
*/
#include <stdio.h>
int main() {
	int t;
	scanf("%d",&t);
	while(t>0){
	    int n;
	    scanf("%d",&n);
	    int a[n],max=0,temp,count,index;
	    for(int i=0;i<n;i++){
	        scanf("%d",&a[i]);
	        temp=a[i];
	        count=0;
	        while(temp>0){
	            if(temp%10==0)
	                count++;
	            temp=temp/10;
	        }
	        if(count>max){
	            max=count;
	            index=i;
	        }
	        else if(count==max){
	            if(a[i]>a[index])
	                index=i;
	        }
	    }
	    printf("%d\n",(max>0?a[index]:-1));
	    t--;
	}
	return 0;
}