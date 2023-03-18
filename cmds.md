### Node Setup

---------------------------

Install Node

```bash
    sudo yum install -y gcc-c++ make
    curl -sL https://rpm.nodesource.com/setup_16.x | sudo -E bash -
    sudo yum install -y nodejs
```

Install Git

```bash
    sudo yum install -y git
```

Check node version

```bash
    node -v
```

Clone Project from github

```bash
    git clone https://github.com/compudemy/aws-auto-scaling-project.git
```

Run Application

```bash
    node app.js
```

Install dependencies

```bash
    npm install
```

### Run Stress on PC

```
sudo amazon-linux-extras install epel -y

sudo yum install stress -y

sudo stress --cpu 8 --vm-bytes $(awk '/MemAvailable/{printf "%d\n", $2 * 0.9;}' < /proc/meminfo)k --vm-keep -m 1

```