package org.ohravaara.raspicar;

import android.os.Bundle;
import android.preference.PreferenceActivity;

/**
 * Created by juuso on 5.2.2016.
 */
public class SettingsActivity extends PreferenceActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        addPreferencesFromResource(R.xml.settings);
    }
}
