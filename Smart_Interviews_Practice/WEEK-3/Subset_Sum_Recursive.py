"""
Given an array of integers "Arr" and sum "K". 
To check whether there exists a subset in Arr which sum upto k.

No.of subsets for given set of N elements will be 2^N.

Here we will be using Backtracking method to get the solution, by calculating all the possible answers.
In backtracking method we will get all possible solutions.
"""
def Subset_Sum_Recursive(Arr,K,index):
    if(index==-1): 
        """
        When we reach last index, then that means we got a subset,
        Now we will check whether the given subset sum is equal to accquired sum or not.
        Since we are decrementing K for each recursion, once we get K==0 at end, 
        that means a subset exits, else not.
        """
        return(K==0)

    """
    Here We check whether to include a element of array into subset or not to include it. 
    """
    return (Subset_Sum_Recursive(Arr,K-Arr[index],index-1) or Subset_Sum_Recursive(Arr,K,index-1) )
    

Arr = list(map(int,input().split()))
K=int(input("SubSet Sum: "))
x=Subset_Sum_Recursive(Arr,K,0)
if(x==True):
    print("Subset Exits")
else:
    print("Subset Does not exist.")

"""
Time Complexity: O(2^N) --> Better than bit manipulation method which gives O(N*(02^N))
Space Complexity: O(1)
"""