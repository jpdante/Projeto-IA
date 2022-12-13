package com.projetoia;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.util.Base64;
import android.view.View;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.Toast;

import com.google.gson.Gson;
import com.projetoia.core.CustomAdapter;
import com.projetoia.model.ResponseItem;
import com.projetoia.model.ResponseModel;

public class ResponseActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_response);

        Intent intent = getIntent();
        String extraData = intent.getStringExtra("response");

        Gson gson = new Gson();
        ResponseModel response = gson.fromJson(extraData, ResponseModel.class);
        if (!response.status) {
            Toast.makeText(this, "Falha ao processar arquivo.", Toast.LENGTH_LONG);
            finish();
        }

        ImageView imageView = findViewById(R.id.imageView);
        byte[] decodedString = Base64.decode(response.data.image, Base64.DEFAULT);
        Bitmap decodedByte = BitmapFactory.decodeByteArray(decodedString, 0, decodedString.length);
        imageView.setImageBitmap(decodedByte);

        ListView listView = findViewById(R.id.listView);
        response.data.items.add(0, new ResponseItem("Índice", "Predição", "Classifação"));
        listView.setAdapter(new CustomAdapter(response.data.items,this));
    }

    public void goBack(View view) {
        finish();
    }
}