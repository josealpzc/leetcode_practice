#include <iostream>
using namespace std;

int main()
{
	
	struct Node          //binary tree node declaration 
	{
		Node *left;
		Node *right;
		int data;	
	};

	struct 
	{
		int myNum;
		string myString;
	}testing;
	
	testing.myNum=1;
	testing.myString= "Hello World!";
	
	cout << testing.myNum << "\n";
	
	string food = "Pizza";
	cout << food << " <- Value\n";
	cout << &food << " <- Address\n";

	string* ptr =&food;

	cout << ptr << " <- Pointer\n";	

	cout << "Hello, World!.\n";
	
	return 0;

}
