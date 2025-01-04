# **Pure Pursuit Path Following Algorithm**

Welcome! This project is a **Pure Pursuit Path Following Algorithm** simulation written in **Processing (Python Mode)**. It lets you draw a path, control a follower object, and watch as the follower tracks the path using a lookahead-based approach. Below, you'll find everything you need to set up, run the program, and interact with it.

Here is a demo of the project:

https://github.com/user-attachments/assets/6fd0d321-fb0b-4aa7-91c0-1ae5027116a4

---

## **How to Set Up the Project**

### **Step 1: Install Processing**
1. Download and install **Processing** from [https://processing.org/download](https://processing.org/download).
2. Once installed, open Processing and switch to **Python Mode**:
   - Go to the drop-down menu in the top-right corner of the editor and select **Python Mode**. If it isn’t there, click **Add Mode...** and install it.

### **Step 2: Add the Code**
1. Copy the code provided into a new file in Processing.
2. Save the file with the name `PurePursuit.py`. Make sure it's saved in a folder with the same name (Processing requires this structure).

### **Step 3: Run the Program**
1. Click the **Play** button in the Processing editor to run the program.
2. A window will pop up where you can draw a path, add a follower, and see the simulation in action.

---

## **How to Use the Program**

Here’s a quick guide to the **keys and buttons**:

### **Mouse Controls**
- **Right-Click (Mouse Button 2):** Add a point to the path at the mouse's location.
- **Left-Click (Mouse Button 1):** Show a preview of the lookahead point from the mouse's position. (This doesn’t add points but shows where the follower would aim.)

### **Keyboard Controls**
- **`r`:** Reset everything. This clears the path and removes the follower.
- **`n`:** Start the follower from the first point on the path. The follower will begin moving when you press `f` (see below).
- **`f`:** Move the follower toward the lookahead point. Keep pressing this to advance the follower step by step.
- **`+`:** Increase the lookahead distance. The follower will look further ahead for the next point to pursue.
- **`-`:** Decrease the lookahead distance. This makes the follower look closer for the next point (but the distance can’t go negative).

---

## **How It Works**
1. **Draw the Path:** Right-click to place points in the window. These points will form the path for the follower.
2. **Add the Follower:** Once you’ve drawn a path, press `n` to add the follower to the first point of the path.
3. **Move the Follower:** Press `f` repeatedly to move the follower along the path. The follower moves toward a "lookahead point," which is a point ahead of it on the path within a set distance.
4. **Adjust the Lookahead Distance:** Use `+` and `-` to change how far ahead the follower looks. This changes how tightly or loosely the follower tracks the path.

---

## **Tips for Using the Program**
- **Smooth Paths Work Best:** When adding points to the path, try to avoid sharp turns or overlapping lines. The follower performs better with smooth, flowing paths.
- **Experiment with Lookahead Distance:** A larger lookahead distance results in smoother, less accurate movement. A smaller distance makes the follower more precise but can lead to jittery movement on tight turns.
- **Watch the Lookahead Circle:** The circle around the follower shows its lookahead range. The red dot marks the lookahead point it’s currently pursuing.

---

## **Troubleshooting**
- If the program doesn’t start:
  - Make sure Python Mode is installed and active in Processing.
  - Check that the file is named `PurePursuit.py` and saved in a folder with the same name.
- If the follower doesn’t move:
  - Ensure you’ve added a path first (using right-click) and pressed `n` to initialize the follower.

---

Enjoy watching your follower chase the path you create!
