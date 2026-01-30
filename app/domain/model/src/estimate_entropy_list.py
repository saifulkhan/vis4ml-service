import infomeasure as im

data = [0, 1, 0, 1, 0, 1, 0, 1, 1, 2, 1, 3, 1, 1, 1, 1]
entropy0 = im.entropy(data, approach="discrete", base=2)
entropy1 = im.entropy(data, approach="kernel", bandwidth=1, kernel="box", base=2)
entropy5 = im.entropy(data, approach="kernel", bandwidth=5, kernel="box", base=2)

symbol = ["cat", "dog", "dog", "mouse"]
entropy = im.entropy(symbol, approach="discrete", base=2)
# or
# est = im.estimator(
#     data, measure="entropy", approach="kernel", bandwidth=3, kernel="box"
# )
print(f"Entropy with im.entropy discrete   = {entropy0}")
print(f"Entropy with im.entropy band1   = {entropy1}")
print(f"Entropy with im.entropy band5  = {entropy5}")
print(f"Entropy = {entropy}")

# print(f"Entropy with im.estimator = {est.result()}")
