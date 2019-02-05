#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

const size_t MAX_N = 5000000+2;
std::vector<short> cache(MAX_N, -1);

unsigned short collatz(unsigned long long x)
{
    //finished recursion?
    if(x==1)
        return 1; 
    
    //using cached results...
    if(x < cache.size() && cache[x] != -1) //short circuiting c++
        return cache[x];    
    
    //deeper recursion
    unsigned long long next;
    if(x%2==0)
        next = x>>1;
    else
        next = x*3+1;
    
    unsigned long long result;
    result = collatz(next) +1;
    
    if(x < cache.size())
        cache[x] = result;
    
    return result;
        
}

int main() {
    // dict<biggest_number: longest_chain_length>
    std::map<unsigned int, unsigned int> longest;
    
    unsigned long long max_tested = 1;
    longest[max_tested] = 1; //obvious case
    
    unsigned int t;
    std::cin >> t;
    while(t--)
    {
        unsigned int x;
        std::cin >> x;
        
        // if input x is bigger than anything tested
        for(; max_tested<=x; max_tested++)
        {
            auto chain_length = collatz(max_tested);
            // if current chain length is longer than any of tested number's chain length
            if (chain_length >= longest.rbegin()->second)
                longest[max_tested] = chain_length;
        }
        
        // find number with longest chain length from `std::map longest` 
        // but number should be less than equal to x, hence we use upperbound(x) then go back one
        auto best_length = longest.upper_bound(x);
        best_length--;
        
        std::cout << best_length->first << std::endl;
    }
    
    return 0;
}
