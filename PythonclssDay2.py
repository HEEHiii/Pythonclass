#!/usr/bin/env python
# coding: utf-8

# In[5]:


no = 1

while no <= 100:
    if no % 3 == 0
          sum = sum + no
        
    no = no + 1
 # no  += 1 과 같은 표현 (파이썬에서는 이걸 많이 씀)
                 # java에서는 no++룰 씀
        
print(sum)


# In[11]:


for i in range(1, 11):
    print(i)


# In[15]:


# for 문으로 구구단 출력하기

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end="\t")
    print()


# In[34]:


for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end="\n")
        
        
    print()   


# In[41]:


# range를 사용하여 100 이하의 수중 짝수들만의 합계를 구하세요.
for i in range(1,101
        


# In[ ]:


# range(start, stop, step)

# for i in range(11):   #start를 생략 하면 0에서 시작 # stop을 생략하면 1씩 증가
#     print(i)
    


# In[47]:


# 리스트 축약/내포 List comprehension
# 리스트를 좀 더 편리하고 직관적으로 만드는 방법이다.

list1 = [1, 2 ,3, 4]
print(list1)

list2 = [num          for num in list1]
print(list2)

list3 = [num*2          for num in list1]
print(list3)

list4 = [num           for num in list1         if num %2 ==0]
print(list4)
# 리스트1에서 2의 배수만 뽑는다. (2,3,1 순서로)


# In[52]:


no = 70

if no >= 70:
    print("합격입니다.")
else:
    print("불합격입니다.")

    
#위의 if를 표현하는 또다른 방법

print("합격입니다." if no>=80 else "불합격입니다.")
 
      #true 케이스               뒤에는 false 케이스를 적는다.


# In[ ]:




