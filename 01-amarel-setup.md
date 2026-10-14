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

## Cluster Basics

Before proceeding, it is helpful to review basic cluster computing terms and concepts. A computing cluster is a collection of interconnected computers, called *nodes*, that work together to provide computational resources. Clusters allow users to run workloads that require more processing power, memory, or storage than is available on a typical personal computer.

### Login Nodes vs. Compute Nodes

**Login nodes** are used to access the cluster, manage files, install software, and submit computational jobs. They are not intended for computationally intensive tasks.

**Compute nodes** are dedicated to executing computational jobs. Users typically access these resources through a job scheduler rather than connecting to them directly.

### Shared Resource Management

Computing clusters are shared by many users, who must share limited computational resources. A **job scheduler**, such as Slurm (the scheduler used by Amarel), manages these resources by allocating compute nodes, CPU cores, memory, and GPUs to submitted jobs. Jobs may be placed in a queue until the requested resources become available. (Yes this means you might need to go grab a coffee while you wait for your job to start!)

### Partitions

A **partition** is a logical grouping of compute nodes with particular hardware configurations or scheduling policies. For example, Amarel provides a `main` partition for general computing and a `gpu` partition for GPU-accelerated workloads. Users select an appropriate partition when submitting jobs, depending on their computational requirements.

### Cores and Hyperthreads

A **CPU core** is a physical processing unit inside a CPU that independently executes program instructions. Modern CPUs contain multiple cores, allowing multiple tasks to execute in parallel. **Hyper-threading** is an Intel technology that allows a single physical CPU core to execute two hardware threads, appearing to the operating system as two *logical CPUs*. AMD provides similar functionality through *simultaneous multithreading* (SMT). Logical CPUs share the resources of their underlying physical core, so two hyperthreads do not generally provide twice the performance of a single physical core.

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
...
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

A successful login will either show a welcome message or simply land you on the login server.

**NOTE: the login server is NOT where you do work. The login server that you land on when you first login to Amarel is NOT the place where you should be running programs or attempting to perform larger computing jobs.**

The login server is a shared computing node that is less powerful than the machines that actually perform heavy computing jobs on Amarel. Many other people are likely on the server at the same time as you are. If you attempt to perform intensive work from this server (e.g., training a large model). As we will see next, we will use the tools on Amarel to request a partition of the GPU servers available and use these servers to do our work.

On successful login, you should see a message like the following.

```text
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

### Confirm You are Logged in Correctly

Once you see the message above, you can explore the login node (again, not this is NOT where you do work) to confirm everything is working as expected.

Start by printing the hostname.

```bash
hostname
```

The hostname should show you are on one of the Amarel login nodes. You should see something like the following.

```text
amarel3.amarel.rutgers.edu
```

This should not be the name of your local machine or any other machine. Later, we will request an interactive GPU session and use `hostname` to confirm that we are not on the login node anymore so we can be sure we are ready to do work without disturbing other users.

Confirm your user name and check where you are.

```bash
whoami
pwd
```

You should be logged in as your Amarel account name and `pwd` should show you are in your home directory on the login node.

See the files in your home directory.

```bash
ls -al
```

These login nodes are shared by many users and are intended for light administrative work. You can use them for configuring and managing the software packages you need to work but must submit all resource intensive jobs through the scheduler that we will review below.

### Understand Your Shell Environment

If you need a review of how the shell environment works reference prior course materials along with the tutorial in the Amarel user guide [here](https://user-guide-f4258a.gitlab.io/environment/shell_startup/).

### (Optional) View and Load Modules with Lmod

Users are free to install their own software on Amarel (see directions in the following sections) however Amarel also provides Lmod for automated package management and development environment configuration.

You can read about Lmod in the [official documentation](https://lmod.readthedocs.io/en/latest/index.html) and [official user guide](https://lmod.readthedocs.io/en/latest/010_user.html). The Amarel user guide provides a [tutorial](https://user-guide-f4258a.gitlab.io/environment/lmod/) on using Lmod.

You are welcome to use Lmod where it makes sense for your projects. In this tutorial we will review standing up a custom Python development environment similar to the environment we have already been using in class.

You can use `ml avail` to list available Lmod packages. You can activate and Lmod environment with `ml <name>`, i.e., `ml cuda` or `ml gcc`.

## Slurm and Job Scheduling Basics

Amarel uses Slurm for cluster resource management and job scheduling. Slurm is responsible for allocating resources to users, providing a framework for starting, executing and monitoring work on allocated resources and scheduling work for future execution. You can read more about job scheduling on Amarel in the user guide [here](https://user-guide-f4258a.gitlab.io/jobs/).

In this class, our basic Slurm workflow is:
1. Inspect resources available to you
2. Submit jobs to partitions that meet your requirements
3. Inspect those jobs to determine their status

The Slurm basics and commands below will enable us to execute that workflow.

### Slurm Basics

The Slurm [quickstart guide](https://slurm.schedmd.com/quickstart.html) introduces Slurm as follows.

*"Slurm is an open source, fault-tolerant, and highly scalable cluster management and job scheduling system for large and small Linux clusters. Slurm requires no kernel modifications for its operation and is relatively self-contained. As a cluster workload manager, Slurm has three key functions. First, it allocates exclusive and/or non-exclusive access to resources (compute nodes) to users for some duration of time so they can perform work. Second, it provides a framework for starting, executing, and monitoring work (normally a parallel job) on the set of allocated nodes. Finally, it arbitrates contention for resources by managing a queue of pending work."*

*"As depicted in Figure 1, Slurm consists of a slurmd daemon running on each compute node and a central slurmctld daemon running on a management node (with optional fail-over twin). The slurmd daemons provide fault-tolerant hierarchical communications."*

![Alt text](images/arch.gif)

These *daemons*, or background processes, manage the nodes, compute resource in Slurm, and *partitions*, which group nodes into logical sets for user jobs to run on.

Slurm will also manage the allocations of resources assigned to a user, the time those resources are allocated, and *job steps*, which are sets of (possibly parallel) tasks within a job.

### Basic Commands

The following commands are helpful to know.

`sinfo` reports the state of partitions and nodes managed by Slurm and provides sorting and filtering options.

`srun` is what we will use to submit a job for execution or initiate job steps interactively. We will see examples of `srun` in the following sections. `srun`provides configurability for the user jobs to specific minimum and maximum node count, processor count, specific nodes to use or not use, and node requirements such as memory or disk space available.

`sbatch` is used to submit a job script for later execution. The script will typically contain one or more srun commands to launch parallel tasks.

`squeue -u $USER` will show your jobs.

`scontrol show job 123456` will provide the reason a job is waiting.

`squeue --start -j 123456` will provide an estimate of how long the job needs to wait before running.

These commands will support our three step workflow in enabling us to inspect partitions, run jobs, and check the status of those jobs.

### Slurm Workflow Step 1: Inspect Partitions

Cluster jobs need to be sent to a partition. A partition defines a list of nodes that the job can run on, given the requirements specified using `srun`.

Before requesting resources (compute nodes), it can be helpful to see what resources are available and what cluster partitions to use for certain resources.

Use commands such as the following examples to explore what cluster resources are available to you.

Get a summary of available partitions.

```bash
# sinfo = get information about available partitions
# -s = summarize
sinfo -s
```

Filter and display the GPU partition details, including nodes, available GPUs, and their current state.

```bash
sinfo --partition=gpu --format="%N %G %T"
```

### Slurm Workflow Step 2: Submit Jobs

Request a GPU using `srun`. Use its arguments to specify your requirements. Here we request a node with one GPU, two CPUs per task, 8GB of memory, for 10 minutes. We specify we want to log onto this node with a Bash shell.

```bash
srun --partition=gpu \
     --gres=gpu:1 \
     --cpus-per-task=2 \
     --mem=8G \
     --time=00:10:00 \
     --pty bash
