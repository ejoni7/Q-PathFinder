# LineMove — A Simple Q-Learning Environment for Movement in n-Dimensional Grid

## Short Description
This project is a simple implementation of the Q-learning algorithm for an agent moving in a discrete n-dimensional grid (cubic lattice) from the start point to the goal point.  
The environment is defined as a `LineMove` class, and the agent uses an ε-greedy policy.  
The goal is to demonstrate Q-value learning and visualize the final path (2D/3D) using `matplotlib`.

---

## Main Structure of the Code

### LineMove class
A simple environment that:

- **Inputs:** `dim` (space dimension, default = 3) and `dima` (grid size in each dimension, default = 5).  
- **Start state:** all coordinates are zeros `(0,0,...)`.  
- **Goal state:** all coordinates are `dima-1` `(dima-1, dima-1,...)`.  
- **Actions:** two actions per dimension (increase or decrease) .  
- **step(action) function:** updates the state and:
  - If the goal is reached: returns a positive reward (a root function of dimensions and size) and ends the episode.  
  - Otherwise: returns reward `-1`.

### Q Initialization
- `q`: a dictionary where keys are possible states and values are lists of Q-values for each action.

### Learning Loop
- **Number of episodes:** appropriate with dimensions and sizes .  
- **ε-greedy policy:** with decreasing ε based on logarithm.  
- **Q-values update rule:**  

````
Q ← Q + α (r + γ max Q' − Q)

````

### Path Visualization
- If the space dimension is **3**, the path is drawn in 3D using `matplotlib`.  
- If the space dimension is **2**, the path is drawn in 2D.

---

## How to Run

 Install requirements:
 ```bash
 pip install numpy matplotlib
````

   After training, the agent’s final path will be displayed in a `matplotlib` window.

---

## Key Parameters

* **dim** (in LineMove constructor): number of dimensions (e.g., 2 or 3).
* **dima**: size of each dimension.
* **alpha**: learning rate (default `0.5`).
* **gamma**: discount factor (default `0.9`).
* **epsilon**: exploration probability, decreasing as:

  ```
  epsilon = 0.3 / (1 + log10(eq/2 + 1))
  ```
---

## Notes on Reward and Agent Behavior

* Each non-terminal move gives a reward of `-1`, encouraging shorter paths.
* Reaching the goal returns a positive reward scaled with dimensions and grid size.
* This is an educational implementation; the reward function and parameters can be adjusted.


