# Determine the weight of 3 different steel cylinders using the following formula:

# 𝑤𝑒𝑖𝑔ℎ𝑡 = 𝑑𝑒𝑛𝑠𝑖𝑡𝑦 × π × 𝑟𝑎𝑑𝑖𝑢𝑠2 × ℎ𝑒𝑖𝑔ℎ𝑡

#Prompt the users to enter the radius and height separately for the THREE different cylinders, given the density is the same for all the cylinders which is 0.634.
# Coding by Bellamy



density = 0.634
π=22/7

c_1height = input('Enter height of cylinder 1:')
c_1height = int(c_1height)
c_1radius = input('Enter radius of cylinder 1:')
c_1radius = int(c_1radius)
c_1weight = density*π*c_1radius*c_1radius*c_1height

print(float(c_1weight))
print(' ')

c_2height = input('Enter height of cylinder 2:')
c_2height = int(c_2height)
c_2radius = input('Enter radius of cylinder 2:')
c_2radius = int(c_2radius)
c_2weight = density*π*c_2radius*c_2radius*c_2height

print(float(c_2weight))
print(' ')

c_3height = input('Enter height of cylinder 3:')
c_3height = int(c_3height)
c_3radius = input('Enter radius of cylinder 3:')
c_3radius = int(c_3radius)
c_3weight = density*π*c_3radius*c_3radius*c_3height

print(float(c_3weight))

input('Press ENTER to exit')
