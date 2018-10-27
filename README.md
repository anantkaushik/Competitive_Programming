/*
// Sample code to perform I/O:

#include <iostream>

using namespace std;

int main() {
	int num;
	cin >> num;										// Reading input from STDIN
	cout << "Input number is " << num << endl;		// Writing output to STDOUT
}

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here
#include <bits/stdc++.h>
using namespace std;
int main ()
{
    long long int n;
    cin>>n;
    long long int a[n],i,sum1=0,sum2=0,sum3=0,j,k;
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(i=0;i<n;i=i+3)
    {
        sum1=sum1+a[i];
    }
    for(j=1;j<n;j=j+3)
    {
        sum2=sum2+a[j];
    }
    for(k=2;k<n;k=k+3)
    {
        sum3=sum3+a[k];
    }
    
    
    
    
    cout<<sum1<<" ";
    cout<<sum2<<" ";
    cout<<sum3;
    return 0;
}
    
