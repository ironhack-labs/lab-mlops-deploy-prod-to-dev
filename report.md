# Project Report

## Process  
I tested if I could build the same conda environment on my Mac using a `.yml` file that was exported from a Windows machine.  

## Issues & Fixes  
- **Didn’t work at first**: The Windows `.yml` had system-specific details that don’t work on macOS.  
- **Fix**: I modified the file in three ways:  

1. **Removed Windows-only packages**  
   - Deleted: `ucrt`, `vc`, `vc14_runtime`, `vcomp14`.  
   - **Reason**: These packages are only available on Windows. macOS doesn’t use them, so conda failed when trying to install them.  

2. **Removed the hard-coded prefix path**  
   - Original line:  
     ```
     prefix: D:\Anaconda\envs\csv_clean
     ```  
   - **Reason**: The prefix is the installation path from the original Windows machine. On macOS this path doesn’t exist, so it caused errors. Conda can create its own path automatically, so removing it fixed the issue.  

3. **Stripped build strings after versions**  
   - Examples:  
     - `bzip2=1.0.8=h2466b09_7` → `bzip2=1.0.8`  
     - `python=3.11.13=h3f84c4b_0_cpython` → `python=3.11.13`  
     - `pip=25.2=h8b19718_0` → `pip=25.2`  
   - **Reason**: The parts after the version (like `=h2466b09_7` or `_cpython`) are build identifiers that depend on the operating system and compiler. They worked on Windows but not on macOS. By removing them, conda picked the right build automatically for my system.  

After these edits, the environment built successfully on macOS.  

## Challenges  
The biggest challenge was that a `.yml` file exported from Windows includes a lot of system-specific details. These don’t transfer well across operating systems, so the file has to be cleaned up before it can be reused on macOS.  

## Conclusion  
This was **my personal experience**: after modifying the `.yml` file, I was able to get the environment running on macOS.  
**Lesson learned:** When sharing `.yml` files, always remove OS-specific packages, file paths, and build strings. This makes the file portable and ensures it works across different systems.  