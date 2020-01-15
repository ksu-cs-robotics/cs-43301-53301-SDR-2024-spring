#include "general.h"
#include "motor_driver.h"

Turtlebot3MotorDriver motor_driver;


void setup() 
{   
  // Initalize dynamixel driver and odom
  motor_driver.init(NAME);
}

void loop() 
{
  // serial communication
  recieved_py();

  // motor control 
  motor_driver.controlMotor(WHEEL_RADIUS, WHEEL_SEPARATION, goal_velocity);
}


/////////////////////////////////////////
//              Robot                  //
/////////////////////////////////////////



/////////////////////////////////////////
//            Data Parsing             //
/////////////////////////////////////////

void recieved_py(){
  if (Serial.available() > 0){
    char tmpChar = Serial.read();
    if ((msgBufferPointer == 0) && (tmpChar == '<')){
      msgBuffer[msgBufferPointer] = tmpChar; 
      msgBufferPointer++;
    }
    else if (msgBufferPointer == 1){
      if (tmpChar == '!'){ 
        msgBuffer[msgBufferPointer] = tmpChar; 
        msgBufferPointer++; 
      }
      else{
        if (tmpChar == '<'){
          msgBuffer[0] = tmpChar;
          msgBufferPointer = 1;
        }else{
          msgBufferPointer = 0;          
        }
      }
    }

    else if (msgBufferPointer >= 2){
      if (tmpChar == '<'){ 
        msgBuffer[0] = tmpChar;
        msgBufferPointer = 1;
      }
      else if (tmpChar == '>'){
        msgBuffer[msgBufferPointer] = tmpChar;
        msgBufferPointer = 0;
        evaluateCommand();
      }
      else{
        msgBuffer[msgBufferPointer] = tmpChar;
        msgBufferPointer++;
      }
    }
  }
}

void evaluateCommand(){
  char* command = strtok(msgBuffer, ",");
  int temp = 0;
  String type = "none";
  while (command != 0){
    if (temp == 1){
      if (String(command) == TORQUE_MSG){
        type = TORQUE_MSG;
      }
      else if (String(command) == CMD_MSG){
        type = CMD_MSG;
      }
    }

    if (type == TORQUE_MSG){
      if (temp == 3){
        if (String(command) == "true"){
          motor_driver.setTorque(true);
        }
        else if (String(command) == "false"){
          motor_driver.setTorque(false);
        }
      }
    }

    else if (type == CMD_MSG){
      if (temp == 3){
        goal_velocity[0] = String(command).toFloat();
      }
      else if (temp == 4){
        goal_velocity[1] = String(command).toFloat();
      }
    }
    
    temp += 1;
    command = strtok(0, ",");
  }
}

void send_py(String data[], int size, String type){
  String data_out;
  data_out = "<!," + type + "," + String(size) + ",";
  for(int i = 0; i < size; i++){
    data_out += data[i];
    data_out += ",";
  }
  data_out += "#>";

  Serial.print(data_out);
  Serial.print("\n");
}
