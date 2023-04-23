# def qn(m):
#     if len(m)==0:
#         return None
#     if len(m)==1:
#         return m
#     qnright=[]
#     qnleft=[]
#     right=left=False
#     for k in m:
#         if k==m[int(len(m)/2)]:
#             qnleft.append(k)    
#         elif k<m[int(len(m)/2)]:
#             qnleft.append(k)  
#             print(qnleft)
#             if len(m)==2:
#                 right=True
#                 break    
#         else:
#             qnright.append(k)
#             print(qnright)
#             if len(m)==2:
#                 left=True
#                 break   
#     if right==True:
#         qnright.append(m[1])
#     elif left==True:
#         qnleft.append(m[1])      
#     x=qn(qnleft)
#     y=qn(qnright)
#     return x+y

# print(qn([1,4,2,5,9,7,8]))    


# def quick_sort(input_array):
#     array_len = len(input_array)
#     if array_len == 0:
#         return  None
#     elif array_len == 1:
#         return input_array
#     pivot = input_array[int(array_len/2)]
#     pivot_left = []
#     pivot_right = []
#     for k in range(len(input_array)):
#         if k == int(array_len/2):
#             pivot_left.append(pivot)
#         elif input_array[k] < pivot:
#             pivot_left.append(input_array[k])
#             if array_len == 2:
#                 pivot_right.append(input_array[k+1])
#                 break
#         else:
#             pivot_right.append(input_array[k])
#             if array_len == 2:
#                 pivot_left.append(input_array[k+1])
#                 break
#     left = quick_sort(pivot_left)
#     right = quick_sort(pivot_right)
#     return left + right

# print(quick_sort([1,4,2,5,9,7,8]))

# def qn(m):
#     if len(m)==0:
#         return None
#     if len(m)==1:
#         return m
#     qnright=[]
#     qnleft=[]
#     for k in m:
       
#         if k<m[int(len(m)/2)]:
#             if len(m)==2 and qnleft!=[]:
#                 qnright.append(k)
#             else:    
#                 qnleft.append(k)  
#                 print(qnleft)
#         else:
#             if len(m)==2 and qnright!=[]:
#                 qnleft.append(k)
#             else:
#                 qnright.append(k)
#                 print(qnright)
#     x=qn(qnleft)
#     y=qn(qnright)
#     return x+y

# print(qn([1,4,2,5,9,7,8]))

def qf(n):
    qf_right=[]
    qf_left=[]
    qf_mid=[]
    for k in n: # 對應k的數字
        if k==n[int(len(n)/2)]:
                qf_mid.append(k)
        elif k>n[int(len(n)/2)]:
                qf_right.append(k)
            #     print(k,"right") 
        elif k<n[int(len(n)/2)]:
                qf_left.append(k)
            #     print(k,"left")
            # if n==2:
            #     qf_right.append(k)
            # else:
            #     qf_left.append(k)
    print(qf_left,qf_mid,qf_right)       
    # left=qf(qf_left)
    # mid=qf(qf_mid)
    # right=qf(qf_right)
    return  qf_left+qf_mid+qf_right 
    # return 僅為回傳數值，並非遞迴
A=qf([1,4,2,5,9,3,8])
# d,e,f=qf(a) #  測試下一輪執行狀況
print(A)
# print(d,e,f) 
# 
#






        