```

Note that if this command succeeds, you are now on a different host.

```bash
hostname
```

This should confirm you are on a GPU node, e.g., `gpu017.amarel.rutgers.edu`. Once you have confirmed you are on the host node, run `nvidia-smi` to confirm available GPUs. You should see something like this.

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

Note that you will need to exit the node by typing `exit` when finished to get back to your log in shell.

### Slurm Workflow Step 3: Check Status of Jobs

When you submit the job, Slurm responds with the job's ID, which will be used to identify this job in reports from Slurm.

```bash
$ sbatch job.sh
Submitted batch job 123456
```

123456 is the job ID. You can use the job ID to see your jobs, check their status or reason for not running yet, and get estimates of when your jobs will start. For example, to see info about your job ID 123456, do the following.

```bash
squeue -u $USER           # See your jobs
scontrol show job 123456  # Understand why a job is waiting
squeue --start -j 123456  # Estimate its start time
```

You can also see what Slurm partitions are associated with your user name.

```bash
# Show your Slurm associations
sacctmgr show assoc user="$USER"
```

### Slurm Man Pages

The Slurm man pages are available [here](https://slurm.schedmd.com/man_index.html).

### Citing Slurm

Slurm recommends the following citation for research using it.

Jette, M.A., Wickberg, T. (2023). Architecture of the Slurm Workload Manager.
In: Klusáček, D., Corbalán, J., Rodrigo, G.P. (eds) Job Scheduling Strategies
for Parallel Processing. JSSPP 2023. Lecture Notes in Computer Science,
vol 14283. Springer, Cham. https://doi.org/10.1007/978-3-031-43943-8_1

## Create a Python Environment

Now that we have confirmed we can access the cluster, request and access a partition, and submit jobs, we are ready to set up our cluster development environment. Amarel allows users to install personal software to facilitate this. You can read more about installing software on Amarel [here](https://user-guide-f4258a.gitlab.io/software/installing-software/).

### Install `uv`

Start by adding a personal installation of `uv`. Run the following command from your login node.

```bash
curl -LsSf https://astral.sh/uv/install.sh \
    | env UV_INSTALL_DIR="$HOME/.local/bin" \
          UV_NO_MODIFY_PATH=1 sh
```

This will download the `uv` installer and run it to install `uv`.

### Add `uv` to your `$PATH`

Just as with our local development environment setup, we need to add `uv` to the `$PATH`.

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Verify `uv` works.

```bash
uv --version
which uv
```

You should see something similar to the following.

```bash
[<netID>@amarel3 ~]$ uv --version
uv 0.13.0 (x86_64-unknown-linux-gnu)
[<netID>@amarel3 ~]$ which uv
~/.local/bin/uv
[<netID>@amarel3 ~]$
```

If everything works, make add the path modification to your `.bashrc` for future sessions.

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

### Install `uv` Managed Python

With `uv` installed, you can install whatever version of Python you need for your own projects without affecting the Amael system Python.

Install Python 3.12.

```bash
uv python install 3.12
```

Verify the installation.

```bash
uv python list --only-installed
```

### Create a Test Virtual Environment

Now we will built a test virtual environment to confirm we can work with PyTorch and other Python packages.

--

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