# Module 1: OS Overview

***Go back through slides on local machine.***

## Topics

- History and Evolution of Computers
- What is an OS?
- Computer Sytem Organization
- OS Structure

### History and Evolution of Computers

1. 1945-1955, Vaccum tubes, serial processing, no OS, process concept. Very early on in tech.
2. 1955-1965, transistors, batch processing, but first *real* OS.
    - stored on punch cards
    - converted to magnetic tape
    - submitted to machine as a batch
3. 1965-1980, Integrated circuits, multiprogramming, advent of the mini/micro computer, spooling, and early time-sharing systems
    - multiple jobs running on CPU
    - keeps it close to 100% busy
    - Parralell programming
4. 1980-Present, Very-large scale integration (LSI), rapid time-sharing capability, modular development, focus on user experience, client-server architecture like systems
5. 1990-Present, OS goes mobile

### What is an OS?

The operating system is a special program that:
- controls the execution of other programs
- acts as an interface between apps and hardware

The user interacts with both apps and hardware. The **Kernal** is the headmaster of the hardware and determines what processes get the resources available to it. This is here to make computers easier to use and allows for evolution.

Most general-purpose systems consist of one or more CPUs, main memory, and device controllers. CPU and device controllers have access to memory.

When looking at a graph, lines are called a *bus*. This shows how the hardware is connected.

Few different types of Architecture:
- Von Neumann (Most common)
- Harvard

### Types of Memory
- DRAM (Dynamic Random Access Memory)
    * Volatile semiconductor memory
    * Needs periodic refresh to maintain data
    * Commonly used for main memory
- SRAM (Static Random Access Memory)
    * Volatile semiconductor memory
    * Does not need to be refreshed as DRAM does 
    * Less dense and more expensive than DRAM

*ROM* is also a prevalent type of storage. (Read-Only Memory)

This type of storage is *non-volatile*. Usually referred to as **firmware**. 

A **thread** is what *actually* runs within a processor. These are the workers doing the tasks. Each process starts with exactly *one* thread.

### Lab 6 Documentation

***THIS IS HELPFUL FOR THE EXAM ON FRIDAY***

### Windows Commands

- *tasklist*: Shows a list of all the tasks running
- *taskmgr*: Opens up the task manager
- *procexp*: Opens up Process Explorer
- *notepad*: Opens up a notepad

Notepad requires a lot of processes when needing to print. 

*Three things are required to run:*
- DLLs
- Processors
- Resources

### Linux Commands

- *ps -e*: Lists the processes that are running
- *top*: The linux 'task manager'
- *ps -a*: Lists the processes associted with a terminal
- *top -d .25 -H -p <PID>*: Shows information regarding the process associated with the PID given
- *kill*: Sends signals to precesses
- *renice 10 -p <PID>*: Lowers the priority of the given PID by the value provided. In this case, 10. Basically is nice to other processors by lowering its own priority using this command.

### Windows Mapped Memory Lab

This lab describes how Windows maps memory/resource allocation to processes. 


### Page Replacement Policies FILL THIS IN

- First in First Out (FIFO)
    * Simple algorithm tht maintains an ordered

### Memory Management Lab

This lab will go over memory management in Solaris, Linux, and Windows. 

#### Windows

*Memory Usage Values*

- **Physical Memory**
    - Total: the total amount of physical memory allocated to this system
    - Available: how much physical memory is currently available

- **Commit charge**
    - Current: the current amount of data that we can store in memory on this system
    - Limit: the maximum amount of data that we can store in memory on this system
    - Peak: the highest level of memory usage since the system was last rebooted
    - Peak/Limit: a percentage value showing how much of the limit amount we were using when memory usage peaked
    - Current/Limit: a percentage value showing how much of our limit we are currently using

*CPU Tab*

The graphs of CPU usage are:
- The green line shows total CPU usage (kernel-mode and user-mode)
- The red line shows CPU usage in kernel-mode

