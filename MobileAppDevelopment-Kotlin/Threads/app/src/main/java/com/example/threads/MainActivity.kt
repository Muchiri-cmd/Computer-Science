package com.example.threads

import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.ImageView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.delay
import kotlinx.coroutines.withContext

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        val button1 = findViewById<Button>(R.id.btnImage1)
        val button2 = findViewById<Button>(R.id.btnImage2)

        button1.setOnClickListener{
            //run task in background thread
            //Dispatchers.IO - 4 background tasks
            CoroutineScope(Dispatchers.IO).launch{
                loadImage(R.drawable.gate1)
            }
        }

        button2.setOnClickListener{
            CoroutineScope(Dispatchers.IO).launch{
                loadImage(R.drawable.gate2)
            }
        }
        }

        private suspend fun loadImage(imgResource:Int){
            //we cant update UI from background thread i.e Dispatcher.IO
            // so we pass context effectively switching back to main Thread when updating UI
            Log.i("MyTag","Entering load Image function in ${Thread.currentThread()}.name")
            withContext(Dispatchers.Main){
                val image= findViewById<ImageView>(R.id.ivImage)
                image.setImageResource(imgResource)
                Log.i("MyTag","Loading image in ${Thread.currentThread().name} thread")
            }

        }
    }



