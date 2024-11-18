package com.example.studentdatabase.db

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey

//make it a ROOM entity class and define table name
@Entity(tableName = "student_database" )
data class Student(


    //define database names according to best practices -@ColumnInfo
    //define student entities as constructor params
    @PrimaryKey //mark roll as primary key
    @ColumnInfo(name = "student_roll")
    var rollno: String,
    @ColumnInfo(name = "student_name")
    var name:String,
    @ColumnInfo(name = "student_marks")
    var marks:Int,
)
