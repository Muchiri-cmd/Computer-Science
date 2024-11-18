package com.example.studentdatabase

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.studentdatabase.db.Student

class StudentRecylerViewAdapter(
    private val clickListener:(Student) -> Unit
):RecyclerView.Adapter<StudentViewHolder>(){
    private val studentsList = ArrayList<Student>()

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): StudentViewHolder {
       val layoutInflater = LayoutInflater.from(parent.context)
        val listItem = layoutInflater.inflate(R.layout.list_item,parent,false)
        return StudentViewHolder(listItem)
    }

    override fun onBindViewHolder(holder: StudentViewHolder, position: Int) {
        holder.bind(studentsList[position],clickListener)
    }

    override fun getItemCount(): Int {
        return studentsList.size
    }

    fun setList(students: List<Student>){
        studentsList.clear()
        studentsList.addAll(students)
    }
}

//view holder class
class StudentViewHolder(private val view: View):RecyclerView.ViewHolder(view){
    fun bind(student:Student, clickListener:(Student) -> Unit ){
        val rollListTextView = view.findViewById<TextView>(R.id.tvListRoll)
        val nameListTextView = view.findViewById<TextView>(R.id.tvListName)
        val marksListTextView = view.findViewById<TextView>(R.id.tvListMarks)

        rollListTextView.text = "Roll Number : ${student.rollno}"
        nameListTextView.text = "Name : ${student.name}"
        marksListTextView.text = "Marks : ${student.marks}"


        view.setOnClickListener{
            clickListener(student)
        }

    }
}