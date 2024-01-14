import numpy as np
import math
class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        avg=0
        array=np.array(img)
        s=array.shape
        newarray=np.zeros(s)
        alen=len(array)
        for i in range(alen):
            for j in range(len(array[i])):
                if i+1>=alen and j+1<len(array[i]):
                    sum=array[i][j]+array[i-1][j]+array[i][j-1]+array[i][j+1]+array[i-1][j-1]+array[i-1][j+1]
                    avg=math.floor(sum/6)
                    newarray[i][j]=avg
                if (i-1>=0 and j-1>=0) and (i+1<alen and j+1<len(array[i])):
                    sum=array[i][j]+array[i-1][j]+array[i+1][j]+array[i][j-1]+array[i][j+1]+array[i+1][j+1]+array[i-1][j-1]+array[i+1][j-1]+array[i-1][j+1]
                    avg=math.floor(sum/9)
                    newarray[i][j]=avg
                if i+1<alen and j+1>=len(array[i]):
                    sum=array[i][j]+array[i-1][j]+array[i][j-1]+array[i+1][j]+array[i-1][j-1]+array[i+1][j-1]
                    avg=math.floor(sum/6)
                    newarray[i][j]=avg
                if (i-1<0 and j-1>=0) and (i+1<alen and j+1<len(array[i])):
                    sum=array[i][j]+array[i+1][j]+array[i][j-1]+array[i][j+1]+array[i+1][j+1]+array[i+1][j-1]
                    avg=math.floor(sum/6)
                    newarray[i][j]=avg
                if (i-1>=0 and j-1<0) and (i+1<alen and j+1<len(array[i])):
                    sum=array[i][j]+array[i+1][j]+array[i-1][j]+array[i][j+1]+array[i+1][j+1]+array[i-1][j+1]
                    avg=math.floor(sum/6)
                    newarray[i][j]=avg
                if (i-1<0 and j-1<0) and (i+1<alen and j+1<len(array[i])):
                    sum=array[i][j]+array[i+1][j]+array[i][j+1]+array[i+1][j+1]
                    avg=math.floor(sum/4)
                    newarray[i][j]=avg
                if i+1>=alen and j+1>=len(array[i]):
                    sum=array[i][j]+array[i-1][j]+array[i-1][j-1]+array[i][j-1]
                    avg=math.floor(sum/4)
                    newarray[i][j]=avg
                if i-1<0 and j+1>=len(array[i]) and i+1<alen:
                    sum=array[i][j]+array[i+1][j]+array[i+1][j-1]+array[i][j-1]
                    avg=math.floor(sum/4)
                    newarray[i][j]=avg
                if i+1>=alen and j-1<0 and j+1<len(array[i]):
                    sum=array[i][j]+array[i-1][j]+array[i-1][j+1]+array[i][j+1]
                    avg=math.floor(sum/4)
                    newarray[i][j]=avg
        final=newarray.astype(int).tolist()
        return final
