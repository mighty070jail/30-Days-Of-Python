# Day 11: Implementing the Purple Shell Effect with Lists

### **Question: List Operations**

The next iteration of Mario Kart will feature an extra-infuriating new item, the **Purple Shell**.  
When used, it warps the last-place racer into first place and the first-place racer into last place.

Given the list of racers below, apply the Purple Shell effect manually using list operations.

```python
# Initial list of racers
racers = ["Mario", "Bowser", "Luigi"]

# Apply the Purple Shell effect here:
racers[0], racers[-1] = racers[-1], racers[0]

# Check the result
print(racers)  # Expected Output: ["Luigi", "Bowser", "Mario"]
```

### **Task:**
1. Use list indexing to swap the first and last elements in the `racers` list.
2. Verify the result matches the expected output.

### **Challenge:**
- Try the same operation with other lists of racers.  
- Handle edge cases like a list with only one racer or an empty list.

```python
# Example Tests
# Test 1
racers1 = ["Peach", "Mario", "Yoshi"]
racers1[0], racers1[-1] = racers1[-1], racers1[0]
print(racers1)  # Expected Output: ["Yoshi", "Mario", "Peach"]

# Test 2: List with two racers
racers2 = ["Wario", "Luigi"]
racers2[0], racers2[-1] = racers2[-1], racers2[0]
print(racers2)  # Expected Output: ["Luigi", "Wario"]

# Test 3: List with three identical racers
racers3 = ["Mario", "Mario", "Mario"]
racers3[0], racers3[-1] = racers3[-1], racers3[0]
print(racers3)  # Expected Output: ["Mario", "Mario", "Mario"]
```
