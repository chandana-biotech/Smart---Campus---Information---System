import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set up page configuration for the website
st.set_page_config(page_title="Smart Campus Information System", layout="wide")

# Initialize persistent session states for internal records if they don't exist
if "all_courses" not in st.session_state:
    st.session_state.all_courses = []  # For Lab 2

if "student_records" not in st.session_state:
    # Pre-populate with exactly Lab 3 data
    st.session_state.student_records = [
        {"name": "Priya", "age": 20, "grades": [85, 90, 78]},
        {"name": "Rahul", "age": 21, "grades": [72, 88, 91]},
        {"name": "Anita", "age": 19, "grades": [95, 89, 92]}
    ]

# --- LAB 7 USER-DEFINED EXCEPTION ---
class MissingFileOrFolderError(Exception):
    """Raised when a required file or folder is missing in the directory."""
    pass

# --- MAIN DASHBOARD NAVIGATION ---
st.title("🏫 Smart Campus Information System Dashboard")
st.write("Welcome to the integrated Dayananda Sagar College of Engineering Academic Management Portal.")
st.markdown("---")

# Sidebar navigation menu matching the 8 Labs
menu = [
    "1. Student Registration & Grades",
    "2. Course Enrollment Management",
    "3. Student Record Data Management",
    "4. Sorting & Searching IDs",
    "5. Student Fee Calculation",
    "6. File Handling (Academic Records)",
    "7. Directory Scanning (Exceptions)",
    "8. Student Performance Analytics"
]
choice = st.sidebar.selectbox("Navigate Functional Modules", menu)

st.sidebar.markdown("---")
st.sidebar.info("Developed via Python Laboratory Experiments 1 to 8.")


# =====================================================================
# LAB 1: STUDENT REGISTRATION AND GRADE EVALUATION
# =====================================================================
if choice == "1. Student Registration & Grades":
    st.header("📝 Student Registration and Grade Evaluation")
    st.write("Evaluate performance marks using conditional statements.")
    
    # Form input collection
    with st.form("lab1_form"):
        student_name = st.text_input("Enter student name:")
        score_input = st.number_input("Enter exam score (0-100):", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
        submit_btn = st.form_submit_button("Evaluate Grade")
        
    if submit_btn and student_name:
        score = float(score_input)
        # Exact logic and syntax from Lab 1
        if score >= 90 and score <= 100:
            grade = "A"
            remark = "Excellent"
        elif score >= 75:
            grade = "B"
            remark = "Very Good"
        elif score >= 60:
            grade = "C"
            remark = "Good"
        elif score >= 40:
            grade = "D"
            remark = "Average"
        else:
            grade = "F"
            remark = "Needs Improvement"
            
        # Output Display
        st.subheader("--- Student Report ---")
        st.write(f"**Name:** {student_name}")
        st.write(f"**Score:** {score}")
        st.write(f"**Grade:** {grade}")
        st.write(f"**Performance Remark:** {remark}")


# =====================================================================
# LAB 2: COURSE ENROLLMENT MANAGEMENT SYSTEM
# =====================================================================
elif choice == "2. Course Enrollment Management":
    st.header("📚 Course Enrollment Management System")
    max_courses = 5
    
    st.write(f"Add courses for a student. (Maximum limit: {max_courses} courses)")
    
    # Show current course counts
    current_count = len(st.session_state.all_courses)
    st.info(f"Total courses currently enrolled: {current_count} / {max_courses}")
    
    if current_count >= max_courses:
        st.warning("Maximum course limit reached! You cannot add more courses.")
    else:
        # Form for course entry mimicking the continuous collection iteration
        with st.form("lab2_form", clear_on_submit=True):
            course_name = st.text_input("Enter course name:")
            credits_raw = st.text_input("Enter credit value:")
            add_btn = st.form_submit_button("Add Course")
            
        if add_btn:
            # Validation using loop-like checks with skip notifications
            if not course_name or course_name.strip().lower() == "done":
                st.error("Invalid course name!")
            elif not credits_raw.isdigit():
                st.error("Invalid credit value! Skipping entry...")
            else:
                credits = int(credits_raw)
                if credits <= 0:
                    st.error("Credit must be positive! Skipping entry...")
                else:
                    # Valid entry -> add to list
                    st.session_state.all_courses.append((course_name, credits))
                    st.success(f"Course '{course_name}' with {credits} credits added.")
                    st.rerun()

    # Clear button to reset
    if st.button("Reset Enrolled Courses"):
        st.session_state.all_courses = []
        st.rerun()

    # Output Display
    st.subheader("--- Enrollment Report ---")
    if st.session_state.all_courses:
        for course, credit in st.session_state.all_courses:
            st.write(f"🔹 **Course:** {course} | **Credits:** {credit}")
        st.write(f"**Total courses enrolled:** {len(st.session_state.all_courses)}")
    else:
        st.write("*No courses enrolled yet.*")


# =====================================================================
# LAB 3: STUDENT RECORD DATA MANAGEMENT USING DATA STRUCTURES
# =====================================================================
elif choice == "3. Student Record Data Management":
    st.header("🗂️ Student Record Data Management using Data Structures")
    
    # 1. Record Management Display (Lists & Dictionaries)
    st.subheader("Student Records")
    for student in st.session_state.student_records:
        st.write(f"**Name:** {student['name']}")
        st.write(f"**Age:** {student['age']}")
        st.write(f"**Grades:** {student['grades']}")
        st.write("---")
        
    # 2. Event Participation Analysis using Sets
    st.subheader("Event Participation Analysis")
    
    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}
    
    st.write(f"**Event A Participants:** {event_A}")
    st.write(f"**Event B Participants:** {event_B}")
    
    # Set calculations exactly as requested
    common_participants = event_A & event_B
    all_participants = event_A | event_B
    only_event_A = event_A - event_B
    
    st.markdown("#### Operations Results:")
    st.write(f"🤝 **Common Participants (Intersection):** {common_participants}")
    st.write(f"🌍 **All Participants (Union):** {all_participants}")
    st.write(f"🎯 **Only Event A Participants (Difference):** {only_event_A}")


