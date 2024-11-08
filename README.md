# fall2024-cs460-indoor-env
Webots simulated environment of Saban Catholic Student Center for class assignment

To build and run world-

1. Clone repository to a folder on your device
2. Open terminal
3. Navigate to the repository clone destination folder
4. Enter the following commands-
    'cd fall2024-cs460-envs/fall2024-cs460-indoor-env/'
    'colcon build'
    'source install/setup.bash'
    'ros2 launch myenv webots_launch.py'

To adjust doors-
Select a door to open/close
note- doors are colored for ease of distinction

1. Left bathroom door (RED)
    position 0 (closed) through -1.4 (open)
2. Right bathroom door (BLUE)
    position 0.45 (closed) through 1.4 (open)
3. Left study room door (ORANGE)
    position 0 (closed) through -1.5 (open)
4. Right study room door (GREEN)
    position 0 (closed) through 1.5 (open)
    
