scp -i /home/ubuntu/.ssh/keymtc \
-o StrictHostKeyChecking=no \
-o UserKnownHostsFile=/dev/null \
-q ec2-user@${nodeip}:/etc/rancher/k3s/k3s.yaml ${k3s_path}/k3s-${nodename}.yaml && 
sed -i 's/127.0.0.1/${nodeip}/' ${k3s_path}/k3s-${nodename}.yaml