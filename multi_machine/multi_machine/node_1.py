import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):

    def __init__(self):
        super().__init__('node_1')

        # Load params
        self.declare_parameter('robot_name', None)
        self.declare_parameter('my_param', None)
        self.robot_name = self.get_parameter('robot_name').value
        self.my_param = self.get_parameter('my_param').value
        self.add_on_set_parameters_callback(self.parameters_callback)

        # Use the node name to create the topic name
        self.node_name = self.get_name()

        # Create a publisher using the topic name
        self.publisher = self.create_publisher(String, f'{self.robot_name}/my_topic', 10)

        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self._timer_callback)

    def parameters_callback(self, params):
        # do some actions, validate parameters, update class attributes, etc.        
        return SetParametersResult(successful=True)

    def _timer_callback(self):
        # Publish a message on the topic
        message = String()
        message.data = self.node_name
        self.publisher.publish(message)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
