import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("delhiaqi.csv")
df["date"] = pd.to_datetime(df["date"])

df["Month"] = df["date"].dt.month
df["Year"] = df["date"].dt.year
df["Season"] = df["Month"].apply(lambda m: "Winter" if m in [12,1,2] else ("Summer" if m in [3,4,5] else ("Monsoon" if m in [6,7,8] else "PostMonsoon")))

pollutants = ["pm2_5","pm10","no2","so2","co","o3","nh3"]

print(df[pollutants].describe())

plt.figure(figsize=(12,6))
plt.plot(df["date"], df["pm2_5"])
plt.title("PM2.5 Levels Over Time")
plt.show()

df["pm2_5_rolling"] = df["pm2_5"].rolling(window=24).mean()

plt.figure(figsize=(12,6))
plt.plot(df["date"], df["pm2_5"], alpha=0.4)
plt.plot(df["date"], df["pm2_5_rolling"], color="red")
plt.title("PM2.5 with 24-Hour Rolling Average")
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(x="Season", y="pm2_5", data=df)
plt.title("Seasonal PM2.5 Distribution")
plt.show()

seasonal_stats = df.groupby("Season")["pm2_5"].mean()
print(seasonal_stats)

winter = df[df["Season"]=="Winter"]["pm2_5"]
summer = df[df["Season"]=="Summer"]["pm2_5"]
monsoon = df[df["Season"]=="Monsoon"]["pm2_5"]
post = df[df["Season"]=="PostMonsoon"]["pm2_5"]

anova_result = stats.f_oneway(winter, summer, monsoon, post)
print("ANOVA Result:", anova_result)

plt.figure(figsize=(10,8))
sns.heatmap(df[pollutants].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

correlation_with_pm25 = df[pollutants].corr()["pm2_5"].sort_values(ascending=False)
print(correlation_with_pm25)

monthly_avg = df.groupby(["Year","Month"])["pm2_5"].mean().unstack()

plt.figure(figsize=(12,6))
sns.heatmap(monthly_avg, cmap="YlOrRd")
plt.title("Year-Month Heatmap of PM2.5")
plt.show()

z_scores = np.abs(stats.zscore(df["pm2_5"]))
df["Anomaly"] = z_scores > 3

plt.figure(figsize=(12,6))
plt.scatter(df["date"], df["pm2_5"], c=df["Anomaly"], cmap="coolwarm")
plt.title("PM2.5 Anomaly Detection (Z-Score)")
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(df["pm2_5"], kde=True)
plt.title("Distribution of PM2.5")
plt.show()

daily_avg = df.resample("D", on="date").mean(numeric_only=True).reset_index()

plt.figure(figsize=(12,6))
plt.plot(daily_avg["date"], daily_avg["pm2_5"])
plt.title("Daily Average PM2.5 Trend")
plt.show()

df_reg = df.dropna()
X = df_reg[["pm10","no2","so2","co","o3","nh3"]]
y = df_reg["pm2_5"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

coefficients = pd.Series(model.coef_, index=X.columns).sort_values(ascending=False)
print("Regression Coefficients:")
print(coefficients)

plt.figure(figsize=(8,6))
coefficients.plot(kind="bar")
plt.title("Pollutant Influence on PM2.5")
plt.show()