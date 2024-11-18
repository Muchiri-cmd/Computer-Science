package com.example.emailproject

import android.content.Intent
//import android.net.Uri
import android.os.Bundle
//import android.provider.ContactsContract.CommonDataKinds.Email
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

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

        val btnSubmit = findViewById<Button>(R.id.button)
        btnSubmit.setOnClickListener {
            val email = findViewById<EditText>(R.id.eMail).text.toString()
            val subject = findViewById<EditText>(R.id.etSubject).text.toString()
            val message = findViewById<EditText>(R.id.etMessageBody).text.toString()

            sendEmail(email, subject, message)
        }

    }
    private fun sendEmail(email: String, subject: String, message: String) {
        // Create an intent to open the email app
        val emailIntent = Intent(Intent.ACTION_SEND).apply {
            type = "message/rfc822"  // Specifies email clients only
            putExtra(Intent.EXTRA_EMAIL, arrayOf(email))  // Sets the "To" field
            putExtra(Intent.EXTRA_SUBJECT, subject)  // Sets the "Subject" field
            putExtra(Intent.EXTRA_TEXT, message)  // Sets the "Body" field
        }

        // Try to start the email client
        try {
            startActivity(Intent.createChooser(emailIntent, "Send email"))
        } catch (e: Exception) {
            Toast.makeText(this, "No email app found", Toast.LENGTH_LONG).show()
        }
    }

}