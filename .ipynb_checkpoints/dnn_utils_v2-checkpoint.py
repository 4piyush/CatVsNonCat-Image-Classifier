{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def sigmoid(Z):\n",
    "    \"\"\"\n",
    "    Implements the sigmoid activation in numpy\n",
    "    \n",
    "    Arguments:\n",
    "    Z -- numpy array of any shape\n",
    "    \n",
    "    Returns:\n",
    "    A -- output of sigmoid(z), same shape as Z\n",
    "    cache -- returns Z as well, useful during backpropagation\n",
    "    \"\"\"\n",
    "    \n",
    "    A = 1/(1+np.exp(-Z))\n",
    "    cache = Z\n",
    "    \n",
    "    return A, cache\n",
    "\n",
    "def relu(Z):\n",
    "    \"\"\"\n",
    "    Implement the RELU function.\n",
    "\n",
    "    Arguments:\n",
    "    Z -- Output of the linear layer, of any shape\n",
    "\n",
    "    Returns:\n",
    "    A -- Post-activation parameter, of the same shape as Z\n",
    "    cache -- a python dictionary containing \"A\" ; stored for computing the backward pass efficiently\n",
    "    \"\"\"\n",
    "    \n",
    "    A = np.maximum(0,Z)\n",
    "    \n",
    "    assert(A.shape == Z.shape)\n",
    "    \n",
    "    cache = Z \n",
    "    return A, cache\n",
    "\n",
    "\n",
    "def relu_backward(dA, cache):\n",
    "    \"\"\"\n",
    "    Implement the backward propagation for a single RELU unit.\n",
    "\n",
    "    Arguments:\n",
    "    dA -- post-activation gradient, of any shape\n",
    "    cache -- 'Z' where we store for computing backward propagation efficiently\n",
    "\n",
    "    Returns:\n",
    "    dZ -- Gradient of the cost with respect to Z\n",
    "    \"\"\"\n",
    "    \n",
    "    Z = cache\n",
    "    dZ = np.array(dA, copy=True) # just converting dz to a correct object.\n",
    "    \n",
    "    # When z <= 0, you should set dz to 0 as well. \n",
    "    dZ[Z <= 0] = 0\n",
    "    \n",
    "    assert (dZ.shape == Z.shape)\n",
    "    \n",
    "    return dZ\n",
    "\n",
    "def sigmoid_backward(dA, cache):\n",
    "    \"\"\"\n",
    "    Implement the backward propagation for a single SIGMOID unit.\n",
    "\n",
    "    Arguments:\n",
    "    dA -- post-activation gradient, of any shape\n",
    "    cache -- 'Z' where we store for computing backward propagation efficiently\n",
    "\n",
    "    Returns:\n",
    "    dZ -- Gradient of the cost with respect to Z\n",
    "    \"\"\"\n",
    "    \n",
    "    Z = cache\n",
    "    \n",
    "    s = 1/(1+np.exp(-Z))\n",
    "    dZ = dA * s * (1-s)\n",
    "    \n",
    "    assert (dZ.shape == Z.shape)\n",
    "    \n",
    "    return dZ\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
