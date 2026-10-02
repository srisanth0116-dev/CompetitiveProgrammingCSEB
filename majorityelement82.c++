#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin>>n;
    vector<int>arr;
    for(int i =0;i<n;i++){
        int m;
        cin>>m;
      arr.push_back(m);
    }
 
    int c=0;int currnum;int maxi = 0;int ma;
   
    for(int i =0;i<n;i++){
        if(c==0){
            currnum = arr[i];
        }
         if(currnum == arr[i]){
            c = c+1;;
            if(maxi<c){
                maxi = c;
                ma = currnum;
            }
        }
        else{
            c=c-1;}
       
    }int p=0;
    for(int i =0;i<n;i++){
       if(arr[i]==ma){
        p++;
       }
    }
    if(p> n/2){
        cout<<ma;
    }
    else{
        cout<<-1;
    }
   
    return 0;
}
