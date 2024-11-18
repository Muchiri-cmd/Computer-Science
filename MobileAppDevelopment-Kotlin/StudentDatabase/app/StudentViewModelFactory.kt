package com.example.studentdatabase

import com.example.studentdatabase.db.StudentDao
import androidx.lifecycle.ViewModelProvider

class StudentViewModelFactory (
    private val dao:StudentDao
):ViewModelProvider.Factory{

}
