import unittest
from io import StringIO
import sys
from test_base import captured_io, run_unittests
from unittest.mock import patch
import robot


class MyTests(unittest.TestCase):
    def test_get_robot_name(self):
        with captured_io(StringIO("Jules\n")):
            self.assertEqual(robot.get_robot_name(), 'Jules')


    def test_do_help(self):
        with captured_io(StringIO("help")):
            self.assertEqual(robot.do_help(), (True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays movement commands
REPLAY SILENT - replays movement commands silently and returns location
REPLAY REVERSE - replays movement commands in reverse
REPLAY REVERSE SILENT - replays movement commands in reverse silently and returns location
"""))


    def test_get_command(self):
        with captured_io(StringIO("forward 10")):
            self.assertEqual(robot.get_command("Jules"), "forward 10")


    def test_split_command_input(self): 
        with captured_io(StringIO("forward 10")):
            self.assertEqual(robot.get_command("forward 10"), "forward 10")

    
    def test_valid_command_replay(self):
        with captured_io(StringIO("replay")):
            self.assertEqual(robot.valid_command("replay"), True)
    

    def test_valid_command_replay_silent(self):
        with captured_io(StringIO("replay silent")):
            self.assertEqual(robot.valid_command("replay silent"), True)


    def test_valid_command_replay_reversed(self):
        with captured_io(StringIO("replay reversed")):
            self.assertEqual(robot.valid_command("replay reversed"), True)


    def test_valid_command_replay_reversed_silent(self):
        with captured_io(StringIO("replay reversed silent")):
            self.assertEqual(robot.valid_command("replay reversed silent"), True)

    
    def test_is_position_allowed_no(self):
        self.assertEqual(robot.is_position_allowed(700, 700), False)


    def test_is_position_allowed_yes(self):
        self.assertEqual(robot.is_position_allowed(70, 70), True)

    
    def test_update_position_allowed_no(self):
        self.assertEqual(robot.update_position(1000), False)


    def test_update_position_allowed_yes(self):
        self.assertEqual(robot.update_position(10), True)


    def test_do_forward_in_range(self):
        self.assertEqual(robot.do_forward("Jules", 5), (True, ' > Jules moved forward by 5 steps.'))
    

    def test_do_forward_not_in_range(self):
        self.assertEqual(robot.do_forward("Jules", 500), (True, 'Jules: Sorry, I cannot go outside my safe zone.'))

    
    def test_do_back_in_range(self):
        self.assertEqual(robot.do_back("Jules", 5), (True, ' > Jules moved back by 5 steps.'))
    

    def test_do_back_not_in_range(self):
        self.assertEqual(robot.do_back("Jules", 500), (True, 'Jules: Sorry, I cannot go outside my safe zone.'))  

    
    def test_get_history_one_element(self):
        self.assertEqual(robot.get_history([], 'forward 3'), ['forward 3'])

    
    def test_get_history_multiple_elements(self):
        self.assertEqual(robot.get_history(['forward 5'], 'forward 3'), ['forward 5','forward 3'])


    
if __name__ == '__main__':
    unittest.main()

