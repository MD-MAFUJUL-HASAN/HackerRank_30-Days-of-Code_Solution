#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";

    
    // Declare second integer, double, and String variables.
    int second_integer;
    double second_double;
    string second_string;
    // Read and save an integer, double, and String to your variables.
    string temp;
    getline(cin, temp);
    second_integer = stoi(temp);
    getline(cin, temp);
    second_double = stod(temp);
    getline(cin, second_string);
    // Note: If you have trouble reading the entire string, please go back and review the Tutorial closely.
    
    // Print the sum of both integer variables on a new line.
    cout<<i+second_integer<<endl;
    // Print the sum of the double variables on a new line.
    cout<<fixed<<setprecision(1)<<d+second_double<<endl;
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    cout<<s<<second_string<<endl;
    return 0;
