package com.example.khai_mobile_lab

import android.content.Context
import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.hardware.SensorManager
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView

class MainActivity : AppCompatActivity(), SensorEventListener {
    private lateinit var sensorManager: SensorManager
    private var SENSOR_ACCELEROMETER: Sensor ?= null
    private var SENSOR_GYROSCOPE: Sensor ?= null
    private var SENSOR_LIGHT: Sensor ?= null

    private var resume = true


    override fun onAccuracyChanged(sensor: Sensor?, accuracy: Int) {
        return
    }

    override fun onSensorChanged(event: SensorEvent?) {
        if (event != null && resume) {

            when(event.sensor.type) {
                Sensor.TYPE_ACCELEROMETER -> findViewById<TextView>(R.id.accelerometer).text = event.values[0].toString()
                Sensor.TYPE_GYROSCOPE -> findViewById<TextView>(R.id.gyroscope).text = event.values[0].toString()
                Sensor.TYPE_LIGHT -> findViewById<TextView>(R.id.light).text = event.values[0].toString()
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        sensorManager = getSystemService(Context.SENSOR_SERVICE) as SensorManager

        loadSensors()
        onResume()
    }

    private fun loadSensors() {
        SENSOR_ACCELEROMETER = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)
        SENSOR_GYROSCOPE = sensorManager.getDefaultSensor(Sensor.TYPE_GYROSCOPE)
        SENSOR_LIGHT = sensorManager.getDefaultSensor(Sensor.TYPE_LIGHT)
    }

    override fun onResume() {
        super.onResume()
        sensorManager.registerListener(this, SENSOR_ACCELEROMETER, SensorManager.SENSOR_DELAY_NORMAL)
        sensorManager.registerListener(this, SENSOR_GYROSCOPE, SensorManager.SENSOR_DELAY_NORMAL)
        sensorManager.registerListener(this, SENSOR_LIGHT, SensorManager.SENSOR_DELAY_NORMAL)
    }
    override fun onPause() {
        super.onPause()
        sensorManager.unregisterListener(this)
    }
}