/* Yes, you read it right - Little Jhool is back, but no, he's not over his break up, still. And he's sad, broken and depressed; thus, he decided 
to visit a psychologist. She tells him to think about his pleasant memories of childhood, and stay busy so as to not miss his ex-girlfriend.
She asks him about his favorite memories from childhood, and being the genius Mathematician Little Jhool is, he remembered that solving Mathematics 
problem given to him by his teacher was his favorite memory.
He had two types of notebooks, when he was a kid.
*10 problems could be solved in one page, in the first notebook.
*12 problems could be solved in one page, in the second notebook.
Little Jhool remembered how in order to maintain symmetry, if he was given with n problems in total to solve, he tore out pages from both notebooks, 
so no space was wasted. EVER!But, now he's unable to solve his own problem because of his depression, and for the exercise of the week, 
he has to answer the queries asked by his psychologist.Given n number of questions, print the minimum number of pages he needs to tear out from the 
combination of both the notebooks, so that no space is wasted.
Input Format:
The first line will contain t- number of test cases.The second will contain an integer n- number of questions.
Output Format:
Corresponding to the input, print the minimum number of pages Little Jhool needs to tear out from the combination of both the notebooks. 
If it is NOT possible, print "−1".

SAMPLE INPUT
2
23
32
SAMPLE OUTPUT
-1
3
*/
#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t>0){
        int n,temp;
        scanf("%d",&n);
        if(n%2!=0 || n<10)
            printf("-1\n");
        else{
            if(n%12==0)
                printf("%d\n",n/12);
            else{
                int flag=0;
                temp=(n%12)+12;
                if(n%12==10)
                    temp=10;
                while(temp<=n){
                    if(temp%10==0){
                        printf("%d\n",(temp/10)+((n-temp)/12));
                        flag=1;
                        break;
                    }
                    else{
                        temp+=12;
                    }
                }
                if(flag==0)
                    printf("-1\n");
            }
        }
        t--;
    }
    return 0;
}