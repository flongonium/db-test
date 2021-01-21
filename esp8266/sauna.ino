// Do not remove the include below
#include "sauna.h"

const char *ssid 	= "YOUR SSID";
const char *password	= "YOUR PASSWORD";
const char *host	= "YOUR HOST";

SI7021 sensor;
const int sda_hw = 02;
const int scl_hw = 01;
int temp;
unsigned int hum;

int sensorId;
String sensorLocation = "Sauna";
//The setup function is called once at startup of the sketch
void setup()
{
// Add your initialization code here
	Serial.begin(9600);
	delay(10);
	WiFi.begin(ssid, password);
	Serial.print("connecting to: ");
	Serial.print(ssid);
	Serial.println("...");
	int i = 0;
	while (WiFi.status() != WL_CONNECTED)
	{
		delay(500);
		Serial.print(++i);
		Serial.print(" ");
	}
	Serial.println('\n');
	Serial.println("connection established to IP: ");
	Serial.println(WiFi.localIP());

	delay(50);
	//sensor.begin(sda_hw, scl_hw);
	Serial.println(sensor.getDeviceId());

}

// The loop function is called in an endless loop
void loop()
{
	sensorId = sensor.getDeviceId();
	temp = sensor.getCelsiusHundredths();
	hum = sensor.getHumidityPercent();

	delay(50);
	HTTPClient http;

	http.begin(host);
	http.addHeader("Content-Type", "application/x-www-form-urlencoded");

	String httpRequestData = "api_key=temphum1818&sensor_name=" + String(sensorId) + "&temperature=" + String(temp) + "&humidity=" + String(hum);

	int httpResponseCode = http.POST(httpRequestData);

	Serial.print("ResponseCode: ");
	Serial.println(httpResponseCode);
	Serial.println(temp);
	Serial.println(hum);

	http.end();
	delay(3000);

}
