// PA004 Health Insurance Cross Sell
function onOpen() {
  var u1 = SpreadsheetApp.getUi();
  u1.createMenu('Propensity Score')
    .addItem('Get Prediction','PredictAll')
    .addToUi();
}

host_production = 'insurance-gds.herokuapp.com'

// Helper Function
function ApiCall( data, endpoint ){
  var url = 'https://' + host_production + endpoint;
  var payload = JSON.stringify( data );
  var options = {'method': 'POST', 'contentType': 'application/json', 'payload': payload};
  var response = UrlFetchApp.fetch( url, options );

  // get response
  var rc = response.getResponseCode();
  var respondeText = response.getContentText();

  // error
  if ( rc !== 200 ){
    Logger.log('Response (%s) %s', rc, respondeText );
  }
  else{
    prediction = JSON.parse(respondeText);
  }

  return prediction

}

// Health Insurance propensity score prediction
function PredictAll(){
  // google sheets parameters
  var ss = SpreadsheetApp.getActiveSheet();
  var titleColumns = ss.getRange('A1:M1').getValues()[0];
  var lastRow = ss.getLastRow();

  var data = ss.getRange( 'A2' + ':' + 'M' + lastRow ).getValues();

  // run over all rows
  for ( row in data ){
    var json = new Object();

    // run over all columns
    for( var j=0; j < titleColumns.length; j++ ){
      json[titleColumns[j]] = data[row][j];
    };

    // list of json to send
    var jsonSend = new Object();
    jsonSend['id'] = json['id'];
    jsonSend['gender'] = json['gender'];
    jsonSend['age'] = json['age'];
    jsonSend['driving_license'] = json['driving_license'];
    jsonSend['region_code'] = json['region_code'];
    jsonSend['previously_insured'] = json['previously_insured'];
    jsonSend['vehicle_age'] = json['vehicle_age'];
    jsonSend['vehicle_damage'] = json['vehicle_damage'];
    jsonSend['annual_premium'] = json['annual_premium'];
    jsonSend['policy_sales_channel'] = json['policy_sales_channel'];
    jsonSend['vintage'] = json['vintage'];

    pred = ApiCall(jsonSend, '/predict');

    // send back to google sheets
    ss.getRange( Number(row)+2,14).setValue(pred[0]['score'])

  };
}
