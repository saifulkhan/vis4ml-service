import infomeasure as im

data = [0, 1, 0, 1, 0, 1, 0, 1]
entropy = im.entropy(data, approach="kernel", bandwidth=3, kernel="box")
# or
est = im.estimator(
    data, measure="entropy", approach="kernel", bandwidth=3, kernel="box"
)
print(f"Entropy with im.entropy   = {entropy}")
print(f"Entropy with im.estimator = {est.result()}")
