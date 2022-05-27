/* Code for face tracking application
using pan/tilt mechanism.
By Ruthvik @nagasairuthvik1919@gmail.com
*/

#include<Servo.h>

Servo servopan;         // Horizontal servo, 0-180
Servo servotilt;        // Vertical servo, 45-150

int servop1=6;          // Declaring servo pins and variables
int servop2=5;
int x=0,y=0;
int prevx=0,prevy=0;

/* Hardware declaration of each servo and making both servos at 90 deg.*/

void setup() {
  
  Serial.begin(9600);
  servopan.attach(servop1);
  servotilt.attach(servop2);
  servopan.write(90);
  servotilt.write(90);
  delay(1000);
}

/* Keeps searching for data in serial buffer 
 * and if the data starts with X then the integer value after it 
 * is assigned to x and if the next character is Y then repeats the same.
 * Calls the Function track() and stores the values of x,y for further use.
 * After this empty out the serial buffer.
*/

void loop() {
  
  if(Serial.available() > 0){
    if(Serial.read() == 'X'){
      /* For debugging
        digitalWrite(13, HIGH);
        delay(500);
        digitalWrite(13, LOW);
        delay(500);*/
      x = Serial.parseInt();
      if(Serial.read() == 'Y'){
        y = Serial.parseInt();
        track();
        prevx = x;
        prevy = y;
      }
    }
    while(Serial.available() > 0){
      Serial.read();
    }
  }
}

/* Function to control servos
 *  If the position of face is not same as before then 
 *  the recieved coordinates are mapped to the respective servos range of turning.
 *  As the tilt mechanism is not required much it is assigned the recieved coordinate.
 *  However pan servo coordinates keeps changing, so the control mechanism takes 
 *  into account the previous position as well.
 *  Based on the error between the current and previous position the servo 
 *  is made to move in the respective direction with delay for smoothness. 
 *  A tolerance of 10 degrees is given for the coordinates.
*/

void track(){
  if(prevx != x || prevy != y){
    int val1 = map(x, 600, 0, 70, 179);
    int val2 = map(y, 450, 0, 150, 45);
    int pval1 = map(prevx, 600, 0, 70, 179);
  
    servotilt.write(val2);
    
    if(val1 > pval1){           
     while((val1-pval1) >= 10){
       servopan.write(pval1); 
       pval1++;
       delay(10);
     }
    }
    else if(val1 < pval1){       
     while((pval1 - val1) >= 10){
       servopan.write(pval1);    
       pval1--;
       delay(10);
     }
    }       
  }
}
