package com.example.studentdatabase

import androidx.lifecycle.ViewModel
import com.example.studentdatabase.db.StudentDao
import androidx.lifecycle.ViewModelProvider

class StudentViewModelFactory (
    private val dao:StudentDao
):ViewModelProvider.Factory {
    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        if(modelClass.isAssignableFrom(StudentViewModel::class.java)){
            return StudentViewModel(dao) as T
        }
        throw IllegalArgumentException("Unknown view model class")
    }
}
