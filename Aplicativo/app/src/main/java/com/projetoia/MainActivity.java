package com.projetoia;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void openMembers(View view) {
        Intent membersIntent = new Intent(getApplicationContext(), MembersActivity.class);
        //membersIntent.putExtra("key", value); // extra parameters
        startActivity(membersIntent);
    }
}