package com.example.studentdatabase

import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.enableEdgeToEdge
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.studentdatabase.db.Student
import com.example.studentdatabase.db.StudentDatabase

class MainActivity : ComponentActivity() {
    private lateinit var rollNoEditText: EditText
    private lateinit var nameEditText: EditText
    private lateinit var marksEditText: EditText

    private lateinit var saveButton: Button
    private lateinit var clearButton: Button

    //create instance of student view model
    private lateinit var viewModel: StudentViewModel
    //get instance of viewModel using view model provider
        //1) pass instance of view model factory to viewmodel provider
        //to construct view model factory we need dao instance

    private lateinit var studentRecyclerView: RecyclerView
    private lateinit var adapter: StudentRecylerViewAdapter

    private lateinit var selectedStudent: Student
    private var isListItemClicked = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        rollNoEditText = findViewById(R.id.etRollNo)
        nameEditText = findViewById(R.id.etName)
        marksEditText = findViewById(R.id.etMarks)

        saveButton = findViewById(R.id.btnSave)
        clearButton = findViewById(R.id.btnClear)

        val dao = StudentDatabase.getInstance(application).studentDao()
        val factory = StudentViewModelFactory(dao)
        viewModel = ViewModelProvider(this,factory).get(StudentViewModel::class.java)

        studentRecyclerView = findViewById(R.id.rvStudent)

        saveButton.setOnClickListener{
            if(isListItemClicked){
                if (isInputValid()){
                    updateStudentData()
                    clearInput()
                } else {
                    Toast.makeText(this, "Please fill all fields", Toast.LENGTH_SHORT).show()
                }

            } else {
                if (isInputValid()) {
                    saveStudentData()
                    clearInput()
                } else {
                    // Optionally show a message to the user if fields are empty
                    Toast.makeText(this, "Please fill all fields", Toast.LENGTH_SHORT).show()
                }
            }
        }
        clearButton.setOnClickListener{
            if(isListItemClicked){
                deleteStudentData()
                clearInput()
            }
            clearInput()
        }
        initRecyclerView()

    }

    private fun isInputValid(): Boolean {
        val rollNo = rollNoEditText.text.toString()
        val name = nameEditText.text.toString()
        val marksString = marksEditText.text.toString()

        if (rollNo.isEmpty() || name.isEmpty() || marksString.isEmpty()) {
            return false
        }

        val marks = marksString.toIntOrNull()
        if (marks == null || marks < 0 || marks > 100) {
            marksEditText.error = "Marks should be between 0 and 100"
            return false
        }

        // Validate roll number format (sc200/0432/2022 format)
        val rollNoPattern = "sc\\d{3}/\\d{4}/\\d{4}"
        if (!rollNo.matches(Regex(rollNoPattern))) {
            rollNoEditText.error = "Invalid Roll No. Format: sc200/0432/2022"
            return false
        }

        // Validate name (should contain only letters, can adjust if needed)
        if (!name.matches(Regex("^[a-zA-Z ]+$"))) {
            nameEditText.error = "Name should contain only letters"
            return false
        }

        return true
    }

    private fun saveStudentData(){
        viewModel.insertStudent(
            Student(
                rollNoEditText.text.toString(),
                nameEditText.text.toString(),
                marksEditText.text.toString().toInt()
            )
        )
    }

    private fun updateStudentData(){
        viewModel.updateStudent(
            Student(
                rollNoEditText.text.toString(),
                nameEditText.text.toString(),
                marksEditText.text.toString().toInt()
            )
        )
        saveButton.text = "Save"
        clearButton.text = "Clear"
        isListItemClicked = false
    }

    private fun deleteStudentData(){
        viewModel.deleteStudent(
            Student(
                rollNoEditText.text.toString(),
                nameEditText.text.toString(),
                marksEditText.text.toString().toInt()
            )
        )
        saveButton.text = "Save"
        clearButton.text = "Clear"
        isListItemClicked = false
    }
    private fun clearInput(){
        rollNoEditText.setText("")
        nameEditText.setText("")
        marksEditText.setText("")
        saveButton.text = "Save"
        clearButton.text = "Clear"
        isListItemClicked = false
    }

    private fun initRecyclerView(){
        studentRecyclerView.layoutManager = LinearLayoutManager(this)
        adapter = StudentRecylerViewAdapter{
            selectedItem:Student -> listItemClicked(selectedItem)
        }
        studentRecyclerView.adapter = adapter
        displayStudentsList()
    }

    private fun displayStudentsList(){
        viewModel.students.observe(this) { students ->
            Log.i("Students","$students")
            adapter.setList(students)
            adapter.notifyDataSetChanged()
        }
    }

    private fun listItemClicked(student: Student){
//        Toast.makeText(
//            this,
//            "Student name is ${student.name}",
//            Toast.LENGTH_LONG
//        ).show()
        selectedStudent = student
        saveButton.text = "Update"
        clearButton.text = "Delete"
        isListItemClicked = true

        rollNoEditText.setText(selectedStudent.rollno)
        nameEditText.setText(selectedStudent.name)
        marksEditText.setText(selectedStudent.marks.toString())


    }
}

