#include <IRremote.h>

const int RECV_PIN = 10;
IRrecv irrecv(RECV_PIN);
decode_results results;

void setup()
{
  Serial.begin(9600);
  Serial.write("Listening");
  irrecv.enableIRIn();
  irrecv.blink13(true);
}

void loop()
{
  if (irrecv.decode(&results))
  {
    Serial.println(results.value, HEX);
    irrecv.resume();

    // Sleep 1s to guard against button hold
    delay(1000);
  }
}
