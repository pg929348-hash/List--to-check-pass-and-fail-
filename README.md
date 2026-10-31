# List--to-check-pass-and-fail-
📊 Marks Pass/Fail & Average Calculator

This project analyzes a list of student marks to find pass/fail status, total passes, and average marks. 🎯

📝 What This Program Does

1. 📥 Takes a list of marks for different subjects.
2. 🔍 Checks each mark one by one.
3. ✅ If marks >= 33 -> PASS
4. ❌ If marks < 33 -> FAIL
5. 📈 At the end, shows total passes and average marks.

📌 Passing Criteria

- 🎓 Pass Marks = 33
- ✅ Marks >= 33 = Pass
- ❌ Marks < 33 = Fail

📥 Input Example

marks =
Total Subjects = 7[45][22][67][33][90][12][78]

📤 Output Example

✅ pass 45
❌ fail 22
✅ pass 67
✅ pass 33
✅ pass 90
❌ fail 12
✅ pass 78
🏆 pass:- 5
📊 your average:- 49.57

🔍 Output Explanation

- 📚 Total Subjects: 7
- ✅ Passed: 5 subjects
- ❌ Failed: 2 subjects (22 and 12)
- ➕ Total Marks = 347
- ➗ Average = 347 / 7 = 49.57

💡 Other Examples

Example 1: All Pass - 🌟 Topper

Input:[80][90][75]

✅ pass 80
✅ pass 90
✅ pass 75
🏆 pass:- 3
📊 your average:- 81.66

Example 2: Mix Result - 🙂 Average

Input:[32][33][31]

❌ fail 32
✅ pass 33
❌ fail 31
🏆 pass:- 1
📊 your average:- 32.0

Example 3: All Fail - 😢 Need Improvement

Input:[10][20][15]

❌ fail 10
❌ fail 20
❌ fail 15
🏆 pass:- 0
📊 your average:- 15.0
