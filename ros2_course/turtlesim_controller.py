import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class TurtlesimController(Node):

    def __init__(self):
        super().__init__("turtlesim_controller")
        self.twist_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.pose = None

        # Subscribe to turtle position updates
        self.subscription = self.create_subscription(
            Pose, "/turtle1/pose", self.cb_pose, 10
        )

    def cb_pose(self, msg):
        """Callback function for the Pose subscriber"""
        self.pose = msg  # Update the turtle's position

    def go_to(self, speed, omega, x, y):
        """Move turtle to (x, y) coordinate with speed and angular velocity"""

        # Wait until the first pose message is received
        loop_rate = self.create_rate(10, self.get_clock())  # 10 Hz
        while self.pose is None and rclpy.ok():
            self.get_logger().info("Waiting for pose...")
            rclpy.spin_once(self)

        self.get_logger().info(f"Moving to ({x}, {y})")

        # Create velocity message
        vel_msg = Twist()

        while rclpy.ok():
            # Calculate distance to target
            dx = x - self.pose.x
            dy = y - self.pose.y
            distance = math.sqrt(dx**2 + dy**2)

            # Calculate desired heading angle
            target_theta = math.atan2(dy, dx)

            # Calculate angular error
            angle_error = target_theta - self.pose.theta

            # Normalize angle to range [-pi, pi]
            angle_error = (angle_error + math.pi) % (2 * math.pi) - math.pi

            if distance < 0.001 and angle_error < 0.001:  # Stop when close enough
                break

            # Set linear and angular velocities
            vel_msg.linear.x = min(speed, speed * distance)  # Reduce speed if close
            vel_msg.angular.z = omega * angle_error  # Proportional control

            self.twist_pub.publish(vel_msg)
            rclpy.spin_once(self)

        # Stop the turtle when destination is reached
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 0.0
        self.twist_pub.publish(vel_msg)
        self.get_logger().info("Arrived at destination.")


def main(args=None):
    rclpy.init(args=args)
    tc = TurtlesimController()

    # S betű
    tc.go_to(1.0, 2.0, 5, 6)
    tc.go_to(1.0, 2.0, 5, 5)
    tc.go_to(1.0, 2.0, 6, 4)
    tc.go_to(1.0, 2.0, 5, 3.5)
    tc.go_to(1.0, 2.0, 5, 4)

    tc.go_to(1.0, 2.0, 6, 4.5)

    # Z betű felso egyenes
    tc.go_to(1.0, 2.0, 7, 4.5)
    tc.go_to(1.0, 2.0, 7.5, 4.5)

    # Z elso kanyar
    tc.go_to(1.0, 3.0, 7.3, 4.3)
    # Z ferde lefele
    tc.go_to(1.0, 2.0, 7, 4)
    tc.go_to(1.0, 2.0, 6.5, 3.5)
    # Z also egyenes
    tc.go_to(1.0, 2.0, 6.6, 3.5)
    tc.go_to(1.0, 2.0, 6.8, 3.5)
    tc.go_to(1.0, 3.0, 7, 3.5)
    tc.go_to(1.0, 2.0, 8.5, 3.5)

    tc.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
