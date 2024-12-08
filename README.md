# 🚀 **Path-Finding Agent**

## 📝 **Description**

The **Path-Finding Agent** visualizes and evaluates various pathfinding algorithms on a grid. It offers real-time visualizations and metrics, making it a valuable tool for educational purposes, algorithm testing, and demonstrating search strategies.

The project implements algorithms such as:
- **BFS** (Breadth-First Search)
- **DFS** (Depth-First Search)
- **A*** (A-star Search)
- **Greedy Best-First Search**

The tool includes features like step-by-step visualization, metric tracking (e.g., path cost, execution time), and the ability to save results in Excel files.

---

## 🛠 **Prerequisites**

### 💻 **System Requirements**
- **Operating System:** Windows 10 or later, macOS 11.0 or later, Linux  
- **Python Version:** 3.8 or newer  
- **IDE:** PyCharm, VS Code, or any Python-supported IDE

### 📦 **Required Python Libraries**

The following Python libraries are required to run the project:

| **Library**     | **Purpose**                              |
|------------------|------------------------------------------|
| `pygame`        | Grid visualization                       |
| `time`          | Tracking execution time                 |
| `random`        | Randomly generating configurations       |
| `collections`   | Handling deques for certain algorithms   |
| `openpyxl`      | Saving results to Excel files            |

To install all required libraries, see the **Installation Guide** below.

---

## 🚀 **Installation Guide**

### Step 1: Clone the Repository
Clone the project repository to your local machine:

```bash
git clone <repository-url>
```
### Step 2: Install Python  
Ensure Python 3.8 or newer is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 3: Install Libraries  
Install the required Python libraries by running the following command in your terminal:
```bash
pip install pygame openpyxl
```

---

## 🎮 **Usage**

### Running the Project
To start the program, execute the following command:
```bash
python main.py
```

### Features

1. **Grid Visualization**:
   - Interactive grid where nodes are visualized as:
     - **Start (Green)**
     - **End (Light Cyan)**
     - **Barriers (Black)**
     - **Frontier, Not Explored(Green)**
     - **Explored (Red)**
     - **Path (Purple)**

2. **Algorithm Comparison**:
   - Run all algorithms on the same configuration to compare their performance.

3. **Metrics Export**:
   - Results are saved to `data.xlsx` with detailed metrics for each run.
  
  ---

## 🕹️ **Modes of Operation**

The **Path-Finding Agent** provides three distinct modes of operation to test and visualize pathfinding algorithms effectively:

### 1. **Manual Mode**
   - In this mode, the user can manually configure the grid by:
     - Placing start and end points.
     - Adding barriers to simulate obstacles.
   - After setting up the grid, the user presses "Space", and the program visualizes the step-by-step execution of the chosen algorithm (should choose from the main.py loop)

### 2. **Automated Random Mode**
   - The grid is automatically generated with random configurations:
     - Randomly placed barriers.
     - Start and end points are selected randomly.
   - The user's preselected algorithm runs on the random grid, and the pathfinding process is visualized. Then, based on `num_tests` the iterations continue into the next one

### 3. **Automated Random Mode for All Algorithms**
   - A random grid is generated, and all implemented algorithms (BFS, DFS, A*, Greedy Best-First Search) are executed sequentially on the **same grid**.
   - This mode provides a side-by-side comparison of:
     - Execution time.
     - Steps taken.
     - Path length.
     - Expanded nodes.
    
       
   - Results for all algorithms are exported to an Excel file (`data.xlsx`) for further analysis.

---

Each mode is designed to offer flexibility for users, from manual control to fully automated testing and comparison. The **Automated Random Mode for All Algorithms** is particularly useful for analyzing and benchmarking algorithm performance on identical conditions.

---

## 📦 **Sample Output**

The project tracks and visualizes the following metrics:
- Actual Path.
- Execution time (seconds).
- Number of steps.
- Manhattan Distance (the heuristic)
- Number of expanded nodes.
- Name of the Algorithm

Results are saved to `data.xlsx`. Here’s an example of how the metrics are logged:


| **Path**                   | **Execution Time** | **Steps** | **Manhattan Distance** | **Expanded Nodes** | **Algorithm** |
|----------------------------|--------------------|-----------|-------------------------|---------------------|---------------|
| [(11, 8), (12, 8)]         | 1.53060365         | 33        | 20                      | 196                 | A_star        |
| [(12, 11), (13, 1)]        | 0.21062803         | 28        | 27                      | 28                  | A_star        |
| [(39, 1), (39, 2)]         | 2.29333401         | 59        | 52                      | 261                 | A_star        |
| [(9, 47), (9, 48)]         | 4.24531412         | 67        | 44                      | 520                 | A_star        |
| [(30, 27), (31, 1)]        | 1.05139089         | 37        | 34                      | 127                 | A_star        |
| [(46, 19), (45, 4)]        | 0.96028924         | 44        | 43                      | 116                 | A_star        |
| [(8, 7), (8, 6)]           | 0.52769589         | 25        | 16                      | 64                  | A_star        |
| [(20, 44), (21, 1)]        | 1.06542826         | 26        | 21                      | 128                 | A_star        |
| [(43, 40), (42, 1)]        | 1.7910738          | 44        | 33                      | 218                 | A_star        |
---

### DEMONSTRATIONS

![393545508-ecb77920-00ed-4df0-b193-3c57f8c44b3d](https://github.com/user-attachments/assets/2ff52fd4-3ae8-4f2f-b5ea-dc699e4d2e64)
