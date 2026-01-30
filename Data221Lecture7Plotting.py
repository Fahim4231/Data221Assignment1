from sklearn.preprocessing import StandardScaler
data = [[10, 90], [12, 96], [9, 120], [13, 112], [8, 88]]
scaler = StandardScaler()
data = scaler.fit_transform(data)
print(scaler)