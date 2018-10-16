# 473_grading_scripts

- Place the students submission as downloaded from canvas in a directory `student_submission_dir`.
- run `python ./grading_scripts/uncanvas.py ./student_submission_dir/`
	- Ensure that the  `student_submission_dir` has child direcotries with each student's submission.
	- If a student has submitted a `.tar` or a `.zip` file, manually untar/unzip the folder and create a similar child folder with the student's submission.
- Place the project source code in another directory. (Same level as the student submission directory)
- run `python ./grading_scripts/grade.py ./project_source_dir/ ./student_submission_dir/`
	- This should run the autograder on each student's submission and create a .txt file in the `student_submission_dir` for each student with the autograder's output.
- run `python ./grading_scripts/format_grade.py project_num ./student_submission_dir/`
	- This should print the final grades for each student in the terminal (sorted by student name).