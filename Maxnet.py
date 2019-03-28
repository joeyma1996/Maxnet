'''
A Maxnet is a recurrent competitive one-layer network used to determine which node has the highest initial activation.
Theta = 1 and error <= -1 / # of nodes ensures that the node that has the initial highest value prevail as "winner",
while the others subside to zero.
'''

#If only all inputs are 0 except 1 node, a winner is declared
def checkWinner(Input):
    count = 0
    for i in Input:
        if i == 0:
            count += 1
    return count == len(Input) - 1

#Calculate the maxnet
def Maxnet(Input,e):
    Output = []
    for i in range(len(Input)):
        #MAXNET FORMULA
        Output.append(max(0,Input[i] + e * (sum(Input) - Input[i])))
    return Output

def main():
    iteration = 0
    #One of the inputs must be 1
    Input = [1,0.9,0.9,0.9,0.5,0.5]

    try:
        e = -1 / len(Input)
    except:
        print("Length of Input must be longer than 0")
        return

    while checkWinner(Input) == False:
        iteration += 1
        Input = Maxnet(Input,e)
        print(Input)

    #Find winner node
    for i in range(len(Input)):
        if Input[i] != 0:
            node = i + 1
    print("\nIt took", iteration, "iterations, and the winning node is #", node)

main()
