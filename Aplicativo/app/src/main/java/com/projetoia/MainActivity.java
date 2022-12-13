package com.projetoia;

import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.concurrent.TimeUnit;

import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {

    private ActivityResultLauncher<Intent> someActivityResultLauncher;
    private Uri currentPath = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        this.someActivityResultLauncher = registerForActivityResult(
                new ActivityResultContracts.StartActivityForResult(),
                result -> {
                    TextView filePathText = (TextView) findViewById(R.id.filePathText);
                    Button uploadFileBtn = (Button) findViewById(R.id.uploadFileBtn);
                    if (result.getResultCode() == Activity.RESULT_OK) {
                        Intent data = result.getData();
                        uploadFileBtn.setEnabled(true);
                        this.currentPath = data.getData();
                        filePathText.setText(this.currentPath != null ? data.getDataString() : "Arquivo não selecionado");
                    } else {
                        this.currentPath = null;
                        filePathText.setText("Arquivo não selecionado");
                        uploadFileBtn.setEnabled(false);
                    }
                });
    }

    public void sendFile(View view) {
        if (currentPath == null) return;
        Activity activity = this;
        new Thread(new Runnable(){
            @Override
            public void run() {
                byte[] buffer = null;
                int bytesRead = 0;
                try {
                    InputStream in = getContentResolver().openInputStream(currentPath);
                    buffer = new byte[in.available()];
                    bytesRead = in.read(buffer, 0, in.available());
                    in.close();
                } catch (IOException e) {
                    e.printStackTrace();
                    activity.runOnUiThread(() -> Toast.makeText(activity, "Falha ao abrir arquivo.", Toast.LENGTH_LONG).show());
                    return;
                }

                OkHttpClient client = new OkHttpClient.Builder()
                        .connectTimeout(5, TimeUnit.SECONDS)
                        .writeTimeout(120, TimeUnit.SECONDS)
                        .readTimeout(120, TimeUnit.SECONDS)
                        .build();

                RequestBody requestBody = new MultipartBody.Builder()
                        .setType(MultipartBody.FORM)
                        .addFormDataPart("file", "data.csv", RequestBody.create(MediaType.parse("text/csv"), buffer, 0, bytesRead))
                        .build();

                Request request = new Request.Builder()
                        .url("http://10.0.2.2:5000/ia/upload")
                        .post(requestBody)
                        .build();

                try (Response response = client.newCall(request).execute()) {
                    if (!response.isSuccessful()) throw new IOException("Unexpected code " + response);
                    if (response.body() == null) throw new IOException("Empty response " + response);

                    Intent membersIntent = new Intent(getApplicationContext(), ResponseActivity.class);
                    membersIntent.putExtra("response", response.body().string());
                    startActivity(membersIntent);
                } catch (IOException e) {
                    activity.runOnUiThread(() -> Toast.makeText(activity, "Falha ao fazer requisição.", Toast.LENGTH_LONG).show());
                    e.printStackTrace();
                }
            }
        }).start();
    }

    public void selectFile(View view) {
        Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
        intent.setType("*/*");
        someActivityResultLauncher.launch(intent);
    }

    public void openMembers(View view) {
        Intent membersIntent = new Intent(getApplicationContext(), MembersActivity.class);
        startActivity(membersIntent);
    }
}