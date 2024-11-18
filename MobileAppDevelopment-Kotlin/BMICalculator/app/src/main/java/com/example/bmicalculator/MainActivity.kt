package com.example.bmicalculator

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
import androidx.core.content.ContextCompat
import com.example.bmicalculator.ui.theme.BMICalculatorTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        val weightText = findViewById<EditText>(R.id.etWeight)
        val heightText = findViewById<EditText>(R.id.etHeight)
        val calcBtn = findViewById<Button>(R.id.btnCalculate)

        calcBtn.setOnClickListener {
            val weight = weightText.text.toString()
            val height = heightText.text.toString()

            if(validateInput(weight,height)){
                //calculate BMI

                val bmi = weight.toFloat()/((height.toFloat()/100) * (height.toFloat()/100) )
                val bmi2dp = String.format("%.2f",bmi).toFloat()
                displayResults(bmi2dp)
            }
        }
    }

    private fun validateInput(weight:String?,height:String):Boolean{
        return when{
            weight.isNullOrEmpty() -> {
                Toast.makeText(this,"Please input weight",Toast.LENGTH_LONG).show()
                return false
            }
            height.isNullOrEmpty()-> {
                Toast.makeText(this,"Please input height",Toast.LENGTH_LONG).show()
                return false
            }
            else -> {
                return true
            }
        }
    }
    private fun displayResults(bmi:Float){
        val resultIndex = findViewById<TextView>(R.id.tvIndex)
        val resultDescription = findViewById<TextView>(R.id.tvResult)
        val info = findViewById<TextView>(R.id.tvInfo)

        resultIndex.text = bmi.toString()
        info.text = "(Normal range is 18.5 - 24.9)"

        var resultText = ""
        var color = 0

        when{
            bmi<18.50 -> {
                resultText = "Underweight"
                color=R.color.under_weight
            }
            bmi in 18.50..24.99->{
                resultText ="Fit"
                color = R.color.fit
            }
            bmi in 25.00..29.99->{
                resultText="Overweight"
                color=R.color.over_weight
            }
            bmi > 29.99->{
                resultText="Obese"
                color=R.color.obese
            }
        }

        resultDescription.setTextColor(ContextCompat.getColor(this,color))
        resultDescription.text=resultText
    }
}

