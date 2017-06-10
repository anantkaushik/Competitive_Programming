/* HackerMan has brought a new drawing book for his child,which consists only of geometric shapes. 
Its consists of lessons where the child has to make drawings using the geometric shapes.
The first lesson is based on how to use squares to build different objects.
You are task is to help HackerMan in teaching one part of this lesson. You have to help him in determining, 
given S number of squares, how many distinct rectangles you can build out of that.
Two rectangles are considered different if none of them can be rotated and moved to obtain the second one. 
During rectangle construction, the child can neither deform the squares nor put any squares upon any other ones.
Note: All the squares are of the same configuration.
Input: There will be one line of input that will contain an integer N which represents the number of test cases, 
each subsequent line contains an integer S that represents the number of squares available.
Output:Each line should contain a single integer equal to the number of different rectangles that the child can form using the 
corresponding number of squares in that line of input.

SAMPLE INPUT
3
1
2
4

SAMPLE OUTPUT
1
2
5
*/
#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t>0){
        int n,count=0;
        scanf("%d",&n);
        for(int i=1;i<=n;i++){
            for(int j=i;j<=n;j++){
                if(i*j<=n)
                    count++;
                else 
                    break;
            }
        }
        printf("%d\n",count);
        t--;
    }
    return 0;
}