# =====================================================================
# LAB 4: SORTING AND SEARCHING OF STUDENT IDS
# =====================================================================
elif choice == "4. Sorting & Searching IDs":
    st.header("🔍 Sorting and Searching of Student IDs")
    
    # Initial array raw list
    student_ids_base = [105, 102, 110, 108, 101, 115]
    st.write(f"**Original list of IDs:** {student_ids_base}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Bubble Sort Implementation")
        arr_bubble = list(student_ids_base)
        n = len(arr_bubble)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr_bubble[j] > arr_bubble[j+1]:
                    temp = arr_bubble[j]
                    arr_bubble[j] = arr_bubble[j+1]
                    arr_bubble[j+1] = temp
        st.success(f"Sorted IDs (Bubble Sort): {arr_bubble}")
        
    with col2:
        st.subheader("2. Selection Sort Implementation")
        arr_select = list(student_ids_base)
        n2 = len(arr_select)
        for i in range(n2):
            min_index = i
            for j in range(i+1, n2):
                if arr_select[j] < arr_select[min_index]:
                    min_index = j
            temp = arr_select[i]
            arr_select[i] = arr_select[min_index]
            arr_select[min_index] = temp
        st.success(f"Sorted IDs (Selection Sort): {arr_select}")

    st.markdown("---")
    st.subheader("Search Engine Operations")
    
    # Interactive search inputs using the bubble sorted list
    sorted_arr = arr_bubble
    target_id = st.number_input("Enter Student ID to Search for:", min_value=100, max_value=120, value=108)
    
    # Linear Search
    found_index_linear = -1
    for i in range(len(sorted_arr)):
        if sorted_arr[i] == target_id:
            found_index_linear = i
            break
            
    # Binary Search
    low = 0
    high = len(sorted_arr) - 1
    found_index_binary = -1
    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == target_id:
            found_index_binary = mid
            break
        elif sorted_arr[mid] < target_id:
            low = mid + 1
        else:
            high = mid - 1
            
    # Output display for searches
    if found_index_linear != -1:
        st.write(f"🟢 **Linear Search:** ID {target_id} found at index `{found_index_linear}`")
    else:
        st.write("🔴 **Linear Search:** ID not found")
        
    if found_index_binary != -1:
        st.write(f"🟢 **Binary Search:** ID {target_id} found at index `{found_index_binary}`")
    else:
        st.write("🔴 **Binary Search:** ID not found")


