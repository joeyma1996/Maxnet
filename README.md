# Maxnet
A Maxnet is a recurrent competitive one-layer network used to determine which node has the highest initial activation.
Theta = 1 and error <= -1 / # of nodes ensures that the node that has the initial highest value prevail as "winner",
while the others subside to zero.

The maxnet allows for greater parallelism in execution, since every computation is local to each node rather than centralized. Maxnet assists more complex unsupervised learning networks, helping to determine the node whose weight vector is nearest to an input pattern.
