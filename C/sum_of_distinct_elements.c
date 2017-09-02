/* Given an array of n elements such that every element of array is an integer in the range 1 to n, find the sum of all the distinct elements of the array.
Input:
First line consists of T test cases. First line of every test case consists of N. Second line of every test case consists of elements of Array.
Output:
Single line output, print the sum of distinct element of array.

Sample Input:
2
5
1 2 3 3 4
5
1 1 1 2 2
Sample Output:
10
3
*/
#include <stdio.h>
int main() {
	int t;
	scanf("%d",&t);
	while(t>0){
	    int n;
	    scanf("%d",&n);
	    int i,a[n],b[n],sum=0;
	    for(i=0;i<=n;i++)
	        b[i]=0;
	    for(i=0;i<n;i++){
	        scanf("%d",&a[i]);
	        b[a[i]]++;
	        if(b[a[i]]==1)
	            sum+=a[i];
	    }
	    printf("%d\n",sum);
	    t--;
	}
	return 0;
}