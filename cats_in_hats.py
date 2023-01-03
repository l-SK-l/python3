# LIST
# hats = [False] * 100

# for i in range(1, 101):
#     for j in range(i - 1, 100, i):
#         hats[j] = not hats[j]

# for i, has_hat in enumerate(hats):
#     if has_hat:
#         print(f"Кот №{i + 1} носит шляпу")


# DICT
theCats = {}

# By default, no cats have been visited
# so we set every cat's number to False
for i in range(1, 101):
    theCats[i] = False

# Walk around the circle 100 times
for i in range(1, 101):
    # Visit all cats each time we do a lap
    for cats, hats in theCats.items():
        # Determine whether or not we visit a cat
        if cats % i == 0:
            # Add or remove the hat
            if theCats[cats]:
                theCats[cats] = False
            else:
                theCats[cats] = True

# Print whether each cat has a hat
for cats, hats in theCats.items():
    if theCats[cats]:
        print(f"Cat {cats} has a hat.")
    # else:
    #     print(f"Cat {cats} is hatless!")