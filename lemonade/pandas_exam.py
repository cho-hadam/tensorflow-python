import pandas as pd

# 파일들로부터 데이터 읽어오기
file_route = 'http://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
lemonade = pd.read_csv(file_route)

file_route = 'http://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
boston = pd.read_csv(file_route)

file_route = 'http://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
iris = pd.read_csv(file_route)

# 데이터 모양 확인
print(lemonade.shape)
print(boston.shape)
print(iris.shape)

# column 이름 출력
print(lemonade.columns)
print(boston.columns)
print(iris.columns)

# 독립변수, 종속변수 분리
independent = lemonade[['온도']]
dependent = lemonade[['판매량']]
print(independent.shape, dependent.shape)

independent = boston[[
    'crim', 'zn', 'indus', 'chas',
    'nox', 'rm', 'age', 'dis', 'rad',
    'tax', 'ptratio', 'b', 'lstat']]
dependent = boston[['medv']]
print(independent.shape, dependent.shape)

independent = iris[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
dependent = iris[['품종']]
print(independent.shape, dependent.shape)

# 상위 5개 데이터 출력
print(lemonade.head())
print(boston.head())
print(iris.head())
