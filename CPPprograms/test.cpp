#include <bits/stdc++.h>

using namespace std;

int main() {
	{
	#ifndef ONLINE_JUDGE
		// for getting input from input.txt
		freopen("input.txt", "r", stdin);
		// for writing output to output.txt
		freopen("output.txt", "w", stdout);
	#endif
	}
	vector<int> v;

	for(int i = 0; i < 100; i++)
	{
		v.push_back(i+1);
		cout << "size: "<< v.size() << endl;
		cout << "capacity: "<< v.capacity() << endl;
	}

	v.push_back(10);
	v.push_back(20);
	v.push_back(30);

	v[1] = 100;



	//don't use [] for inserting elements.
	//v[3] = 1002;
	//v[4] = 1234;

	v.push_back(23);
	v.push_back(234);

		for(int i = 0; i < v.size(); i++) //even after popping back, the stored element in the popped index would be there, since the memory address is still accessible but the size is not the same at all. so the size is modified by the pop function
	{
		cout << v[i] << endl;
	}

	// for(int i = 0; i < v.size(); i++)
	// {
		// cout << v[i] << endl;
	// }
	
	// cout << v[0] << endl;
}
