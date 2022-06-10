# Intro
This work has been accepted for publication in [SmartComp 2022](https://smartcomp.aalto.fi/accepted/).


## Abstract:

The primary contribution of this paper is designing and prototyping a \textit{real-time edge computing system}, *RhythmEdge*, that is capable of detecting changes in blood volume from facial videos (Remote Photoplethysmography; rPPG), enabling cardiovascular health assessment instantly. The benefits of *RhythmEdge* include non-invasive measurement of cardiovascular activity, real-time system operation, inexpensive sensing components, and computing. *RhythmEdge* captures a short video of the skin using a camera and extracts rPPG features to estimate the Photoplethysmography (PPG) signal using a multi-task learning framework while offloading the edge computation. In addition, we intelligently apply a transfer learning approach to the multi-task learning framework to mitigate sensor heterogeneities to scale the *RhythmEdge* prototype to work with a range of commercially available sensing and computing devices. Besides, to further adapt the software stack for resource-constrained devices, we postulate novel pruning and quantization techniques (Quantization: FP32, FP16; Pruned-Quantized: FP32, FP16) that efficiently optimize the deep feature learning while minimizing the runtime, latency, memory, and power usage. We benchmark *RhythmEdge* prototype for three different cameras and edge computing platforms while evaluating it on three publicly available datasets and an in-house dataset collected under challenging environmental circumstances. Our analysis indicates that *RhythmEdge* performs on par with the existing contactless heart rate monitoring systems while utilizing only half of its available resources. Furthermore, we perform an ablation study with and without pruning and quantization to report the model size ( 87 %) vs. inference time (70%) reduction. We attested the efficacy of *RhythmEdge* prototype with a maximum power of  8W  and a memory usage of  290MB , with a minimal latency of  0.0625  seconds and a runtime of  0.64  seconds per  30  frames.

## Research Contributions
- Model Compression. We propose domain-specific compression techniques to compress existing deep learning-based rPPG models while maintaining the baseline model performance (0.15 RMSE). Our approach reduces the model size (10 times), power consumption, memory usage (25%), and latency to enable edge platforms deployment. We validate and ablate our approach on three public datasets by performing empirical and statistical similarity analyses.
- rPPG System Development. We prototype a contact-less system, RhythmEdge, for real-time and offline rPPG estimation. Our prototype is compatible with heterogeneous cameras (differing sensitivity, resolution, fps, etc.) and is executable on diverse resource-constrained edge devices (different architectures). Particularly, RhythmEdge is deployed on three platforms (NVIDIA Jetson Nano, Google Coral Development Board, Raspberry Pi) and facilitates three commercially available cameras (web camera, action camera and DSLR) with an option of storing and notifying longitudinal rPPG.
- Evaluation and Benchmarking. We evaluate RhythmEdge on three public datasets and our collected realistic data for both off-line and real-time operation. Further, we test RhythmEdge thoroughly for robustness, device overheating, time complexity, and memory overheads to ensure stable operation and provide system bench-marking parameters across different design choices. Finally, we open-source our new data, instructions, codes, baseline model weights, and compressed model to enable future research.

## System Overview

<img src="https://github.com/mxahan/rPPG_edge_implementation/blob/main/Images/prototype_.png" width="50%" height="300px"/>

<img src="https://github.com/mxahan/rPPG_edge_implementation/blob/main/Images/overview_approach.png" width="50%" height="300px"/>
Figure: Overview diagram of RhythmEdge development.

## System development Instruction

We are planning to upload a demo paper (accepted in SmartComp) providing the details to develop a rPPG system using off-the-shelf edge devices.

### Set Up for Coral Dev board
[Instructions:](https://coral.ai/docs/dev-board/get-started/#requirements)
(Until screen is terminating writing shows up)
- If command doesn't work
**Solution:** sudo screen /dev/ttyUSB0 115200 (https://github.com/f0cal/google-coral/issues/2)
After that follow instructions again.


### Camera setup
Check under /dev folder whether the camera is detected or not. Usually the coral camera is dev/video0. Others will be either video1 or video2.
- Memory card should be removed first (For AKASO EX7000) and mode should be ‘PC camera not USB’.

### Taking picture
- Use fswebcam
  - sudo apt-get install fswebcam
  - Fswebcam -d /dev/video(select appropriate port no) image_name.jpg
- Push the saved image to github to visualize



