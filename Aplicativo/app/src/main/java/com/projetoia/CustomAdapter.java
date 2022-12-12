package com.projetoia;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import java.util.ArrayList;

public class CustomAdapter extends ArrayAdapter<ResponseItem> {

    private ArrayList<ResponseItem> dataSet;
    Context mContext;

    // View lookup cache
    private static class ViewHolder {
        TextView txtId;
        TextView txtPredict;
        TextView txtTrueResult;
    }

    public CustomAdapter(ArrayList<ResponseItem> data, Context context) {
        super(context, R.layout.row_item, data);
        this.dataSet = data;
        this.mContext = context;

    }

    private int lastPosition = -1;

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        ResponseItem dataModel = getItem(position);
        ViewHolder viewHolder;

        final View result;

        if (convertView == null) {

            viewHolder = new ViewHolder();
            LayoutInflater inflater = LayoutInflater.from(getContext());
            convertView = inflater.inflate(R.layout.row_item, parent, false);
            viewHolder.txtId = (TextView) convertView.findViewById(R.id.txtid);
            viewHolder.txtPredict = (TextView) convertView.findViewById(R.id.txtpredict);
            viewHolder.txtTrueResult = (TextView) convertView.findViewById(R.id.txttrueresult);

            result = convertView;

            convertView.setTag(viewHolder);
        } else {
            viewHolder = (ViewHolder) convertView.getTag();
            result = convertView;
        }

        lastPosition = position;

        viewHolder.txtId.setText(dataModel.getId());
        viewHolder.txtPredict.setText(dataModel.getPredict());
        viewHolder.txtTrueResult.setText(dataModel.getTrueResult());
        return convertView;
    }
}
