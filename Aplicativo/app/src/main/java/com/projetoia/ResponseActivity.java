package com.projetoia;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import com.google.gson.Gson;

import java.util.ArrayList;

public class ResponseActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_response);

        Intent intent = getIntent();
        String extraData = intent.getStringExtra("response");

        Gson gson = new Gson();
        ResponseModel response = gson.fromJson(extraData, ResponseModel.class);

        ListView l = findViewById(R.id.listView);
        l.setAdapter(new CustomAdapter(response.Items,this));
    }
}