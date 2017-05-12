/* Our friend Monk has an exam that has quite weird rules. Each question has a difficulty level in the form of an Integer. 
Now, Monk can only solve the problems that have difficulty level less than X . Now the rules are-
-Score of the student is equal to the maximum number of answers he/she has attempted without skipping a question.
-Student is allowed to skip just "one" question that will not be counted in the continuity of the questions.
Note- Assume the student knows the solution to the problem he/she attempts and always starts the paper from first question.
Given the number of Questions, N ,the maximum difficulty level of the problem Monk can solve , 
X,and the difficulty level of each question , Ai can you help him determine his maximum score?

Input Format: First Line contains Integer N , the number of questions and the maximum difficulty X Monk can solve.
Next line contains N integers, Ai denoting the difficulty level of each question.
Output Format: Maximum score Monk can achieve in the exam. 


SAMPLE INPUT
7 6
4 3 7 6 7 2 2
SAMPLE OUTPUT
3

Explanation: In this example, maximum difficulty = 6, Monk solves question 0 and 1, but skips the question 2 as A[2]>6. 
Monk then solves the question 3,but stops at 4 because A[4]>6 and question 2 was already skipped. 
As 3 questions (0,1 and 3) were solved and 2 questions (2 and 4) have been skipped, therefore we print "3".*/

#include <stdio.h>
int main(){
    int q,m;
    scanf("%d %d",&q,&m);
    int a[q],i,count=0,c=0;
    for(i=0;i<q;i++)
        scanf("%d",&a[i]);
    for(i=0;i<q;i++){
        if(a[i]<=m)
            c++;
        else if(a[i]>m && count==0)
            count=1;
        else if(a[i]>m && count==1)
            break;
    }
    printf("%d",c);
    return 0;
}