# arr=[10, 30, 50, 20]

# for i in sorted(arr):
#     print(2*i)

# for i in sorted(arr, reverse=True):
#     print(2*i)

# dc = { 'Toy':3, 'Play':4, 'Games':5}
#  # print keys of dictionaries
# for d in dc:
#     print(d)

# dc = { 'Toy':3, 'Play':4, 'Games':5}
# for k, v in dc.items():
#     print(k, v)


def testNum(num):
    if num in [1,2,3,4,5]:
        print("Thanks!")
    else:
        print("Number is not inside")

testNum(7)
testNum(5)