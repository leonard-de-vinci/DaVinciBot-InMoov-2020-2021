# CMake generated Testfile for 
# Source directory: /home/flavien/inmoov_python3_ws/src/vision_opencv/image_geometry/test
# Build directory: /home/flavien/inmoov_python3_ws/build/vision_opencv/image_geometry/test
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_image_geometry_nosetests_directed.py "/home/flavien/inmoov_python3_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python3" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/flavien/inmoov_python3_ws/build/test_results/image_geometry/nosetests-directed.py.xml" "--return-code" "\"/usr/bin/cmake\" -E make_directory /home/flavien/inmoov_python3_ws/build/test_results/image_geometry" "/usr/bin/nosetests -P --process-timeout=60 /home/flavien/inmoov_python3_ws/src/vision_opencv/image_geometry/test/directed.py --with-xunit --xunit-file=/home/flavien/inmoov_python3_ws/build/test_results/image_geometry/nosetests-directed.py.xml")
add_test(_ctest_image_geometry_gtest_image_geometry-utest "/home/flavien/inmoov_python3_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python3" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/flavien/inmoov_python3_ws/build/test_results/image_geometry/gtest-image_geometry-utest.xml" "--return-code" "/home/flavien/inmoov_python3_ws/devel/lib/image_geometry/image_geometry-utest --gtest_output=xml:/home/flavien/inmoov_python3_ws/build/test_results/image_geometry/gtest-image_geometry-utest.xml")
