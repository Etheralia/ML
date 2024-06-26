{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# batch gradient descent\n",
    "## visualise the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import pylab\n",
    "df = pd.read_csv('../Data/ex1data1.txt', names=['x','y'])\n",
    "pylab.plot(df['x'], df['y'],'o')\n",
    "pylab.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next is to fit the linear regression parameters θ to our dataset using gradient descent."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "def compute_cost_function(m, t0, t1, x, y):\n",
    "    return 1/2/m * sum([(t0 + t1* np.asarray([x[i]]) - y[i])**2 for i in range(m)])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "this function is used to calculate the cost function J(θ). After that, we will create a gradient decent implementation. Below is to calculate the gradient decent value for each iteration while updating the decent value."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'm' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[5], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m grad0 \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m1.0\u001b[39m\u001b[38;5;241m/\u001b[39m\u001b[43mm\u001b[49m \u001b[38;5;241m*\u001b[39m \u001b[38;5;28msum\u001b[39m([(t0 \u001b[38;5;241m+\u001b[39m t1\u001b[38;5;241m*\u001b[39mnp\u001b[38;5;241m.\u001b[39masarray([x[i]]) \u001b[38;5;241m-\u001b[39m y[i]) \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(m)])\n\u001b[1;32m      2\u001b[0m grad1 \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m1.0\u001b[39m\u001b[38;5;241m/\u001b[39mm \u001b[38;5;241m*\u001b[39m \u001b[38;5;28msum\u001b[39m([(t0 \u001b[38;5;241m+\u001b[39m t1\u001b[38;5;241m*\u001b[39mnp\u001b[38;5;241m.\u001b[39masarray([x[i]]) \u001b[38;5;241m-\u001b[39m y[i])\u001b[38;5;241m*\u001b[39mnp\u001b[38;5;241m.\u001b[39masarray([x[i]]) \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(m)])\n\u001b[1;32m      3\u001b[0m \u001b[38;5;66;03m# update the theta_temp\u001b[39;00m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'm' is not defined"
     ]
    }
   ],
   "source": [
    "def gradient_descent(alpha, x, y, ep=0.0001, max_iter=1500):\n",
    "    converged = False\n",
    "    iter = 0\n",
    "    m = x.shape[0] # number of samples\n",
    "\n",
    "    # initial theta\n",
    "    t0 = 0\n",
    "    t1 = 0\n",
    "\n",
    "    # total error, J(theta)\n",
    "    J = compute_cost_function(m, t0, t1, x, y)\n",
    "    print('J=', J);\n",
    "    # Iterate Loop\n",
    "    num_iter = 0\n",
    "    while not converged:\n",
    "        # for each training sample, compute the gradient (d/d_theta j(theta))\n",
    "        grad0 = 1.0/m * sum([(t0 + t1*np.asarray([x[i]]) - y[i]) for i in range(m)]) \n",
    "        grad1 = 1.0/m * sum([(t0 + t1*np.asarray([x[i]]) - y[i])*np.asarray([x[i]]) for i in range(m)])\n",
    "\n",
    "        # update the theta_temp\n",
    "        temp0 = t0 - alpha * grad0\n",
    "        temp1 = t1 - alpha * grad1\n",
    "    \n",
    "        # update theta\n",
    "        t0 = temp0\n",
    "        t1 = temp1\n",
    "\n",
    "        # mean squared error\n",
    "        e = compute_cost_function(m, t0, t1, x, y)\n",
    "        print ('J = ', e)\n",
    "        J = e   # update error \n",
    "        iter += 1  # update iter\n",
    "    \n",
    "        if iter == max_iter:\n",
    "            print ('Max interactions exceeded!')\n",
    "            converged = True\n",
    "\n",
    "    return t0,t1"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Paper",
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
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