# =====================================================================
# LAB 5: STUDENT FEE CALCULATION USING FUNCTIONS
# =====================================================================
elif choice == "5. Student Fee Calculation":
    st.header("💰 Student Fee Calculation using Functions")
    
    # Exact Core Function logic with default parameter settings
    def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
        total_fee = tuition_fee + hostel_fee + transportation_fee
        return total_fee

    st.write("Adjust configuration values below to evaluate custom fee structures:")
    
    t_fee = st.number_input("Tuition Fee charges (Required):", value=50000, step=5000)
    include_hostel = st.checkbox("Include Hostel Accommodations Structure")
    include_transport = st.checkbox("Include Transportation Route Mapping")
    
    h_fee = st.number_input("Hostel Fee:", value=30000 if include_hostel else 0, step=2000, disabled=not include_hostel)
    trans_fee = st.number_input("Transportation Fee:", value=10000 if include_transport else 0, step=1000, disabled=not include_transport)
    
    calculated_total = calculate_fee(t_fee, hostel_fee=h_fee, transportation_fee=trans_fee)
    
    st.markdown("### Runtime Output Displays")
    st.info(f"**Total Generated Calculation Summary Fee Structure Charges:** ₹{calculated_total}")
    
    # Print programmatic cases exact demonstration matching output records
    st.markdown("#### Test Baseline Output Benchmarks:")
    st.text(f"Case 1 (Tuition only [50k baseline]): {calculate_fee(50000)}")
    st.text(f"Case 2 (Tuition [5k] + Hostel [30k]): {calculate_fee(5000, 30000)}")
    st.text(f"Case 3 (Tuition [50k] + Hostel [30k] + Transport [10k]): {calculate_fee(50000, 30000, 10000)}")


# =====================================================================
# LAB 6: FILE HANDLING FOR STUDENT ACADEMIC RECORDS
# =====================================================================
elif choice == "6. File Handling (Academic Records)":
    st.header("💾 File Handling for Student Academic Records")
    
    filename = "student_records.txt"
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Step 1: Write details to File")
        if st.button("Generate & Write Records File"):
            with open(filename, "w") as file:
                file.write("ID, Name, Marks\n")
                file.write("101, Arjun,85\n")
                file.write("102, Meera,92\n")
                file.write("103, Ravi,76\n")
                file.write("104, Anita,89\n")
            st.success("Student records written to file successfully ('student_records.txt').")

    with col2:
        st.subheader("Step 2: Read records from File")
        if os.path.exists(filename):
            if st.button("Read Stored Records"):
                st.text("Reading stored records raw output:")
                with open(filename, "r") as file:
                    records = file.readlines()
                for record in records:
                    st.text(record.strip())
        else:
            st.warning("File must be generated via the left button block first.")

    st.markdown("---")
    st.subheader("Step 3: Process stored data to generate a simple report")
    
    if os.path.exists(filename):
        if st.button("Execute Report Data Engine Processing"):
            with open(filename, "r") as file:
                records = file.readlines()
                
            total_students = 0
            total_marks = 0
            highest_marks = -1
            top_student = ""
            
            # Processing lines while skipping header record exactly
            for record in records[1:]:
                parts = record.strip().split(",")
                if len(parts) == 3:
                    student_id = parts[0]
                    name = parts[1]
                    marks = int(parts[2])
                    
                    total_students += 1
                    total_marks += marks
                    
                    if marks > highest_marks:
                        highest_marks = marks
                        top_student = name
                        
            if total_students > 0:
                average_marks = total_marks / total_students
                
                st.markdown("#### Generated Report Summary Output:")
                st.write(f"📊 **Total Registered Students Count:** {total_students}")
                st.write(f"📈 **Average Score Accumulation:** {average_marks:.2f}")
                st.write(f"🏆 **Top Performer Profile:** {top_student} with `{highest_marks}` marks")
    else:
        st.info("Awaiting file writing activation sequence parameters.")


# =====================================================================
# LAB 7: DIRECTORY SCANNING WITH EXCEPTION HANDLING
# =====================================================================
elif choice == "7. Directory Scanning (Exceptions)":
    st.header("📁 Directory Scanning with Exception Handling")
    st.write("Scan system repository file pathways while managing error boundaries cleanly.")

    # Input entry path string
    directory_path = st.text_input("Enter local directory paths destination block scanner targets:", value="Projects")
    
    # Utility button to automatically mock-setup folders matching PDF sample cases
    if st.button("Setup Default Sample Simulation Project Folder Structure"):
        os.makedirs("Projects/Student1", exist_ok=True)
        os.makedirs("Projects/Student2", exist_ok=True)
        os.makedirs("Projects/EmptyFolder", exist_ok=True)
        with open("Projects/Student1/report.docx", "w") as f: f.write("Mock Document Data")
        with open("Projects/Student2/code.py", "w") as f: f.write("# Mock Python Data")
        st.success("Simulated structural tree 'Projects/' context paths map successfully drafted locally!")

    if st.button("Execute Structural Directory Scanning Run"):
        # Functional implementation strictly containing Try-Except boundaries mapping
        try:
            if not os.path.exists(directory_path):
                raise FileNotFoundError(f"Invalid directory path: {directory_path}")
                
            st.markdown(f"**Scanning directory structural records:** `{directory_path}`")
            
            # Walking through configuration structures tree records mapping
            for root, dirs, files in os.walk(directory_path):
                level = root.replace(directory_path, "").count(os.sep)
                indent = "    " * level
                st.text(f"{indent} {os.path.basename(root)}/")
                
                sub_indent = "    " * (level + 1)
                for f in files:
                    st.text(f"{sub_indent} {f}")
                    
                # Raise custom structural errors if empty matching validation profiles rule blocks
                if not files and not dirs:
                    raise MissingFileOrFolderError(f"Empty folder detected: {root}")
                    
        except FileNotFoundError as e:
            st.error(f"**Error:** {e}")
        except MissingFileOrFolderError as e:
            st.warning(f"**Custom Error Exception Caught:** {e}")
        except Exception as e:
            st.error(f"**Unexpected Error:** {e}")


