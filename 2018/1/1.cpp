// rishav.io

#include <iostream>
#include <vector>
#include <string>
#include <climits>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

typedef long long LL;

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(0);

#ifdef __APPLE__
	freopen("input.txt", "r", stdin);
#endif

	int val;
	int t = 0;
	vector<int> vec;
	while ((cin >> val)) {
		t += val;
		vec.push_back(val);
	}
	cout << t << '\n';
	unsigned int idx = 0;
	t = 0;
	set<int> lookup;
	while (true) {
		t += vec[idx];
		if (lookup.find(t) != lookup.end()) {
			cout << t << '\n';
			break;
		}
		lookup.insert(t);
		idx = (idx + 1) % (vec.size());
	}

}
