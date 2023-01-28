// Examples:

// if string = "yfsgygdf", the function should return: "s".
// if string = "good morning", the function should return: "d".

// Do NOT edit nor remove any existing code when testing or submitting
#include <iostream>

// using namespace std;

std::string main_function(std::string input) {
  // Place your code here
  std::string ans = "";
  bool f = true;
  for(int i = 0; i<input.length(); i++)
  {
    char a = input[i];
    for(int j = i+1; j<input.length(); j++)
    { f = true;
      char b = input[j];
      // std::cout<<a<<" "<<b<<std::endl;
      if((a == b))
      { 
        // std::cout<<"--";
        f = false;
        break;
      }
      // std::cout<<"(flag)"<<f<<std::endl;
    }
  if(f == 1)
  { 
    ans = a;
    break;
  }

  }
  
  return ans;
}
    
// std::string k = main_function("good morning");
// std::cout<<k;
