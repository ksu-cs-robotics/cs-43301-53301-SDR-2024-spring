#ifndef _GENERAL_H_
#define _GENERAL_H_

#define NAME                             "Burger"
#define WHEEL_NUM                        2
#define WHEEL_RADIUS                     0.033           // meter
#define WHEEL_SEPARATION                 0.160           // meter (BURGER : 0.160, WAFFLE : 0.287)
#define TICK2RAD                         0.001533981  // 0.087890625[deg] * 3.14159265359 / 180 = 0.001533981f

#define ODOM_MSG                         "o"
#define CMD_MSG                          "c"
#define TORQUE_MSG                       "t"
#define GENERAL_MSG                      "g"

#define MESSAGE_BUFFER_SIZE              64

//init robot info
bool init_encoder = true;
float zero_velocity[WHEEL_NUM] = {0.0, 0.0};
float goal_velocity[WHEEL_NUM] = {0.0, 0.0};
int32_t last_diff_tick[WHEEL_NUM] = {0, 0};

// init odom 
float odom_pose[3];
double odom_vel[3];
double  last_rad[WHEEL_NUM]       = {0.0, 0.0};

// init general
unsigned long prev_update_time;
static float orientation[4];
int led_pin = 14;
bool shoot = false;
int shootting_blink = 0;

// init joint state
double  last_velocity[WHEEL_NUM]  = {0.0, 0.0};
int32_t left_encoder;
int32_t right_encoder;

// general value
struct Odom{
  float pos_x;
  float pos_y;
  float pos_z;
  float ori_w;
  float ori_x;
  float ori_y;
  float ori_z;
  float lin_x;
  float ang_z;
};

Odom odom_less = {0,0,0,0,0,0,0,0,0}; 

char msgBuffer[MESSAGE_BUFFER_SIZE]; 
int msgBufferPointer = 0;

bool torque;
#endif
