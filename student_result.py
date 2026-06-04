import csv
import os
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


def get_valid_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100.")
        except:
            print("❌ Please enter a valid number.")


students = []

if os.path.exists("students.csv"):

    with open("students.csv", "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Name"]:

                students.append({
                    "name": row["Name"],
                    "marks": [
                        int(row["Subject1"]),
                        int(row["Subject2"]),
                        int(row["Subject3"])
                    ],
                    "total": int(row["Total"]),
                    "average": float(row["Average"]),
                    "grade": row["Grade"]
                })

print(f"📂 Loaded {len(students)} student records.")

while True:
    print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Results")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Statistics Dashboard")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # ADD STUDENT
    if choice == "1":

        name = input("Enter student name: ")

        marks = []
        for i in range(3):
            m = get_valid_marks(f"Subject {i+1}")
            marks.append(m)

        total = sum(marks)
        avg = total / 3
        grade = calculate_grade(avg)

        students.append({
            "name": name,
            "marks": marks,
            "total": total,
            "average": avg,
            "grade": grade
        })

        print(f"✅ {name}'s data added successfully!")

    # VIEW RESULTS
    elif choice == "2":

        if len(students) == 0:
            print("⚠️ No student data available.")

        else:

            print("\n--- Student Results ---")

            topper = students[0]

            for s in students:

                print("\n------------------------")
                print("Name:", s["name"])
                print("Marks:", s["marks"])
                print("Total:", s["total"])
                print("Average:", round(s["average"], 2))
                print("Grade:", s["grade"])

                if s["total"] > topper["total"]:
                    topper = s

            print("\n🏆 Topper:", topper["name"],
                  "-", topper["total"], "marks")

            with open("results.txt", "w") as f:
                for s in students:
                    f.write(
                        f"{s['name']} | Total: {s['total']} | Grade: {s['grade']}\n")

            print("\n💾 Results saved to results.txt")

    # SEARCH STUDENT
    elif choice == "3":

        search_name = input("Enter student name to search: ")

        found = False

        for s in students:
            if s["name"].lower() == search_name.lower():

                print("\n✅ Student Found")
                print("------------------------")
                print("Name:", s["name"])
                print("Marks:", s["marks"])
                print("Total:", s["total"])
                print("Average:", round(s["average"], 2))
                print("Grade:", s["grade"])

                found = True
                break

        if not found:
            print("❌ Student not found.")

    # UPDATE STUDENT
    elif choice == "4":

        update_name = input("Enter student name to update: ")

        found = False

        for s in students:

            if s["name"].lower() == update_name.lower():

                print("Enter new marks")

                new_marks = []

                for i in range(3):
                    m = get_valid_marks(f"Subject {i+1}")
                    new_marks.append(m)

                s["marks"] = new_marks
                s["total"] = sum(new_marks)
                s["average"] = s["total"] / 3
                s["grade"] = calculate_grade(s["average"])

                print("✅ Student record updated successfully.")

                found = True
                break

        if not found:
            print("❌ Student not found.")

    # DELETE STUDENT
    elif choice == "5":

        delete_name = input("Enter student name to delete: ")

        found = False

        for s in students:

            if s["name"].lower() == delete_name.lower():

                students.remove(s)

                print("🗑️ Student record deleted successfully.")

                found = True
                break

        if not found:
            print("❌ Student not found.")

    # STATISTICS DASHBOARD
    elif choice == "6":

        if len(students) == 0:

            print("⚠️ No student data available.")

        else:

            totals = [s["total"] for s in students]

            highest = max(totals)
            lowest = min(totals)

            average_class = sum(totals) / len(students)

            pass_count = 0

            for s in students:
                if s["grade"] != "Fail":
                    pass_count += 1

            pass_percentage = (pass_count / len(students)) * 100

            print("\n===== STATISTICS DASHBOARD =====")
            print("Total Students:", len(students))
            print("Highest Marks:", highest)
            print("Lowest Marks:", lowest)
            print("Class Average:", round(average_class, 2))
            print("Pass Percentage:", round(pass_percentage, 2), "%")

    # EXIT
    elif choice == "7":

        print("👋 Exiting program...")
        break

    else:
        print("❌ Invalid choice. Try again.")


        
        
