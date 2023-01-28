/*
Change the capitalization of the letters
Examples:

if a string = "sUNNY mONDAY", the function should return: "Sunny Monday".
if a string = "cold PLACE", the function should return: "COLD place".

*/

// Do NOT edit nor remove any existing code when testing or submitting
#include <iostream>
#include <cstring>

std::string main_function(std::string input) {
  // Place your code here
  std::string ans = "";
  for(int i = 0; i < input.length(); i++){
    char ch = input[i];
    int asc = int(ch);

    if(int(ch) == 32){
      ans += ch;
      continue;
    }
    if(int(ch) >= 65 && int(ch) <= 92){
      ch = ch + 32;
    }
    else if(int(ch) >=97 && int(ch) <= 122){
      ch = ch - 32;
    }
    ans += ch;
  }

  return ans;

}
    
