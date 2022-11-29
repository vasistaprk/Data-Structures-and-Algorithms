"""
Standard Towers of Hanoi problem.
N = No.of Disks - standard N=3
Towers: A B C

Steps:
Moving N-1 disks from A--->B with help of C
1. A ---> C
2. A ---> B
3. C ---> B
Moving Nth dist A--->C
4. A ---> C
Moving N-1 disks from B--->C with help of A
5. B ---> A
6. B ---> C
7. A ---> C
"""
def TOH(N,Source,Temporary,Destination):
    if(N==0):
        return
    
    TOH(N-1,Source,Destination,Temporary)
    print ("Move "+Source+"-----> "+Destination)
    TOH(N-1,Temporary,Source,Destination)

"""
Time Complexity: O(2^N)
Space Complexity: O(1)
"""
N=int(input())
Towers=["A","B","C"]
TOH(3,"A","B","C")

