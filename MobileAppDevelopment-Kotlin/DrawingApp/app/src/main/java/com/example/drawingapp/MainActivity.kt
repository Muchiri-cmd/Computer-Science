package com.example.drawingapp

import android.graphics.Bitmap
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.Path
import android.os.Bundle
import android.view.MotionEvent
import android.widget.Button
import android.widget.ImageView
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
import androidx.compose.ui.semantics.Role.Companion.Button
import androidx.compose.ui.tooling.preview.Preview
import com.example.drawingapp.ui.theme.DrawingAppTheme

class MainActivity : ComponentActivity() {

    private lateinit var imageView: ImageView
    private lateinit var infoText: TextView
    private lateinit var eraseButton: Button
    private lateinit var resetButton: Button
    private var bitmap: Bitmap? = null
    private lateinit var canvas: Canvas
    private val paint: Paint = Paint()
    private val path: Path = Path()
    private var isEraserMode: Boolean = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        imageView = findViewById(R.id.imageView)
        infoText = findViewById(R.id.tvInfo)
        eraseButton = findViewById(R.id.btnErase)
        resetButton = findViewById(R.id.btnReset)

        // Initialize the paint for drawing
        paint.apply {
            color = Color.BLUE
            isAntiAlias = true
            style = Paint.Style.STROKE
            strokeWidth = 8f
        }

        resetButton.setOnClickListener{
            bitmap = Bitmap.createBitmap(
                imageView.width,
                imageView.height,
                Bitmap.Config.ARGB_8888
            )
            canvas = Canvas(bitmap!!)
            imageView.setImageBitmap(bitmap) // Update the ImageView
            path.reset()
        }

        eraseButton.setOnClickListener{
            toggleEraser()
        }

    }

    private fun drawSketchImage() {
        if (bitmap == null) {
            bitmap = Bitmap.createBitmap(
                imageView.width,
                imageView.height,
                Bitmap.Config.ARGB_8888
            )
            canvas = Canvas(bitmap!!)
            imageView.setImageBitmap(bitmap)
        }
        // Draw the path on the canvas
        canvas.drawPath(path, paint)
        imageView.invalidate()
    }

    override fun onTouchEvent(event: MotionEvent): Boolean {
        val x = event.x
        val y = event.y

        when (event.action) {
            MotionEvent.ACTION_DOWN -> {
                path.moveTo(x, y)
            }

            MotionEvent.ACTION_MOVE -> {
                path.lineTo(x, y)
                drawSketchImage()
            }

            MotionEvent.ACTION_UP -> {
                path.lineTo(x, y)
                drawSketchImage()
                path.reset() // Reset the path for the next stroke
            }
        }

        return true // Indicate event was handled
    }
    private fun toggleEraser() {
        isEraserMode = !isEraserMode
        if (isEraserMode){
            eraseButton.text = "Draw "
            infoText.text = "You are in erase mode.\nDrag finger or stylus to erase"
//            Toast.makeText(this,"You are in erase mode.\\nDrag finger or stylus to erase\"",Toast.LENGTH_LONG).show()
        } else {
            eraseButton.text = "Erase "
            infoText.text ="You are in draw mode.\nDrag finger/stylus to draw"
//            Toast.makeText(this,"You are in erase mode.\\nDrag finger or stylus to erase\"",Toast.LENGTH_LONG).show()
        }
        paint.apply {
            if (isEraserMode) {
                color = Color.WHITE // Match the background color
                strokeWidth = 30f // Make the eraser wider
            } else {
                color = Color.BLUE // Reset to drawing color
                strokeWidth = 8f
            }
        }
    }
}