**Totals**

This box shows the current total number of object handles, threads, and processes.

**CPU Box**

he CPU box also shows the current number of context switches in the *Context Switch Delta* field.


When overloading the system, both the Physical memeory and System commit usage go through the roof. This causes everything to slow down drastically and will eventually crash.

#### Linux


[RAID Level Chart](https://www.acnc.com/raid/)


### I/O Monitoring Lab

Writing to buffer is about the same for both, Reading and Random Access are faster for the second due to *caching*.

The Random Access time was about the same for the seeker and iostat in Debian, but the r/s column was much faster as the seeker.

To get the Page Fault Equation, divide number of faults by 256. 


**ADS**: Alternate Data Stream

If a file is small enough to fit inside of an MFT record, it will not occupy any clusters!




### Registry

You can use the Windows Registry as a sys admin to determine what applications are being opened on a person's computer. This can describe recent apps, how often they are opened, and other great tidbits about a person's CPU habits.

You can write a script that can take manual reviews, and turn them into automated processes to constantly monitor the system. 

### Windows Registry Lab

*Regedit* is the tool we use to look at the internal registry of a system. You can find all kinds of information such as the *hives*, *USB insertions*, and the *network profiles*.

Regarding *Network Profiles*, this stores information such as:
- Date Created
- Name
- Date Last Accessed
- Description

Windows has a unique way of storing applications, this method is not available in UNIX systems. 

**Useful Tidbit**, go to *HKCR\*\shellex\ContextMenuHandlers*, and add a new key called *CopyTo*. In the default file add {C2FBB630-2971-11D1-A18C-00C04FD75D13} to the *Value* field, **(including the {}!)**

This will add a 'Copy To' Link for each text file added providing a nice QOL addition.


*Slide 385 will be on the final!*

### Windows Network Configuration Lab

This table is not empty due to basic connections when started up. 

When you use *ipconfig*, you can see what dns history you have, and even if you clear it, there will still be some stuff in there because of the static entries along with the dynamically allocated DNS entries which are recreated automatically.

### Windows Sysinternals Lab

1. Use the built-in Windows tasklist utility to list running processes. Type **tasklist** at the
command prompt and look at the output. What fields does it contain?
- It contains the Image name, PID, Session Name, Session number, and Memory usage of all running tasks.

2. Compare this to the Sysinternals tool pslist. Type **pslist** into your command prompt and press
Enter. Your list of processes should look more or less the same – obviously, the last process will
say “PsList” instead of “tasklist” and there may be other slight differences. What fields does pslist give you by default? To find out what the column headers mean, type
pslist /? and read the Help file.
- This gives you the Name, Pid, CPU Time, Elaspsed Time, Number of Threads and Handles, the private virtual memory and priority of the task. 

3. Which process has the most threads? Is this a surprise?
- System, no this is not  because it is running the entire thing.

4. What command would you use to view all of the thread information?
- pslist -d

5. Write two different commands that would both show you information about only the “system”
process:
- pslist -e System
- pslist <System pid>

6. First, open your Firefox browser. Back in your command prompt, type handle /? to view the
Help file and then execute a command that will show the handles belonging to the Firefox
process. What command did you use? Do any of these handles look unusual or odd for Firefox to have?
- handle firefox

### Linux Systemmd Lab

**systemctl** is a useful tool to see the various services running on your system. 

### Linux Network Config

When running, **ip neigh flush all**, the output changes and says it is at <incomplete> from the IPv6 address it was associated with

[ip command cheat sheet](https://access.redhat.com/sites/default/files/attachments/rh_ip_command_cheatsheet_1214_jcs_print.pdf)

### Definitions

- Translation Lookaside Buffer: A high-speed cache set up for highly used page table entries to help mitigate virtual memory references from overloading the physical memory acceses.
- Page Table: Translates logical addresses to physical addresses
