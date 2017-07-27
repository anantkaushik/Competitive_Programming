/* John Snow is travelling from Winterfell to Dragonstone to meet Daeneryys Targaryen. In between, Winterfell and Dragonstone there are ‘N’ 
number of towns numbered 1,2,3… N (excluding Winterfell). John will start travelling from Winterfell to town 1 and then to town 2 and so on upto 
town N (Dragonstone). Winterfell is numbered as Town 0. John Snow loves to drink Blackberry wine while travelling.
Each town has got some value ‘C’ associated with it i.e number of bottles of Blackberry at each that town. The value of ‘C’ for Winterfell is 0.
When moving from town ‘i’ to town ‘i+1’, John Snow will either get or lose some bottles of Blackberry Wine. While moving from town i to town i+1, 
John snow will get Ci – Ci+1 ,0<=i< N ,bottles if this number is non-negative else he will lose that number of bottles.
John snow cannot move from town i to town i+1 if he has negative number of bottles with him at any point of time. So, he might need to buy some bottles 
of wine to continue his journey to Dragonstone. Price of each bottle of Blackberry wine is ‘X’ .
Initially, John has ‘P’ amount of money with him, so he asks you whether it is possible for him to travel to Dragonstone or not. 
If it is possible to reach, what amount of money he can save while spending minimum amount of money. If it is not possible, how much more minimum 
amount of money he will require to reach Dragonstone.

Input :
First line of the input will contain T (No. of test cases).
For each test case, first line will contain three space separated integers N, X and P (i.e. number of towns, price of each Blackberry wine 
bottle and amount of money John is having respectively.) Next line will contain N space separated integers denoting Ci, the number of 
Blackberry wine bottles at ith town.

Output :
For every test case, if it is possible to reach Dragonstone print “Possible” without quotes and next line print amount of money 
John will be able to save. If it is not possible to reach Dragonstone with ‘P’ amount of money print “Impossible” without quotes 
and also print minimum amount of money needed more in next line.

SAMPLE INPUT
2
2 10 40
1 3
3 5 10
1 4 1

SAMPLE OUTPUT
Possible
10
Impossible
10
 
Explanation:
For the first test case: Cost of each bottle is 10. John is having 40 amount of money with him . John will buy 1 bottle (0-1=-1) at town 1 and 
2 bottles (1-3=-2) at town 2 . So John can easily reach to Dragonstone and will be able to save 10 amount of money.
For the second test case:Cost of each bottle is 5. John has 10 amount of money with him. John will have to buy 1 bottle at town 1 (0-1=-1) and 
3 bottles of wine at town 2 (1-4=-3). John will get 3 bottles of wine while moving from town 2 to town 3 ( 4-1=3) which he can use in future. 
So total cost incurred will be 4*5=20 but John has only 10 amount of money. So,it is Impossible for him to reach is destination and he need 10 more 
amount of money to reach Dragonstone.*/
#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t>0){
        int n,x,p;
        scanf("%d %d %d",&n,&x,&p);
        int a[n],i,bottle=0,price=0,xb=0;
        for(i=0;i<n;i++){
            scanf("%d",&a[i]);
            if(i==0)
                bottle+=a[i];
            else if(i>0){
                if((a[i-1]-a[i])<0){
                    if(xb>0){
                        if(xb<=(a[i]-a[i-1])){
                            bottle+=(a[i]-a[i-1]-xb);
                            xb=0;
                        }
                        else{
                            xb=xb-(a[i]-a[i-1]);
                        }
                    }
                else
                    bottle+=(a[i]-a[i-1]);   
                }
                else
                    xb+=(a[i-1]-a[i]);
            }
        }
        price=bottle*x;
        if(price<=p){
            printf("Possible\n");
            printf("%d\n",p-price);
        }
        else{
            printf("Impossible\n");
            printf("%d\n",price-p);
        }
        t--;
    }
    return 0;
}