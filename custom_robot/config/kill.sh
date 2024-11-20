#!/bin/bash

# Display memory usage before clearing caches
echo "Memory usage before clearing caches:"
free -h

# Clear system caches
sudo sysctl -w vm.drop_caches=3
sudo sync
echo 3 | sudo tee /proc/sys/vm/drop_caches

# Display memory usage after clearing caches
echo "Memory usage after clearing caches:"
free -h

# Kill Gazebo Classic processes
echo "Terminating Gazebo Classic processes..."
pkill -f -9 'gzserver'
pkill -f -9 'gzclient'

echo "Cleanup complete!"
