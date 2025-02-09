from flask import Flask, request, jsonify
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time

app = Flask(__name__)

# Connect to CoppeliaSim
client = RemoteAPIClient()
sim = client.getObject('sim')

# Get robot motor handles
left_motor = sim.getObject('/leftMotor')
right_motor = sim.getObject('/rightMotor')

# Function to move the robot
def move_robot(left_speed, right_speed, duration):
    sim.setJointTargetVelocity(left_motor, left_speed)
    sim.setJointTargetVelocity(right_motor, right_speed)
    time.sleep(duration)
    sim.setJointTargetVelocity(left_motor, 0)
    sim.setJointTargetVelocity(right_motor, 0) 

@app.route("/")
def home():
    return jsonify({"status": "Flask API is running!"})

# API Endpoint to move the robot
@app.route('/api/move', methods=['POST'])
def move():
    data = request.json
    direction = data.get('direction')
    if direction == 'forward':
        move_robot(2, 2, 2)
    elif direction == 'backward':
        move_robot(-2, -2, 2)
    elif direction == 'left':
        move_robot(2, -2, 1)
    elif direction == 'right':
        move_robot(-2, 2, 1)
    else:
        return jsonify({'error': 'Invalid direction'}), 400
    return jsonify({'status': 'Success', 'direction': direction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

