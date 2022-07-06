## How to install Docker 


yum update

reboot 

## copy the yum docker rep from my personal git hut to /etc/yum.repos.d 

## will look like  the following ls -l 

## -rw-r--r--. 1 root root  2095 Jul  6 05:41 docker-ce.repo

yum -y install slirp4netns fuse-overlayfs container-selinux

yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin


systemctl start docker


 systemctl enable docker


usermod -aG docker oracle




