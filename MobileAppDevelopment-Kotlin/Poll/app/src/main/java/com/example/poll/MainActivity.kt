package com.example.poll

import android.os.Bundle
import android.provider.MediaStore.Audio.Radio
import android.view.View
import android.widget.Button
import android.widget.RadioButton
import android.widget.TextView
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.RadioButton
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.example.poll.ui.theme.PollTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        val button = findViewById<Button>(R.id.button)
        val tvChoice = findViewById<TextView>(R.id.tvChoice)

        val rdbExcellent = findViewById<RadioButton>(R.id.rdbExcellent)
        val rdbGood = findViewById<RadioButton>(R.id.rdbGood)
        val rdbAverage = findViewById<RadioButton>(R.id.rdbAverage)
        val rdbPoor = findViewById<RadioButton>(R.id.rdbPoor)

        button.setOnClickListener{
            if (rdbExcellent.isChecked || rdbAverage.isChecked || rdbGood.isChecked || rdbPoor.isChecked) {
                tvChoice.text = "Thanks for your valued feedback"
                Toast.makeText(this, "Poll Submitted Successfully", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "Please select a rating before submitting", Toast.LENGTH_SHORT).show()
            }
        }
    }

    fun onRadioButtonClicked(view: View){
        val checked = (view as RadioButton).isChecked
        var str = ""

        when (view.id){
            R.id.rdbExcellent -> {
                str = "You selected Excellent"
            }
            R.id.rdbGood -> {
                str = "You selected Good"
            }
            R.id.rdbAverage -> {
                str = "You selected Average"
            }
            R.id.rdbPoor -> {
                str = "You selected Poor"
            }
        }
        Toast.makeText(view.context,str,Toast.LENGTH_SHORT).show()
    }

}
