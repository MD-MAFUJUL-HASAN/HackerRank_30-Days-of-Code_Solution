#include <bits/stdc++.h>

using namespace std;



int main()
{
    string S;
    getline(cin, S);
    try {
        cout<<stoi(S)<<endl;
    }
    catch(invalid_argument &e) 
    {
        cout<<"Bad String\n" ;
    }
    return 0;
}

