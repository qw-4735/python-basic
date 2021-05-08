# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:04:26 2021

@author: qwuni
"""
##### Numpy의 기본 사용법
import numpy as np

list_data = [1,2,3]
array = np.array(list_data)

print(array.size)
print(array.dtype)
print(array[2])

# 0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

array2 = np.zeros((4,4), dtype=float) 
# 하나의 2차원 배열을 만들고, 거기에 있는 값이 모두 0이며, 
#그 자료형들은 각각 실수형(float)을 가진다
array3 = np.ones((3,3), dtype=str)
print(array3)

# 0부터 9까지 랜덤하게 초기화 된 배열 만들기
array4 = np.random.randint(0,10,(3,3))
print(array4)

# 평균이 0이고, 표준편차가 1인 표준정규분포를 띄는 배열 만들기
array5 = np.random.normal(0,1,(3,3))
print(array5)

# Numpy 배열 합치기 (가로로, default)
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
array3 = np.concatenate([array1,array2])
print(array3.shape) # 크기 6
print(array3)

# Numpy 배열 바꾸기
array1 = np.array([1,2,3,4])
array2 = array1.reshape((2,2))
print(array2)

# Numpy 배열 합치기 (세로로, axis=0)
array1 = np.arange(4).reshape(1,4)
array2 = np.arange(8).reshape(2,4)
print(array1)
print(array2)
array3 = np.concatenate([array1, array2], axis=0)
print(array3)

# Numpy 배열 나누기
array = np.arange(8).reshape(2,4)
left,right = np.split(array, [2], axis=1) # index 2를 기준으로 나누고, 이 때 이 index는 열을 의미한다(axis=1).
print(left.shape)
print(right.shape)
print(array)
print(left)


##### Numpy의 기본연산
# Numpy의 상수연산
array = np.random.randint(1,10,size=4).reshape(2,2) 
print(array)
result_array = array * 10
print(result_array)

# 서로 다른 형태의 Numpy연산 (행 우선으로 수행) 
array1= np.arange(4).reshape(2,2) # (2x2)
array2= np.arange(2) # (1x2)
array3 = array1 +array2
print(array3)
# 브로드캐스팅 : 형태가 다른 배열을 연산할 수 있도록 배열의 형태를 동적으로 변환
array1 = np.arange(0,8).reshape(2,4)
array2= np.arange(0,8).reshape(2,4)
array3 = np.concatenate([array1, array2], axis=0)
array4 = np.arange(0,4).reshape(4,1)  # (4x1)
print(array3 + array4)

# Numpy의 마스킹 연산 (각 원소에 대해 조건이 맞는지를 체크)
array1= np.arange(16).reshape(4,4)
print(array1)
array2 = array1 < 10   # 마스킹
print(array2)

array1[array2] = 100  # array1에 마스킹연산이 수행된 array2를 넣게 되면
# 마스킹연산을 만족하는 데이터만 어떤 작업을 해주겠다.

# Numpy의 집계함수
array = np.arange(16).reshape(4,4)
print(array)
print("최대값: ", np.max(array))
print("최소값: ", np.min(array))
print("합계: ", np.sum(array))
print("평균값: ", np.mean(array))

print("합계: ", np.sum(array, axis=0))  # 열 합계

##### numpy를 저장하고 불러오기
# 단일 객체 저장 및 불러오기
array = np.arange(0,10)
np.save('saved.npy', array)

result = np.load('saved.npy')
print(result)

# 복수 객체 저장 및 불러오기
array1 = np.arange(0,10)
array2 = np.arange(10,20)
np.savez('saved.npz', array1= array1, array2=array2)

data = np.load('saved.npz')
result1 = data['array1']
result2= data['array2']
print(result1)
print(result2)

# Numpy원소의 정렬
array = np.array([5,9,10,3,1])
array.sort()  # 오름차순
print(array)
print(array[::-1])  # 내림차순

array = np.array([[5,9,10,3,1], [8,3,4,2,5]])
print(array)
array.sort(axis=0)  # 각 아ㅕㄹ을 기준으로 정렬
print(array)

# 균일한 간격으로 데이터 생성
array = np.linspace(0, 10, 5)
print(array)

# 난수의 재연 (실행마다 결과 동일)
np.random.seed(7)

# Numpy 배열 객체 복사
array1 = np.arange(0,10)
array2 = array1.copy()  # 이렇게 복사하면, array2의 값을 변경하더라도 array1에 영향을 끼치지 x
array2[0] = 99
print(array1)

# 중복된 원소 제거
array = np.array([1,1,2,2,2,3,3,4])
print(np.unique(array))
















