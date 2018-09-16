/* Find the area of a triangle with all its three sides given as a,b and c. 
Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains three space-separated integers a,b and c.
Output:
Output the area of the triangle answer with a precision of 6 decimal places.The area is to be printed as 0.000000 if the triangle does not exist.

Sample Input:
2
2 2 3
3 4 5
Sample Output:
1.984313
6.000000
*/
#include <stdio.h>
#include <math.h>
int main() {
	int t;
	scanf("%d",&t);
	while(t>0){
	    double a,b,c,p,area;
	    scanf("%lf %lf %lf",&a,&b,&c);
	    p=(a+b+c)/2;
	    area=sqrt(p*(p-a)*(p-b)*(p-c));
	    printf("%lf\n",(area>=0?area:0.000000));
	    t--;
	}
	return 0;
}