# Amarel Tutorial

One of the training and inference infrastructure options we will use in this class for larger workloads is Rutgers' own [Amarel](https://it.rutgers.edu/research-computing/amarel/) computing cluster, created and managed by the Office of Advanced Research Computing (OARC). As distinct from the *local development* options we have encountered so far, Amarel provides a shared *cluster* or group of networked computers that you can access to perform training runs using more GPUs than would be practical with your local setup. (Unless you have a *very* high end home set up!) While research groups can purchase their own dedicated Amarel resources, a general access category is provided free to Rutgers students and faculty.

You can learn more about Amarel in the [user guide](https://user-guide-f4258a.gitlab.io/). This tutorial loosely follows the user guide and other relevant resources to briefly introduce Amarel, walk through requesting an account, accessing the cluster, confirming you can configure a Python development environment that mirrors that which we have been using in class, and run Hello World training examples. As we move toward training larger networks with more parameters on larger datasets, which will demand more storage, memory, and compute (operations per second) than practical on our laptops, Amarel will be on of the options available to us to *scale* our systems.

## About

The Amarel [webpage](https://it.rutgers.edu/research-computing/amarel/#about-amarel) introduces Amarel as follows.

*Amarel is a shared, community‑owned advanced computing environment available to Rutgers researchers and students whose projects require computational resources. It combines a flexible design that supports a wide range of research needs with standardized tools and policies, making it easier to use, manage, and troubleshoot while delivering a smooth, consistent user experience.*

*Amarel operates under a ‘condo model,’ offering free, first‑come, first‑served access to all Rutgers researchers, including students, staff, and faculty. In this model, research groups can purchase their own compute nodes and storage, gaining priority access to those resources and the ability to preempt general‑access jobs when needed. The university provides the remaining infrastructure—data center facilities, power and cooling, networking, hardware support, and system administration—at no additional cost.*

An overview of the resources Amarel provides is given in the user manual [here](https://user-guide-f4258a.gitlab.io/systems/).

### Maintenance Schedule

Amarel follows a tentative maintenance schedule with maintenance outages spanning up to 2 days each month, starting on the 3rd Tuesday of the month. In some cases the maintenance period ends early, but in general each maintenance period is expected to begin at about 08:00 ET on the first day and end by about 23:59 ET on the 2nd day. You can get more information about Amarel current status and maintenance periods [here](https://it.rutgers.edu/research-computing/amarel-system-status/).

### Quick Resources

* **User Guide**: [https://user-guide-f4258a.gitlab.io/](https://user-guide-f4258a.gitlab.io/)
* **Website**: [https://it.rutgers.edu/research-computing/amarel/](https://it.rutgers.edu/research-computing/amarel/)
* **FAQ**: [https://it.rutgers.edu/research-computing/research-computing-faqs/#amarel-faq](https://it.rutgers.edu/research-computing/research-computing-faqs/#amarel-faq)
* **Amarel introductory video**: [https://www.youtube.com/watch?v=GECyL_5NcAk&t=1s](https://www.youtube.com/watch?v=GECyL_5NcAk&t=1s)
* **Account Request**: [https://it.rutgers.edu/research-computing/amarel-cluster-access-request/](https://it.rutgers.edu/research-computing/amarel-cluster-access-request/)
* **System Status**: [https://it.rutgers.edu/research-computing/amarel-system-status/](https://it.rutgers.edu/research-computing/amarel-system-status/)

## Setup

These steps need to be performed before accessing Amarel for the first time.

### Request an Account

Follow the directions [here](https://user-guide-f4258a.gitlab.io/accounts/) to request an account through this [form](https://user-guide-f4258a.gitlab.io/). Note it will usually tae approximately 72 hours for accounts to be provisioned, and may take longer. Be sure to request an account early to provide time for provisioning.

You will get an email when you account has been setup by the Amarel team. Your account name will look something like `<netID>@amarel.rutgers.com`.

Read the acceptable use policy [here](https://user-guide-f4258a.gitlab.io/accounts/policy/).

### Download the VPN

**IMPORTANT: You will need to be physically present on campus or connected to the Rutgers VPN to access Amarel.** To do this, you will need to follow the instructions [here](https://it.rutgers.edu/virtual-private-network/) to download the VPN software and install it. Do this before proceeding as you will need to access the VPN before logging in for the first time.

## First Login

Once your account has been provisioned (you should receive an email letting you know when your account is ready) you will need to connect to the VPN and log into Amarel for the first time to verify everything is working properly.

### Connect to a VPN

Launch the VPN software you installed previously and provide your credentials. You will likely need to enter a push code or other two-factor authentication mechanism. If you connect to other Rutgers resources remotely through VPN, do this step as you normally would.

### SSH into the Login Node

Open a terminal (either in VS Code or a standalone terminal) and follow the directions [here](https://user-guide-f4258a.gitlab.io/connect/) to use SSH (secure shell) to connect to Amarel. If you are new to SSH, SSH provides a means to remotely connect to other computers. When you use SSH to connect to another computer, you will start a shell that runs on that computer and has access to its files. You will need to exit this shell with `exit` to return to your local shell (or which ever shell you started your SSH session from).

SSH into the Amarel login node.

```bash
ssh <netID>@amarel.rutgers.edu
```

### Issue: Could Not Resolve Hostname

If you see an error like the following one this likely means that you are not on the Rutgers network.

```bash
$ ssh <netID>@amarel.rutgers.edu
ssh: Could not resolve hostname amarel.rutgers.edu: Name or service not known
```

If you are not physically on campus, this likely means you need to connect to the Rutgers VPN. If you are physically on campus, this might mean you are connected another network besides the Rutgers network, such as a personal hot spot.

### Issue: Remote Host Identification Changed

You may see a message like the following when connecting again after not connecting for some time.

```bash
ssh <netID>@amarel.rutgers.edu
```

```text
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256:12341234123412341234123412341234123412341234
Please contact your system administrator.
Add correct host key in /c/Users/sanch/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /c/Users/sanch/.ssh/known_hosts:5
Host key for amarel.rutgers.edu has changed and you have requested strict checking.
Host key verification failed.
```

If you see this message, it likely means you need to cycle your SSH keys.

Confirm the fingerprint with your instructor or another administrator. For good security practice, avoid bypassing this using `StrictHostChecking=no`.

If you have confirmed you are connecting to the right server with your instructor, use the following command to cycle keys.

```bash
ssh-keygen -R amarel.rutgers.edu
```

### Success

Successful login will either show a welcome message or simply land you on the login server.

**NOTE: the login server is NOT where you do work. The login server that you land on when you first login to Amarel is NOT the place where you should be running programs or attempting to perform larger computing jobs.**

The login server is a shared computing node that is less powerful than the machines that actually perform heavy computing jobs on Amarel. Many other people are likely on the server at the same time as you are. If you attempt to perform intensive work from this server (e.g., training a large model).

```
Last login: Wed Jul  8 11:11:14 2026 from 10.75.233.8
############################################################################
____ _  _ ____ ____ ____ _      ____ ___   ____ _  _ ___ ____ ____ ____ ____
|__| |\/| |__| |__/ |___ |      |__|  |    |__/ |  |  |  | __ |___ |__/ [__
|  | |  | |  | |  \ |___ |___   |  |  |    |  \ |__|  |  |__] |___ |  \ ___]

        Welcome to the AMAREL research computing cluster managed by
   the Office of Advanced Research Computing (OARC) at Rutgers University
                          http://oarc.rutgers.edu

Need help? Send an e-mail to help@oarc.rutgers.edu

User documentation: https://sites.google.com/view/cluster-user-guide

Do NOT run programs, tests, analyses, or pre/postprocessing on the shared
login nodes (amarel1, amarel2, etc.). That's what compute nodes are for.

############################################################################

[saul@amarel2 ~]$
```

## Confirm You are Logged in Correctly

Explore with

hostname
whoami
pwd
ls -al

hostname should show you are on a login node, e.g.,

amarel3.amarel.rutgers.edu

Note this will change later when you request GPUs through the scheduler.

These are shared by many users and are intended for light administrative work. Rutgers explicitly instructs users to run computational work through the scheduler.



## Understand Your Shell Environment

Read tutorial here
https://user-guide-f4258a.gitlab.io/environment/shell_startup/

## Learn How to View and Load Modules

https://user-guide-f4258a.gitlab.io/environment/lmod/

lmod

Documentation: https://lmod.readthedocs.io/en/latest/index.html
User Guide: https://lmod.readthedocs.io/en/latest/010_user.html

module


ml avail
ml spider

ml cuda
ml gcc

## Cluster Basics

### Login Nodes vs. Compute Nodes

### Shared Resource Management

### Partitions

### Cores and Hyperthreads

A CPU core is a physical processing unit inside a computer's central processing unit (CPU) that independently reads and executes program instructions.

Hyper-threading (officially called Hyper-Threading Technology or HTT) is an Intel technology that allows a single physical CPU core to act like two logical (virtual) cores by processing two instruction streams, or threads, at the same time.

## Slurm and Job Scheduling Basics

https://user-guide-f4258a.gitlab.io/jobs/

Amarel uses Slurm for cluster/resource management and job scheduling. Slurm is responsible for allocating resources to users, providing a framework for starting, executing and monitoring work on allocated resources and scheduling work for future execution.

### Slurm Basics

https://slurm.schedmd.com/quickstart.html

"Slurm is an open source, fault-tolerant, and highly scalable cluster management and job scheduling system for large and small Linux clusters. Slurm requires no kernel modifications for its operation and is relatively self-contained. As a cluster workload manager, Slurm has three key functions. First, it allocates exclusive and/or non-exclusive access to resources (compute nodes) to users for some duration of time so they can perform work. Second, it provides a framework for starting, executing, and monitoring work (normally a parallel job) on the set of allocated nodes. Finally, it arbitrates contention for resources by managing a queue of pending work."

As depicted in Figure 1, Slurm consists of a slurmd daemon running on each compute node and a central slurmctld daemon running on a management node (with optional fail-over twin). The slurmd daemons provide fault-tolerant hierarchical communications. The user commands include: sacct, sacctmgr, salloc, sattach, sbatch, sbcast, scancel, scontrol, scrontab, sdiag, sh5util, sinfo, sprio, squeue, sreport, srun, sshare, sstat, strigger and sview. All of the commands can run anywhere in the cluster.

![Alt text](images/arch.gif)

The entities managed by these Slurm daemons, shown in Figure 2, include nodes, the compute resource in Slurm, partitions, which group nodes into logical (possibly overlapping) sets, jobs, or allocations of resources assigned to a user for a specified amount of time, and job steps, which are sets of (possibly parallel) tasks within a job.

Priority-ordered jobs are allocated nodes within a partition until the resources (nodes, processors, memory, etc.) within that partition are exhausted. Once a job is assigned a set of nodes, the user is able to initiate parallel work in the form of job steps in any configuration within the allocation. For instance, a single job step may be started that utilizes all nodes allocated to the job, or several job steps may independently use a portion of the allocation.

### Helpful Commands

sinfo reports the state of partitions and nodes managed by Slurm. It has a wide variety of filtering, sorting, and formatting options.

srun is used to submit a job for execution or initiate job steps in real time. srun has a wide variety of options to specify resource requirements, including: minimum and maximum node count, processor count, specific nodes to use or not use, and specific node characteristics (so much memory, disk space, certain required features, etc.). A job can contain multiple job steps executing sequentially or in parallel on independent or shared resources within the job's node allocation.

sbatch
sbatch is used to submit a job script for later execution. The script will typically contain one or more srun commands to launch parallel tasks.

When you submit the job, Slurm responds with the job's ID, which will be used to identify this job in reports from Slurm.

```bash
$ sbatch job.sh
Submitted batch job 123456
```

123456 is the job ID.


See your jobs for job ID 123456
```bash
squeue -u $USER           # See your jobs
scontrol show job 123456  # Understand why a job is waiting
squeue --start -j 123456  # Estimate its start time
```

### Slurm Partitions

https://user-guide-f4258a.gitlab.io/jobs/partitions/

Whenever a job is run on a HPC system, it must be sent to one of the SLURM partition that defines a list of nodes and any additional settings such as Quality of Service (QoS) which sets resource limits.

Before requesting resources (compute nodes), it can be helpful to see what resources are available and what cluster partitions to use for certain resources.

Example of using the sinfo command:


### Best Practices

Consider putting related work into a single Slurm job with multiple job steps both for performance reasons and ease of management. Each Slurm job can contain a multitude of job steps and the overhead in Slurm for managing job steps is much lower than that of individual jobs.

Job arrays are an efficient mechanism of managing a collection of batch jobs with identical resource requirements. Most Slurm commands can manage job arrays either as individual elements (tasks) or as a single entity (e.g. delete an entire job array in a single command).

[job arrays](https://slurm.schedmd.com/job_array.html)


### Slurm Man Pages

https://slurm.schedmd.com/man_index.html


### Citing Slurm

We recommend citing the peer-reviewed paper from JSSPP 2023: Architecture of the Slurm Workload Manager.

Jette, M.A., Wickberg, T. (2023). Architecture of the Slurm Workload Manager.
In: Klusáček, D., Corbalán, J., Rodrigo, G.P. (eds) Job Scheduling Strategies
for Parallel Processing. JSSPP 2023. Lecture Notes in Computer Science,
vol 14283. Springer, Cham. https://doi.org/10.1007/978-3-031-43943-8_1

## Explore the Cluster

```bash
# sinfo = get information about available partitions
# -s = summarize
sinfo -s
```

```bash
sinfo --partition=gpu --format="%N %G %T"
```
- Filters and displays the GPU partition details, including nodes, available GPUs, and their current state.

```bash
# Show available GPU resources
sinfo -o "%P %G %D %t"
```

The -o flag specifies a custom output format, with each % code representing a particular field.
Field	Meaning	Description
%P	Partition	Name of the Slurm partition (queue). A * indicates the default partition.
%G	GRES	Generic resources configured on the nodes, typically GPUs.
%D	Nodes	Number of nodes represented by the row.
%t	State	Current node state, such as idle, allocated, or mixed.

PARTITION  GRES         NODES  STATE
gpu*       gpu:a100:4   2      idle
gpu        gpu:v100:4   3      mix
gpu        gpu:a100:4   5      alloc
cpu        (null)       10     idle

This tells us:
- 2 nodes have 4 A100 GPUs each and are idle.
- 3 nodes have 4 V100 GPUs each and are partially allocated.
- 5 nodes have 4 A100 GPUs each and are fully allocated.
- 10 nodes have no GPU resources configured.

```bash
# Show your jobs
squeue -u "$USER"
```

```bash
# Show your Slurm associations
sacctmgr show assoc user="$USER"
```

## Request a GPU Interactively

Request a GPU:

```bash
srun --partition=gpu \
     --gres=gpu:1 \
     --cpus-per-task=2 \
     --mem=8G \
     --time=00:10:00 \
     --pty bash
```

Note you are now on a different host

```bash
hostname
```

This should confirm you are on a GPU node, e.g., gpu017.amarel.rutgers.edu

Run `nvidia-smi` to confirm available GPUs.

```text
Tue Oct 13 07:05:23 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.148.08             Driver Version: 570.148.08     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 3090        On  |   00000000:18:00.0 Off |                  N/A |
| 37%   26C    P8             19W /  350W |       1MiB /  24576MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA GeForce RTX 3090        On  |   00000000:3B:00.0 Off |                  N/A |
| 31%   26C    P8             20W /  350W |       1MiB /  24576MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA GeForce RTX 3090        On  |   00000000:86:00.0 Off |                  N/A |
| 31%   26C    P8             30W /  350W |       1MiB /  24576MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA GeForce RTX 3090        On  |   00000000:AF:00.0 Off |                  N/A |
| 30%   26C    P8             18W /  350W |       1MiB /  24576MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

Exit the node when finished.

```bash
exit
```

## Create a Python Environment

Amarel allows users to install personal software.

https://user-guide-f4258a.gitlab.io/software/installing-software/

### Install `uv`

```bash
curl -LsSf https://astral.sh/uv/install.sh \
    | env UV_INSTALL_DIR="$HOME/.local/bin" \
          UV_NO_MODIFY_PATH=1 sh
```

### Add `uv` to your `$PATH`

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Verify `uv` works with

```bash
uv --version
which uv
```

You should see something similar to

```bash
[ms3978@amarel3 ~]$ uv --version
uv 0.13.0 (x86_64-unknown-linux-gnu)
[ms3978@amarel3 ~]$ which uv
~/.local/bin/uv
[ms3978@amarel3 ~]$
```

If everything works, make add the path modification to your `.bashrc` for future sessions.

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

### Install `uv` Managed Python

```bash
uv python install 3.12
```

Verify with

```bash
uv python list --only-installed
```

### Create a Test Environment

Make sure that you can use `uv` to install Python packages.

```bash
mkdir -p ~/amarel-pytorch-test
cd ~/amarel-pytorch-test
uv venv --python 3.12
```

Test the interpretter you created

```bash
.venv/bin/python --version
```

### Install Basic Packages

```bash
uv pip install numpy
```

```bash
.venv/bin/python -c "import numpy; print(numpy.__version__)"
```

### Install GPU-Enabled PyTorch

```bash
cd ~/amarel-pytorch-test

uv pip install \
    torch==2.11.0 \
    torchvision==0.26.0 \
    --index-url https://download.pytorch.org/whl/cu128
```

Verify everything is working:

```bash
.venv/bin/python -c \
    "import torch; print(torch.__version__); print(torch.version.cuda)"
```

### Confirm PyTorch can Run on a GPU Node

Request a GPU node

```bash
srun --partition=gpu \
     --nodes=1 \
     --ntasks=1 \
     --gres=gpu:1 \
     --cpus-per-task=2 \
     --mem=8G \
     --time=00:15:00 \
     --pty bash
```

From the GPU node, run

```bash
hostname
nvidia-smi
```

to confirm you have GPUs allocated.

From inside the `amarel-pytorch-test` directory, run a test script:

```bash
.venv/bin/python - <<'PY'
import torch

print("PyTorch:", torch.__version__)
print("CUDA build:", torch.version.cuda)
print("CUDA available:", torch.cuda.is_available())

assert torch.cuda.is_available(), "CUDA is unavailable"

print("GPU:", torch.cuda.get_device_name(0))

# Matrix multiplication on the GPU
a = torch.randn(4096, 4096, device="cuda")
b = torch.randn(4096, 4096, device="cuda")

torch.cuda.synchronize()

c = a @ b

torch.cuda.synchronize()

print("Result shape:", c.shape)
print(
    "Peak allocated GPU memory:",
    round(torch.cuda.max_memory_allocated() / 1e9, 3),
    "GB",
)
print("GPU test successful!")
PY
```