package com.example.studentdatabase.db

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import kotlinx.coroutines.InternalCoroutinesApi
import kotlinx.coroutines.internal.synchronized

@Database(entities = [Student::class], version = 1 , exportSchema = false)
abstract class StudentDatabase:RoomDatabase() {
     //define function for DAO
    abstract fun studentDao():StudentDao

    //func to create DB Instance
    companion object{
        //marks JVM backing field of property as volatile
        //writes to the field are immediately visible to other threads
        @Volatile
        private var INSTANCE : StudentDatabase? = null

        //add context as param
        @OptIn(InternalCoroutinesApi::class)
        fun getInstance(context: Context):StudentDatabase{
            // execs given function block while holding monitor of given obj block
            //thread safety unlocking technique used in mission critical ops
            synchronized(this){
                var instance = INSTANCE
                if(instance==null){
                    instance = Room.databaseBuilder(
                        context.applicationContext,
                        StudentDatabase::class.java,
                        "student_database"
                        ).build()
                }
                return instance
            }

        }
    }
}