package org.ohravaara.raspicar;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

public class MainActivity extends AppCompatActivity {
    private final int BUTTON_UP_TAG = 1;
    private final int BUTTON_DOWN_TAG = 2;
    private final int BUTTON_LEFT_TAG = 3;
    private final int BUTTON_RIGHT_TAG = 4;

    private Context context;
    private ImageView imageView;

    private final String http = "http://";
    private String serverUrl;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button buttonUp = (Button)findViewById(R.id.buttonUp);
        Button buttonDown = (Button)findViewById(R.id.buttonDown);
        Button buttonLeft = (Button)findViewById(R.id.buttonLeft);
        Button buttonRight = (Button)findViewById(R.id.buttonRight);

        buttonUp.setTag(BUTTON_UP_TAG);
        buttonDown.setTag(BUTTON_DOWN_TAG);
        buttonLeft.setTag(BUTTON_LEFT_TAG);
        buttonRight.setTag(BUTTON_RIGHT_TAG);

        Button.OnTouchListener onTouchListener = OnTouchListener();
        buttonUp.setOnTouchListener(onTouchListener);
        buttonDown.setOnTouchListener(onTouchListener);
        buttonLeft.setOnTouchListener(onTouchListener);
        buttonRight.setOnTouchListener(onTouchListener);

        context = this;
        imageView = (ImageView)findViewById(R.id.backgroundImage);

        serverUrl = http + PreferenceManager.getDefaultSharedPreferences(this).getString("serverIp","192.168.42.1");
    }

    @Override
    protected void onResume() {
        serverUrl = http + PreferenceManager.getDefaultSharedPreferences(this).getString("serverIp","192.168.42.1");
        super.onResume();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        if (item.getItemId() == R.id.menu_settings) {
            Intent intent = new Intent(this, SettingsActivity.class);
            startActivity(intent);
        }
        return super.onOptionsItemSelected(item);
    }

    private void send(String urlEnd) {
        RequestQueue queue = Volley.newRequestQueue(this);

        String url = serverUrl + urlEnd;

        StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                (response) ->
                    Toast.makeText(context, "Success!", Toast.LENGTH_SHORT).show()
                ,
                (error) ->
                    Toast.makeText(context, "Fuckup!", Toast.LENGTH_SHORT).show());


        stringRequest.setRetryPolicy(
                new DefaultRetryPolicy(
                        DefaultRetryPolicy.DEFAULT_TIMEOUT_MS,
                        DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                        DefaultRetryPolicy.DEFAULT_BACKOFF_MULT
                )
        );

        queue.add(stringRequest);
    }

    private void moveForward() {
        send("/move.php?move=back");
        imageView.setImageResource(R.drawable.trump3);
    }

    private void moveBack() {
        send("/move.php?move=true");
        imageView.setImageResource(R.drawable.trump3);
    }

    private void stop() {
        send("/move.php?move=false");
        imageView.setImageResource(R.drawable.trump2);
    }

    private void turn(int direction) {
        String url =  "/turn.php";

        switch (direction) {
            case BUTTON_LEFT_TAG:
                url = url + "?kulma=0.0004";
                break;

            case BUTTON_RIGHT_TAG:
                url = url + "?kulma=0.0025";
                break;

            default:case 0:
                break;
        }

        send(url);
    }

    private Button.OnTouchListener OnTouchListener() {
        return new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {

                boolean press = true, upOrDown;
                switch (event.getAction()) {
                    case MotionEvent.ACTION_DOWN:
                        upOrDown = true;
                        press = true;
                        break;
                    case MotionEvent.ACTION_UP:
                        upOrDown = true;
                        press = false;
                        break;
                    default:
                        upOrDown = false;
                        break;
                }

                if (upOrDown) {

                    int tag = (int)v.getTag();
                    switch (tag) {
                        case BUTTON_UP_TAG:
                            if (press) {
                                moveForward();
                            } else {
                                stop();
                            }
                            break;

                        case BUTTON_DOWN_TAG:
                            if (press) {
                                moveBack();
                            } else {
                                stop();
                            }
                            break;

                        case BUTTON_LEFT_TAG:
                            if (press) {
                                turn(BUTTON_LEFT_TAG);
                            } else {
                                turn(0);
                            }
                            break;

                        case BUTTON_RIGHT_TAG:
                            if (press) {
                                turn(BUTTON_RIGHT_TAG);
                            } else {
                                turn(0);
                            }
                            break;

                        default:
                            // Plaah poop
                            break;
                    }
                }
                return false;
            }
        };
    }
}
