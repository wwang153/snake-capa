# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from capa_interfaces.msg import Num


class CapaSubscriber(Node):

    def __init__(self):
        super().__init__('capa_subscriber')
        self.subscription = self.create_subscription(
            Num,
            'capa_sensor',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        a=1
        # self.get_logger().info('I heard: "%f"' % msg.capa0)


def main(args=None):
    rclpy.init(args=args)

    capa_subscriber = CapaSubscriber()

    rclpy.spin(capa_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    capa_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
