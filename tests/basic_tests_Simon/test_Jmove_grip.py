# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
import torch

from polymetis import RobotInterface
from polymetis import Gripperinterface



if __name__ == "__main__":
    # Initialize robot interface
    robot = RobotInterface(
        ip_address="10.10.10.210",
        port = 50051
    )
    #gripper = Gripperinterface (
        #ip_address = "10.10.10.210",
        #port = 50051
    #)
    # Reset
    #robot.go_home()

    # Get joint positions
    joint_positions = robot.get_joint_positions()
    print(f"Current joint positions: {joint_positions}")

    robot.set_home_pose(joint_positions)
    # Command robot to pose (move 4th and 6th joint)
    joint_positions_desired = torch.Tensor(
        [-0.14, -0.02, -0.05, -1.57, 0.05, 1.50, -0.91]
    )
    print(f"\nMoving joints to: {joint_positions_desired} ...\n")
    state_log = robot.move_to_joint_positions(joint_positions_desired, time_to_go=2.0)

    # Get updated joint positions
    joint_positions = robot.get_joint_positions()
    print(f"New joint positions: {joint_positions}")


    robot.go_home()
    #test gripper

    #gripper_state = gripper.get_state()
    #gripper.goto(width=0.01, speed=0.05)
    #gripper.grasp(speed=0.05, force=0.1)
