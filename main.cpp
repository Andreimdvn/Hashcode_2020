#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

#define maxBooks 100000
#define maxLib 100000

ifstream f("sol_e.txt");
ofstream g("e_out.txt");

long long totalBooks, totalLib, totalDays, score[maxBooks + 5], booksInLib[maxLib + 5],
finishSignUp[maxLib + 5], shipPerDay[maxLib + 5], x, d, localScore;
vector<pair <vector<long long>, pair<long long, long long>>> books;
vector<long long > dummy;

bool sortbysec(const pair <vector<long long>, pair<long long, long long>> &a,
               const pair <vector<long long>, pair<long long, long long>> &b)
{
    return (a.second.first > b.second.first);
}

int main() {
    f >> totalBooks >> totalLib >> totalDays;
    for (int j = 0; j < totalBooks; j++) {
        f >> score[j];

    }
    for (int i = 0; i < totalLib; i++) {
        f >> booksInLib[i] >> finishSignUp[i] >> shipPerDay[i];
        localScore = 0;
        for (int j = 0; j < booksInLib[i]; j++) {
            f >> x;
            dummy.push_back(x);
            localScore += x;
            localScore = localScore - *min_element(dummy.begin(), dummy.end());
            localScore /= finishSignUp[i];
        }
        books.push_back(make_pair(dummy, make_pair(localScore, i)));
        dummy.clear();
    }

//sort (shipPerDay, shipPerDay + totalLib);
    //g << shipPerDay[totalLib-1]<<'\n';
    sort (books.begin(), books.end(), sortbysec);
    /*for (int i = 0; i < totalLib; i++) {
        g << books[i].second.second<< ' ';
    }*/

    /*for (int i = 0; i < totalLib/2; i+2) {

    }*/
    /*g<<15000<<'\n';

    for (int i = 0; i < totalLib/2; i++) {
        g<<books[i].second.second<<' '<<books[i].second.first<<'\n';
        for (int j = 0; j < books[i].first.size(); j++) {
            g << books[i].first[j] << ' ';
        }
        g<<'\n';
    }*/
    d = 0;
    long long lib = 0;
    long long index = 0;
    g << 1000<<'\n';
    for (int i = 0; i < totalLib; i++) {
        if (d < 100000) {
            index = books[i].second.second;
            d += finishSignUp[index];
            lib++;
            g << index << ' '<< booksInLib[index]<<'\n';
            for (int j = 0; j < books[i].first.size(); j++) {
                g << books[i].first[j]<<' ';
            }
            g<<'\n';
        }
    }


    return 0;
}