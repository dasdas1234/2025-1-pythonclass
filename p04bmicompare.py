# 2025.04.30 파이썬 수업
# bmi 예측 머신러닝에서 객체지향실습

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
# 마이너스 깨짐 방지
matplotlib.rcParams['axes.unicode_minus'] = False

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor

# -------------------------------
# 1. BMI 데이터 생성
np.random.seed(42)
height = np.random.normal(170, 10, 1000)
weight = np.random.normal(65, 15, 1000)
bmi = weight / (height / 100) ** 2

X = np.vstack((height, weight)).T
y = bmi

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# -------------------------------
# 2. 다양한 회귀 모델 정의
models = {
    "선형회귀": LinearRegression(),
    "릿지회귀": Ridge(alpha=1.0),
    "라쏘회귀": Lasso(alpha=0.1),
    "엘라스틱넷": ElasticNet(alpha=0.1, l1_ratio=0.5),
    "서포트벡터": SVR(kernel='rbf', C=100),
    "K최근접이웃": KNeighborsRegressor(n_neighbors=5),
    "결정트리": DecisionTreeRegressor(max_depth=5),
    "랜덤포레스트": RandomForestRegressor(n_estimators=100),
    "그래디언트부스팅": GradientBoostingRegressor(n_estimators=100),
    "MLP신경망": MLPRegressor(hidden_layer_sizes=(20, 20), max_iter=1000)
}

results = {}

# -------------------------------
# 3. 모델 학습 및 평가
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    mse = mean_squared_error(y_test, pred)
    results[name] = mse
    print(f'{name}: MSE = {mse:.3f}')

# -------------------------------
# 4. 결과 시각화
sorted_results = dict(sorted(results.items(), key=lambda item: item[1]))

plt.figure(figsize=(12, 6))
bars = plt.bar(sorted_results.keys(), sorted_results.values(), color='skyblue')
plt.xticks(rotation=45)
plt.title("BMI 예측 회귀모델 성능 비교 (MSE 낮을수록 좋음)")
plt.ylabel("평균 제곱 오차 (MSE)")

# 그래프 위 MSE 숫자 표시
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f"{yval:.3f}", ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
