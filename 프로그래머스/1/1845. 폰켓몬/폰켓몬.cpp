#include <vector>
#include <unordered_set>

using namespace std;

int solution(vector<int> nums)
{
    unordered_set <int > us;
    
    for(int i=0; i<nums.size(); i++){
        us.insert(nums[i]);
    }
    if(us.size()>=nums.size()/2){
        return nums.size()/2;
    }
    else{
        return us.size();
    }
}