package com.example.khai_mobile_lab

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.EditText
import android.widget.TextView
import androidx.core.widget.doOnTextChanged

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        loadUI()
    }

    private fun loadUI() {
        val editText = findViewById<EditText>(R.id.editTextTextPersonName)
        val textView = findViewById<TextView>(R.id.textView)
        val textSize = 40
        textView.textSize = textSize.toFloat()
        textView.text = ""

        editText.doOnTextChanged { text, start, before, count ->
            if(text != null && text.length > 0) {
                textView.text = text
            } else {
                textView.text =  ""
            }

        }
    }
}