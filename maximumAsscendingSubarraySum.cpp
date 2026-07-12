#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int m;
    cin>>m;
    int arr[m];
    
    for(int i = 0;i<m;i++){
        cin>>arr[i];
    }  int sum = 0;int maxi = arr[0];
    for(int i = 0;i<m;i++){
        if(arr[i]<arr[i+1]){
            sum+=arr[i];
        }
        else{
            sum = arr[i];
        }
        maxi = max(maxi,sum);
        if(sum < 0){
            sum = 0;
        }
    } cout<<maxi;
    return 0;
}