# =====================================================================
# LAB 8: STUDENT PERFORMANCE ANALYSIS (NUMPY, PANDAS, MATPLOTLIB)
# =====================================================================
elif choice == "8. Student Performance Analytics":
    st.header("📊 Student Performance Analysis Engine")
    
    csv_filename = "student_performance.csv"
    
    # Utility template drafting tool block for smooth standalone operation executions
    if st.button("Generate Default CSV Dataset Template"):
        mock_df = pd.DataFrame({
            "Name": ["Arjun", "Meera", "Ravi", "Anita", "Priya", "Rahul"],
            "Math": [85, 92, 76, 89, 95, 72],
            "Science": [78, 88, 82, 91, 89, 85],
            "English": [90, 84, 80, 88, 92, 79]
        })
        mock_df.to_csv(csv_filename, index=False)
        st.success("Default database layout 'student_performance.csv' file compiled effectively!")

    st.markdown("---")
    
    try:
        # Load performance records sequence pipeline dataset configurations
        df = pd.read_csv(csv_filename)
        
        st.subheader("--- Raw CSV Database Profile Data Grid ---")
        st.dataframe(df.head())
        
        st.subheader("--- Pandas Statistical Analysis Matrix Summary (`.describe()`) ---")
        st.dataframe(df.describe())
        
        # Numeric conversions transformation pipeline parsing configurations matrix
        scores = df[["Math", "Science", "English"]].to_numpy()
        
        # NumPy Operations processing array configurations metrics loops bounds parameters
        mean_scores = np.mean(scores, axis=0)
        median_scores = np.median(scores, axis=0)
        std_dev_scores = np.std(scores, axis=0)
        
        st.subheader("--- NumPy Matrix Arithmetic Output Core Insights ---")
        st.write(f"**Mean Scores (Math, Science, English subjects):** `{mean_scores}`")
        st.write(f"**Median Evaluation Scores (Math, Science, English):** `{median_scores}`")
        st.write(f"**Standard Deviation Vector Metrics (Math, Science, English):** `{std_dev_scores}`")
        
        # Identifying Top performers configurations limits matching pandas queries criteria
        top_math = df.loc[df["Math"].idxmax(), "Name"]
        top_science = df.loc[df["Science"].idxmax(), "Name"]
        top_english = df.loc[df["English"].idxmax(), "Name"]
        
        st.subheader("--- Top Performance Profile Matrix Insights ---")
        st.success(f"🧮 **Mathematics Subject Champion:** {top_math}")
        st.success(f"🔬 **Science Subject Champion:** {top_science}")
        st.success(f"🇬🇧 **English Subject Champion:** {top_english}")
        
        st.markdown("---")
        st.subheader("📊 Analytical Graphical Render Plots Visualization Reports")
        
        fig_col1, fig_col2 = st.columns(2)
        
        with fig_col1:
            # Chart Rendering Block One: Subject Averages Data Mapping Configurations Matrix
            fig, ax = plt.subplots()
            subjects = ["Math", "Science", "English"]
            ax.bar(subjects, mean_scores, color=["blue", "green", "orange"])
            ax.set_title("Average Scores per Subject")
            ax.set_xlabel("Subjects")
            ax.set_ylabel("Average Score")
            st.pyplot(fig)
            
        with fig_col2:
            # Chart Rendering Block Two: Complete student structural comparative review plots
            fig2, ax2 = plt.subplots()
            df.plot(x="Name", y=["Math", "Science", "English"], kind="bar", ax=ax2)
            ax2.set_title("Student Performance Comparison")
            ax2.set_ylabel("Scores")
            plt.xticks(rotation=45)
            st.pyplot(fig2)
            
    except FileNotFoundError:
        st.error("🔴 **Error:** The CSV file 'student_performance.csv' was not found. Please click the button above to generate a default dataset.")
    except Exception as e:
        st.error(f"🔴 **Unexpected Structural Matrix Processing Failure:** {e}")