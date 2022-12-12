package com.projetoia;

public class ResponseItem {

    String id;
    String predict;
    String trueResult;

    public ResponseItem(String id, String predict, String trueResult) {
        this.id = id;
        this.predict = predict;
        this.trueResult = trueResult;
    }

    public String getId() { return id; }
    public String getPredict() { return predict; }
    public String getTrueResult() { return trueResult; }

}
