nums=[0,1,0,3,12]
nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
z=len(nums)
c=0
i=0
while(i!=z):
    if nums[i]==0:
        if c==0:
            j=i
        c+=1
        i+=1
    elif nums[i]!=0 and c!=0:
        nums[i-c:i+1]=nums[i-c:i+1][::-1]
        i=j+1
        c=0


