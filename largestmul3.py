class Solution(object):
    def largestMultipleOfThree(self, digits):
        val_0 = []
        val_1 = []
        val_2 = []
        for i in digits:
            if i % 3 == 0:
                val_0.append(i)
            elif i % 3 == 1:
                val_1.append(i)
            else:
                val_2.append(i)
        val_1.sort(reverse=True)
        val_2.sort(reverse=True)
        
        # formde by 
        max_l = len(val_1) - len(val_1) % 3 + len(val_2) - len(val_2) % 3
        #print max_l
        inx = 0
        for i in range(1,len(val_1)+1):
            if i > len(val_2):
                break
            count = i*2
            remain = len(val_1) - i
            count += (remain - remain%3)
            
            remain = len(val_2) - i
            count += (remain - remain%3)
            
            if max_l < count:
                max_l = count
                inx = i
            
        #print inx,val_1,val_2
        val = []
        #print val_2[:inx]
        #print val_1[:inx]
        val += val_2[:inx]
        val += val_1[:inx]
        #print val
        if len(val_1) > inx:
            remain = val_1[inx:]
            last = len(remain) - len(remain)%3
            val += remain[:last]
        
        if len(val_2) > inx:
            remain = val_2[inx:]
            last = len(remain) - len(remain)%3
            val += remain[:last]
        
        val += val_0
        val.sort(reverse=True)
        res = ''
        for i in val:
            res += str(i)
        if len(res) > 0 and int(res) == 0:
            return '0'
        return res

val=Solution()
digits=list(map(int,input().split()))
print(val.largestMultipleOfThree(digits))
