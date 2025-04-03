#include <iostream>
using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        
        string result = "";
        int longest = 0;
        int len1 = 0;
        int len2 = 0;

        for(char letter1: word1){
            len1++;
        }

        for(char letter2: word2){
            len2++;
        }

        if(len1 > len2){
            longest = len1;
        } else {
            longest = len2;
        }

        for(int i = 0; i < longest; i++){

            if (i < len1 && word1[i] != '\0') {
                result += word1[i];
            }

            if (i < len2 && word2[i] != '\0') {
                result += word2[i];
            }
        }

        return result;
    }
};

int main(){

    Solution Hola;

    string word_one = "abc";
    string word_two = "pqraaa";
    cout << Hola.mergeAlternately(word_one,word_two);

    
    return 0;
}