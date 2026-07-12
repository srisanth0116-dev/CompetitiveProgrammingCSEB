#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n;
    cin>>n;
   int arr[n];
    for(int i = 0;i<n;i++){
        cin>>arr[i];
    }  
    int m ;
    cin>>m;
    int b[m];
    for(int i = 0;i<m;i++){
        cin>>b[i];
    }
    vector<int>c;int i = 0;int j = 0;
    while(i<n && j<m){
        
        if(arr[i]<b[j]){
            
            c.push_back(arr[i]);
            i++;
        }
        else{
            c.push_back(b[j]);
            j++;
        }
    }
    while(i<n){
        c.push_back(arr[i]);
        i++;
    }
    while(j<m){
        c.push_back(b[j]);
        j++;
    }
    for(int i = 0;i<c.size();i++){
        cout<<c[i]<<" ";
    }
    return 0;
}