package com.example.gradingapp

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.example.gradingapp.ui.theme.GradingAppTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        val cat1 = findViewById<EditText>(R.id.etCat1)
        val cat2 = findViewById<EditText>(R.id.etCat2)
        val mainExam = findViewById<EditText>(R.id.etMain)

        val gradeButton = findViewById<Button>(R.id.btnCalculate)
        val resetButton = findViewById<Button>(R.id.btnReset)
        val gradeTextView = findViewById<TextView>(R.id.tvGrade)
        val averageTextView = findViewById<TextView>(R.id.tvAverage)

        gradeButton.setOnClickListener{
            calculateGrade(cat1,cat2,mainExam,averageTextView,gradeTextView)
        }
        resetButton.setOnClickListener{
            resetFields(cat1,cat2,mainExam,averageTextView,gradeTextView)
        }

    }

    private fun calculateGrade(cat1:EditText,cat2:EditText,mainExam:EditText,
                               average:TextView,grade:TextView){

        if (cat1.text.isEmpty() || cat2.text.isEmpty() || mainExam.text.isEmpty()) {
            Toast.makeText(this, "Please enter marks for all exams", Toast.LENGTH_SHORT).show()
            return
        }

        val marks1 = cat1.text.toString().toIntOrNull() ?: 0
        val marks2 = cat2.text.toString().toIntOrNull() ?: 0
        val mainMarks = mainExam.text.toString().toIntOrNull() ?: 0

        if (marks1 > 20 || marks2 > 20) {
            Toast.makeText(this, "CAT marks cannot exceed 20.", Toast.LENGTH_SHORT).show()
            return
        }

        if (mainMarks > 60) {
            Toast.makeText(this, "Main Exam marks cannot exceed 60.", Toast.LENGTH_SHORT).show()
            return 
        }

        val total = marks1 + marks2 + mainMarks
        val avg = total / 1.0

        val gradeValue = when {
            total < 25 -> "F"
            total in 25..44 -> "E"
            total in 45..49 -> "D"
            total in 50..59 -> "C"
            total in 60..79 -> "B"
            else -> "A"
        }

        average.text = "Your Average is : %.2f".format(avg)
        grade.text = " $gradeValue"

    }
    private fun resetFields(
        cat1:EditText,
        cat2:EditText,
        mainExam: EditText,
        average: TextView,
        grade:TextView
    ){
        cat1.text.clear()
        cat2.text.clear()
        mainExam.text.clear()

        average.text = ""
        grade.text = ""

        Toast.makeText(this, "Fields have been reset.", Toast.LENGTH_SHORT).show()

    }
}
