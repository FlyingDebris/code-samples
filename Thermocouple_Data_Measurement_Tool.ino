//This code lets you display the temperature reading coming in from a MAX31856 breakout board with a K-type thermocouple attached.
//If you want to save your data, make sure to open PuTTY, change the baud to 115200, and have it listen to whichever port you're connected to.

#include <Adafruit_MAX31856.h>

//Change these to determine which pins are being used
Adafruit_MAX31856 maxthermo = Adafruit_MAX31856(10, 11, 12, 13);

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(1000);
  Serial.println("Thermocouple Interpreter Initiated");

  maxthermo.begin();

  //The line below allows you to manually set thermocouple type, if needed. Need to comment out getThermocoupleType to keep that setting though.
  //maxthermo.setThermocoupleType(MAX31856_TCTYPE_K);

  Serial.print("Thermocouple type: ");
  switch (maxthermo.getThermocoupleType() ) 
  {
    case MAX31856_TCTYPE_K: Serial.println("K-Type"); break;
    //You can add in other thermocouple types here if you really need to, but we generally only use K-type.
  }
}

void loop() {
  Serial.print("Cold Junction Temp: ");
  Serial.println(maxthermo.readCJTemperature());
//CJ temp should always be around 22C, if it isn't, then you may need to reevaluate testing procedures as the temperature results will likely be inaccurate.

  Serial.print("Thermocouple Temp: ");
  Serial.println(maxthermo.readThermocoupleTemperature());
//Thermocouple temp measurements break down outside around -200C to 1000C. I will be surprised and concerned if you exceed either of those values.

//Fault detection for bad inputs. Generally, if you get voltage high/low faults, the connections to the board are bad.
  uint8_t fault = maxthermo.readFault();
  if (fault) {
    if (fault & MAX31856_FAULT_CJRANGE) Serial.println("Cold Junction Range Fault");
    if (fault & MAX31856_FAULT_TCRANGE) Serial.println("Thermocouple Range Fault");
    if (fault & MAX31856_FAULT_CJHIGH)  Serial.println("Cold Junction High Fault");
    if (fault & MAX31856_FAULT_CJLOW)   Serial.println("Cold Junction Low Fault");
    if (fault & MAX31856_FAULT_TCHIGH)  Serial.println("Thermocouple High Fault");
    if (fault & MAX31856_FAULT_TCLOW)   Serial.println("Thermocouple Low Fault");
    if (fault & MAX31856_FAULT_OVUV)    Serial.println("Over/Under Voltage Fault");
    if (fault & MAX31856_FAULT_OPEN)    Serial.println("Thermocouple Open Fault");
  }
//The delay below adjusts your refresh rate, in miliseconds. For most TEG testing, you won't need anything under 500.
  delay(500);
}
