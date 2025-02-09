from fastapi import FastAPI 
from pydantic import BaseModel
from urllib.parse import urlparse   
from coppeliasim_zmqremoteapi_client import RemoteAPIClient



#connect the robot to coppeliasim 
client = RemoteAPIClient() 
sim = client.require('sim') #provides access to external python functions

#Get handle for robot (change 'Quadracopter' to your robot's actual name) 
robot_handle = sim.getObject('/Quadracopter') 
app = FastAPI()  

class MoveRequest(BaseModel):
    x: float
    y: float
    z: float 


class URLRequest(BaseModel):
    url: str

@app.post('/process_url')
async def process_url(): 
    parsed_url = urlparse(request.url)
    return {
        "scheme": parsed_url.scheme,
        "netloc": parsed_url.netloc,
        "path": parsed_url.path,
        "query": parsed_url.query
    } 

@app.post("/move")
async def move_robot(move: MoveRequest):
    """Move the robot to the given X, Y, Z coordinates."""
    sim.setObjectPosition(robot_handle, -1, [move.x, move.y, move.z])
    
    return {
        "message": "Robot moved successfully",
        "new_position": {"x": move.x, "y": move.y, "z": move.z}
    }