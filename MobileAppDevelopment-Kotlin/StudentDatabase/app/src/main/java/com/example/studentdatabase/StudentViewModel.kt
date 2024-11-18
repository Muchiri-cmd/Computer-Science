package com.example.studentdatabase

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.studentdatabase.db.Student
import com.example.studentdatabase.db.StudentDao
import kotlinx.coroutines.launch

class StudentViewModel (private val dao:StudentDao): ViewModel(){
    //2 receive list of saved student instances - observe live data from main activity
    val students = dao.getAllStudents()

    //func to save,update & delete student data to database
    fun insertStudent(student: Student)=viewModelScope.launch {
        dao.insertStudent(student)
    }

    fun updateStudent(student: Student)=viewModelScope.launch {
        dao.updateStudent(student)
    }

    fun deleteStudent(student: Student)=viewModelScope.launch {
        dao.deleteStudent(student)
    }


}