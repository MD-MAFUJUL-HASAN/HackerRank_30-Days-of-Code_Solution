#include <iostream>
#include <queue>
#include <stack>

using namespace std;

class Solution {
    //Write your code here
private:
    queue<char> q;
    stack<char> s;

public:
    char popCharacter() {
        char tmp = s.top();
        s.pop();
        return tmp;
    }

    void pushCharacter(char ch) {
        s.push(ch);
    }

    char dequeueCharacter() {
        char tmp = q.front();
        q.pop();
        return tmp;
    }

    void enqueueCharacter(char ch) {
        q.push(ch);
    }
};

int main() {