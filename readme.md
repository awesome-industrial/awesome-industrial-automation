# Awesome Industrial Automation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Open source software, protocols, standards and learning resources for industrial automation.

From the PLC and the fieldbus to SCADA, historians, MES and industrial AI: the tools engineers use to connect,
control and understand machines. Also known as operational technology (OT), the Industrial Internet of Things
(IIoT), Industry 4.0 or smart manufacturing.

Entries are open source unless marked `Commercial`. Commercial products are listed sparingly, as reference points
next to the open source options.

<!-- This file is generated from data/*.yml by scripts/build.py. Edit the data files, not this file. -->

## Contents

- [Protocols and Connectivity](#protocols-and-connectivity)
	- [Modbus](#modbus)
	- [OPC UA](#opc-ua)
	- [MQTT and Sparkplug](#mqtt-and-sparkplug)
	- [Siemens S7](#siemens-s7)
	- [EtherNet/IP and CIP](#ethernetip-and-cip)
	- [BACnet](#bacnet)
	- [EtherCAT and PROFINET](#ethercat-and-profinet)
	- [Power Grid Protocols](#power-grid-protocols)
	- [Multi-protocol Libraries](#multi-protocol-libraries)
- [Edge and Integration](#edge-and-integration)
	- [Edge Platforms and Gateways](#edge-platforms-and-gateways)
	- [Message Brokers](#message-brokers)
	- [Unified Namespace](#unified-namespace)
- [Control and PLC Programming](#control-and-plc-programming)
	- [PLC Runtimes and IDEs](#plc-runtimes-and-ides)
	- [IEC 61131-3 Tooling](#iec-61131-3-tooling)
	- [Motion, CNC and Robotics](#motion-cnc-and-robotics)
- [SCADA and HMI](#scada-and-hmi)
	- [Dashboards and Visualization](#dashboards-and-visualization)
- [Manufacturing Operations](#manufacturing-operations)
	- [MES and Production](#mes-and-production)
	- [Maintenance](#maintenance)
	- [Quality](#quality)
- [Industrial Data](#industrial-data)
	- [Historians and Time Series Databases](#historians-and-time-series-databases)
	- [Information Models](#information-models)
	- [Digital Twins and Simulation](#digital-twins-and-simulation)
- [Industrial AI](#industrial-ai)
	- [Predictive Maintenance and Anomaly Detection](#predictive-maintenance-and-anomaly-detection)
	- [AI Agents and LLMs for OT](#ai-agents-and-llms-for-ot)
	- [Datasets](#datasets)
- [Security](#security)
- [Learning and Community](#learning-and-community)
	- [Standards](#standards)
	- [Books](#books)
	- [Courses and Tutorials](#courses-and-tutorials)
	- [YouTube Channels](#youtube-channels)
	- [Podcasts](#podcasts)
	- [Communities](#communities)
	- [Related Lists](#related-lists)

## Protocols and Connectivity

_Stacks, libraries and tools for the protocols machines speak._

### Modbus

- [ArduinoModbus](https://github.com/arduino-libraries/ArduinoModbus) - Arduino library for Modbus RTU and TCP clients and servers on Arduino boards.
- [digitalpetri modbus](https://github.com/digitalpetri/modbus) - Java 17+ library for Modbus TCP, Modbus TCP Security and Modbus RTU over serial or TCP.
- [FluentModbus](https://github.com/Apollo3zehn/FluentModbus) - Lightweight Modbus TCP and RTU client and server for .NET.
- [j2mod](https://github.com/steveohara/j2mod) - Java Modbus library with master and slave support over TCP, UDP and serial lines.
- [libmodbus](https://github.com/stephane/libmodbus) - Portable C library for Modbus RTU and TCP masters and slaves on Linux, macOS, FreeBSD and Windows.
- [mbpoll](https://github.com/epsilonrt/mbpoll) - Command-line utility to read and write Modbus RTU or TCP slaves from a terminal.
- [mbusd](https://github.com/3cky/mbusd) - Gateway daemon that bridges Modbus TCP clients to Modbus RTU devices on RS-232 or RS-485 lines.
- [Modbus Register Maps](https://github.com/proxus-io/modbus-register-maps) - Machine-readable YAML register maps for energy meters, inverters and drives, with address, data type, byte order, unit and scale.
- [modbus-serial](https://github.com/yaacov/node-modbus-serial) - Pure JavaScript Modbus RTU and TCP client and server for Node.js.
- [ModbusTools](https://github.com/serhmarch/ModbusTools) - Cross-platform GUI client and server simulators for Modbus TCP, UDP, RTU and ASCII.
- [NModbus](https://github.com/NModbus/NModbus) - C# implementation of Modbus masters and slaves over serial RTU and ASCII, TCP and UDP.
- [node-red-contrib-modbus](https://github.com/BiancoRoyal/node-red-contrib-modbus) - Node-RED nodes for reading and writing Modbus TCP and serial devices.
- [Open ModScan](https://github.com/sanny32/OpenModScan) - Free Modbus master utility for Windows and Linux that polls RTU, ASCII and TCP devices and shows registers in a grid.
- [pymodbus](https://github.com/pymodbus-dev/pymodbus) - Modbus client and server stack for Python with serial, TCP, TLS and UDP transports and a built-in simulator.
- [rodbus](https://github.com/stepfunc/rodbus) - Modbus library written in Rust with bindings for C, C++, .NET and Java.
- [simonvetter/modbus](https://github.com/simonvetter/modbus) - Go Modbus client and server supporting RTU, TCP, TCP over TLS and RTU over TCP or UDP.
- [tokio-modbus](https://github.com/slowtec/tokio-modbus) - Asynchronous Modbus RTU and TCP client and server for Rust, built on Tokio.

### OPC UA

- [async-opcua](https://github.com/FreeOpcUa/async-opcua) - OPC UA client and server implementation in Rust.
- [Eclipse Milo](https://github.com/eclipse-milo/milo) - Java implementation of OPC UA with client and server SDKs.
- [gopcua](https://github.com/gopcua/opcua) - Native Go OPC UA library focused on client applications.
- [node-opcua](https://github.com/node-opcua/node-opcua) - OPC UA client and server SDK for Node.js, written in TypeScript.
- [node-red-contrib-opcua](https://github.com/mikakaraila/node-red-contrib-opcua) - Node-RED nodes for OPC UA clients and servers, based on node-opcua.
- [OPC PLC](https://github.com/Azure-Samples/iot-edge-opc-plc) - OPC UA server simulator with nodes that generate random, ramping and anomalous data for testing.
- [OPC Publisher](https://github.com/Azure/Industrial-IoT) - Edge module that subscribes to OPC UA servers and publishes the data as OPC UA PubSub messages to Azure IoT Hub or MQTT.
- [opcua-asyncio](https://github.com/FreeOpcUa/opcua-asyncio) - Asyncio-based OPC UA client and server library for Python, published as asyncua.
- [opcua-client-gui](https://github.com/FreeOpcUa/opcua-client-gui) - Desktop OPC UA client for browsing address spaces, reading, writing and subscribing to nodes.
- [opcua-commander](https://github.com/node-opcua/opcua-commander) - Terminal-based OPC UA client for browsing and monitoring nodes, built on node-opcua.
- [open62541](https://github.com/open62541/open62541) - OPC UA client and server SDK in C99 with PubSub support, suitable for embedded targets.
- [S2OPC](https://gitlab.com/systerel/S2OPC) - Safety and security oriented OPC UA toolkit in C, designed with embedded devices in mind.
- [UA-.NETStandard](https://github.com/OPCFoundation/UA-.NETStandard) - OPC Foundation reference stack for building OPC UA clients and servers in .NET.
- [UA-ModelCompiler](https://github.com/OPCFoundation/UA-ModelCompiler) - Generates NodeSet files and C# or ANSI C code from OPC UA information model designs.
- [UA-Nodeset](https://github.com/OPCFoundation/UA-Nodeset) - NodeSet XML files for the OPC UA core information model and companion specifications.
- [UaExpert](https://www.unified-automation.com/products/development-tools/uaexpert.html) `Commercial` - Free-of-charge OPC UA test client for browsing, data access, alarms, history and method calls.

### MQTT and Sparkplug

- [aiomqtt](https://github.com/empicano/aiomqtt) - Idiomatic asyncio MQTT client for Python.
- [Eclipse Paho C](https://github.com/eclipse-paho/paho.mqtt.c) - MQTT client library in C for Linux, Windows and macOS, with synchronous and asynchronous APIs.
- [Eclipse Paho Go](https://github.com/eclipse-paho/paho.mqtt.golang) - MQTT 3.1.1 client library for Go.
- [Eclipse Paho Python](https://github.com/eclipse-paho/paho.mqtt.python) - MQTT 3.1, 3.1.1 and 5.0 client library for Python.
- [Eclipse Tahu](https://github.com/eclipse-tahu/tahu) - Reference Sparkplug B implementations in Java, C, C#, Python and JavaScript, plus Node-RED nodes.
- [HiveMQ MQTT Client](https://github.com/hivemq/hivemq-mqtt-client) - Java client library for MQTT 5.0 and 3.1.1 with reactive, asynchronous and blocking APIs.
- [MQTT CLI](https://github.com/hivemq/mqtt-cli) - Command-line MQTT 5.0 and 3.1.1 client for publishing, subscribing and testing brokers.
- [MQTT.js](https://github.com/mqttjs/MQTT.js) - MQTT client for Node.js and the browser over TCP, TLS and WebSockets.
- [MQTTnet](https://github.com/dotnet/MQTTnet) - MQTT client and server library for .NET.
- [MQTTX](https://github.com/emqx/MQTTX) - Cross-platform MQTT 5.0 client for the desktop, the command line and the browser.
- [PubSubClient](https://github.com/knolleary/pubsubclient) - Lightweight MQTT client library for Arduino and compatible boards.
- [Sparkplug](https://github.com/eclipse-sparkplug/sparkplug) - Eclipse specification and compatibility kit for stateful MQTT topics and payloads in industrial systems.
- [SparkplugNet](https://github.com/SeppPenner/SparkplugNet) - Library for .NET to build Sparkplug edge nodes and host applications, built on MQTTnet.

### Siemens S7

- [gos7](https://github.com/robinson/gos7) - Go implementation of the Siemens S7 protocol for reading and writing PLC data.
- [node-red-contrib-s7](https://github.com/st-one-io/node-red-contrib-s7) - Node-RED nodes to read and write variables on Siemens S7 PLCs.
- [python-snap7](https://github.com/gijzelaerr/python-snap7) - Pure Python library for the classic S7 protocol, covering S7-300/400 and S7-1200/1500 with PUT/GET enabled.
- [S7.Net Plus](https://github.com/S7NetPlus/s7netplus) - Library for .NET to read and write data on Siemens S7 PLCs over Ethernet.
- [Snap7](https://snap7.sourceforge.net/) - Multi-platform S7 communication suite with client, server and partner components for exchanging data with S7 PLCs.
- [SoftPlc](https://github.com/fbarresi/SoftPlc) - Simulated S7 PLC in a Docker container, with a web API to create and edit data blocks for testing.

### EtherNet/IP and CIP

- [cpppo](https://github.com/pjkundert/cpppo) - Python parser and originator for EtherNet/IP CIP, including a simulated Logix controller.
- [digitalpetri ethernet-ip](https://github.com/digitalpetri/ethernet-ip) - Asynchronous, non-blocking EtherNet/IP client for Java.
- [EEIP.NET](https://github.com/rossmann-engineering/EEIP.NET) - EtherNet/IP library for .NET with explicit and implicit messaging.
- [EIPScanner](https://github.com/nimbuscontrols/EIPScanner) - C++ library for EtherNet/IP scanners with explicit and implicit messaging.
- [gologix](https://github.com/danomagnum/gologix) - EtherNet/IP client and server library for Go, modeled after pylogix.
- [libplctag](https://github.com/libplctag/libplctag) - Portable C library for reading and writing tags on Allen-Bradley and Modbus PLCs over Ethernet.
- [libplctag.NET](https://github.com/libplctag/libplctag.NET) - Wrapper for .NET around libplctag for reading and writing PLC tags.
- [node-ethernet-ip](https://github.com/cmseaton42/node-ethernet-ip) - Lightweight EtherNet/IP API for Node.js to talk to ControlLogix and CompactLogix controllers.
- [OpENer](https://github.com/EIPStackGroup/OpENer) - EtherNet/IP stack in C for I/O adapter devices, with implicit and explicit connections.
- [pycomm3](https://github.com/ottowayi/pycomm3) - Python EtherNet/IP library for reading and writing tags and calling CIP services on Allen-Bradley PLCs.
- [pylogix](https://github.com/dmroeder/pylogix) - Python library to read and write tags on Allen-Bradley ControlLogix and CompactLogix PLCs.

### BACnet

- [BAC0](https://github.com/ChristianTremblay/BAC0) - Python scripting library on top of BACpypes3 for discovering, reading, writing and trending BACnet points.
- [BACnet for .NET](https://github.com/ela-compil/BACnet) - Standalone BACnet stack for .NET to talk to BACnet devices or expose an application as one.
- [BACnet Stack](https://github.com/bacnet-stack/bacnet-stack) - BACnet application, network and MAC layer library in C for embedded devices and command-line tools.
- [bacnet-js](https://github.com/bacnet-js/client) - BACnet protocol stack for Node.js written in TypeScript.
- [BACnet4J](https://github.com/RadixIoT/BACnet4J) - BACnet/IP stack written in Java.
- [BACpypes3](https://github.com/JoelBender/BACpypes3) - Asyncio-based BACnet communications library for Python.
- [YABE](https://sourceforge.net/projects/yetanotherbacnetexplorer/) - Graphical explorer for browsing, reading and writing BACnet devices over MS/TP, Ethernet and IP.

### EtherCAT and PROFINET

- [ethercat_driver_ros2](https://github.com/ICube-Robotics/ethercat_driver_ros2) - Hardware interface for integrating EtherCAT modules with ros2_control.
- [EtherCrab](https://github.com/ethercrab-rs/ethercrab) - Pure Rust EtherCAT main device that runs in std and no_std environments.
- [IgH EtherCAT Master](https://gitlab.com/etherlab.org/ethercat) - EtherCAT main device for Linux, implemented as kernel modules for real-time applications.
- [KickCAT](https://github.com/leducp/KickCAT) - EtherCAT master and slave stack written in C++.
- [p-net](https://github.com/rtlabs-com/p-net) - PROFINET device stack in C for embedded devices.
- [pysoem](https://github.com/bnjmnp/pysoem) - Cython wrapper around SOEM for writing EtherCAT master applications in Python.
- [SOEM](https://github.com/OpenEtherCATsociety/SOEM) - Simple open source EtherCAT master library in C.
- [SOES](https://github.com/OpenEtherCATsociety/SOES) - Simple open source EtherCAT slave stack in C for microcontrollers.

### Power Grid Protocols

- [c104](https://github.com/Fraunhofer-FIT-DIEN/iec104-python) - Python module for simulating IEC 60870-5-104 SCADA and RTU communication.
- [CoMPAS OpenSCD](https://github.com/com-pas/compas-open-scd) - Browser-based editor for IEC 61850-6 substation configuration (SCL) files.
- [lib60870](https://github.com/mz-automation/lib60870) - C library for the IEC 60870-5-101 and 104 telecontrol protocols used alongside DNP3 in utilities.
- [lib60870.NET](https://github.com/mz-automation/lib60870.NET) - C# implementation of the IEC 60870-5-101 and 104 protocols.
- [libIEC61850](https://github.com/mz-automation/libiec61850) - C library for IEC 61850 MMS, GOOSE and Sampled Values clients and servers.
- [stepfunc dnp3](https://github.com/stepfunc/dnp3) - DNP3 (IEEE 1815) implementation in Rust with bindings for C, C++, .NET and Java.

### Multi-protocol Libraries

- [Apache PLC4X](https://github.com/apache/plc4x) - Libraries for Java, Go, C and Python that read and write PLCs over S7, Modbus, EtherNet/IP, ADS, OPC UA and more through one API.
- [ICSNPP](https://github.com/cisagov/ICSNPP) - Zeek parsers for industrial protocols including BACnet, DNP3, EtherCAT, EtherNet/IP, Modbus, OPC UA, PROFINET and S7comm.
- [iot-communication](https://github.com/xingshuangs/iot-communication) - Java library for the Siemens S7, Modbus and Mitsubishi MELSEC protocols.
- [IoTClient](https://github.com/zhaopeiym/IoTClient) - Library for .NET Standard covering Modbus, Siemens S7, Mitsubishi, Omron FINS and Allen-Bradley PLC communication.
- [Proxus Drivers](https://github.com/proxus-io/proxus-drivers) - Modbus and OPC UA client drivers for .NET, Native AOT compatible and without third-party dependencies.
- [Wireshark](https://www.wireshark.org/) - Packet analyzer with dissectors for Modbus, OPC UA, S7comm, EtherNet/IP, BACnet, EtherCAT, PROFINET, DNP3 and IEC 61850.

## Edge and Integration

_Gateways, brokers and platforms that move plant data from machines to the systems that use it._

### Edge Platforms and Gateways

- [Apache StreamPipes](https://github.com/apache/streampipes) - Self-service toolbox to connect, analyze and explore industrial IoT data streams, with adapters for PLCs and OPC UA.
- [benthos-umh](https://github.com/united-manufacturing-hub/benthos-umh) - Stream processor with inputs for OPC UA, Siemens S7, Modbus, EtherNet/IP, Beckhoff ADS and Sparkplug B.
- [Eclipse Kura](https://github.com/eclipse-kura/kura) - Java and OSGi framework for IoT edge gateways with field protocol drivers, cloud connectors and remote management.
- [EdgeX Foundry](https://github.com/edgexfoundry/edgex-go) - Vendor-neutral microservice framework for edge data collection, with device services for Modbus, BACnet, MQTT and more.
- [Fledge](https://github.com/fledge-iot/fledge) - Edge platform that collects, processes and forwards sensor and machine data through pluggable south and north services.
- [FlowFuse](https://github.com/FlowFuse/flowfuse) - Platform for deploying, managing and scaling Node-RED instances across edge devices and teams.
- [HiveMQ Edge](https://github.com/hivemq/hivemq-edge) - Edge gateway and MQTT broker that translates OPC UA, Modbus, EtherNet/IP and S7 data into MQTT.
- [Ignition Edge](https://inductiveautomation.com/ignition/edge) `Commercial` - Edge editions of the Ignition platform for device connectivity, local HMI and MQTT publishing at the machine.
- [Kepware Server](https://www.velotic.com/products/kepware/kepware-server) `Commercial` - Windows connectivity server with a large library of device drivers that exposes PLC data over OPC UA, OPC DA and MQTT.
- [Litmus Edge](https://litmus.io/litmus-edge) `Commercial` - Industrial edge platform for collecting, normalizing and analyzing machine data on site.
- [Neuron](https://github.com/emqx/neuron) - Industrial connectivity server that collects device data and publishes it over MQTT, with Modbus drivers in the open source edition.
- [Node-RED](https://github.com/node-red/node-red) - Flow-based low-code tool for event-driven applications, with built-in MQTT and community nodes for Modbus, OPC UA and S7.
- [OpenRemote](https://github.com/openremote/core) - IoT platform with Modbus, MQTT and other agents, asset modelling, rules and dashboards for energy and industrial sites.
- [Proxus](https://proxus.io/platform/) `Commercial` - Industrial data platform that connects PLCs, CNCs and OPC UA servers, models plant data in a Unified Namespace and delivers it to databases and AI.
- [Shifu](https://github.com/Edgenesis/shifu) - Kubernetes-native framework that runs each device as a pod, with drivers for OPC UA, Modbus, MQTT and PLCs.
- [Telegraf](https://github.com/influxdata/telegraf) - Plugin-driven data collection agent with inputs for Modbus, OPC UA, Siemens S7 and MQTT.
- [ThingsBoard IoT Gateway](https://github.com/thingsboard/thingsboard-gateway) - Python gateway with connectors for Modbus, OPC UA, BACnet, S7, MQTT and more that forwards data to ThingsBoard.

### Message Brokers

- [Aedes](https://github.com/moscajs/aedes) - Barebone MQTT broker for Node.js that runs on any stream server.
- [Apache BifroMQ](https://github.com/apache/bifromq) - Distributed, multi-tenant MQTT broker written in Java.
- [Eclipse Mosquitto](https://github.com/eclipse-mosquitto/mosquitto) - Lightweight MQTT 5.0, 3.1.1 and 3.1 broker that ships with the mosquitto_pub and mosquitto_sub clients.
- [EMQX](https://github.com/emqx/emqx) - Distributed MQTT 5.0 broker with a rule engine and data integrations, released under the Business Source License.
- [FlashMQ](https://github.com/halfgaar/FlashMQ) - Multi-threaded MQTT broker in C++ designed to make use of many CPU cores.
- [HiveMQ Community Edition](https://github.com/hivemq/hivemq-community-edition) - Java-based MQTT 3.x and 5 broker that forms the open source core of the HiveMQ platform.
- [Mochi MQTT](https://github.com/mochi-mqtt/server) - Embeddable MQTT v5 broker written in Go.
- [Moquette](https://github.com/moquette-io/moquette) - Lightweight Java MQTT broker that can run standalone or embedded in an application.
- [NanoMQ](https://github.com/nanomq/nanomq) - Lightweight MQTT broker and messaging bus for edge devices, written in C.
- [rumqtt](https://github.com/bytebeamio/rumqtt) - MQTT client library and embeddable broker written in Rust.
- [VerneMQ](https://github.com/vernemq/vernemq) - Distributed MQTT broker built on Erlang/OTP.

### Unified Namespace

- [AMRC Connectivity Stack](https://github.com/AMRC-FactoryPlus/amrc-connectivity-stack) - Open source implementation of the Factory+ framework, built on MQTT Sparkplug with edge cluster management.
- [Grafana MQTT Data Source](https://github.com/grafana/mqtt-datasource) - Grafana plugin that streams live data from any MQTT broker into dashboards.
- [HighByte Intelligence Hub](https://www.highbyte.com/intelligence-hub) `Commercial` - Industrial DataOps software for modeling OT data and publishing it to a Unified Namespace and other targets.
- [i3X](https://github.com/cesmii/i3X) - CESMII specification for a common API to access contextualized manufacturing information platforms.
- [MQTT Explorer](https://github.com/thomasnordquist/MQTT-Explorer) - MQTT client that shows the topics of a broker as a structured, browsable tree.
- [mqtt-spb-wrapper](https://github.com/javier-fg/mqtt-spb-wrapper) - Python wrapper around Eclipse Tahu for building Sparkplug B edge nodes, devices and host applications.
- [United Manufacturing Hub](https://github.com/united-manufacturing-hub/united-manufacturing-hub) - Open source stack for ingesting, contextualizing and storing factory data in a Unified Namespace.

## Control and PLC Programming

_Soft PLCs, IEC 61131-3 and IEC 61499 tooling, motion control, CNC and industrial robotics._

### PLC Runtimes and IDEs

- [Beremiz](https://github.com/beremiz/beremiz) - Integrated IEC 61131-3 development environment and soft PLC runtime for machine automation, built on the MATIEC compiler.
- [CODESYS](https://www.codesys.com/) `Commercial` - Vendor-independent IEC 61131-3 development system and soft PLC runtime used by hundreds of controller manufacturers.
- [Eclipse 4diac FORTE](https://github.com/eclipse-4diac/4diac-forte) - Small, portable IEC 61499 runtime environment for embedded controllers and PCs, programmed from 4diac IDE.
- [Eclipse 4diac IDE](https://github.com/eclipse-4diac/4diac-ide) - Engineering tool for distributed control applications based on the IEC 61499 function block standard.
- [OpenPLC Editor](https://github.com/Autonomy-Logic/openplc-editor) - Cross-platform IEC 61131-3 IDE for writing ladder, structured text and other programs and deploying them to OpenPLC runtimes.
- [OpenPLC Runtime](https://github.com/Autonomy-Logic/openplc-runtime) - Headless soft PLC that runs IEC 61131-3 programs on standard computers with deterministic scan cycles, controlled from OpenPLC Editor.
- [ProviewR](https://www.proviewr.se/) - Integrated process control and automation system for Linux PCs, originally developed by Mandator and SSAB Oxelösund.

### IEC 61131-3 Tooling

- [blark](https://github.com/klauer/blark) - Python parser for Beckhoff TwinCAT structured text and project files, with an experimental code formatter.
- [CfUnit](https://forge.codesys.com/lib/counit/home/Home/) - Unit testing library for CODESYS projects, ported from TcUnit.
- [IEC Checker](https://github.com/iec-checker/iec-checker) - Static analyzer for IEC 61131-3 programs that finds bugs and enforces the PLCopen coding guidelines.
- [l5x](https://github.com/jvalenzuela/l5x) - Python module for reading and modifying Rockwell RSLogix and Studio 5000 L5X export files.
- [MATIEC](https://github.com/beremiz/matiec) - IEC 61131-3 compiler that translates structured text, instruction list and SFC programs to C, used by Beremiz and OpenPLC.
- [OSCAT](https://www.oscat.de/) - Open source IEC 61131-3 function block libraries for building automation, control engineering and general PLC tasks.
- [PLCverif](https://gitlab.com/plcverif-oss) - Formal verification tool from CERN that model checks PLC programs, including Siemens STEP 7 SCL and STL code.
- [RuSTy](https://github.com/PLC-lang/rusty) - Structured text compiler written in Rust that uses LLVM to produce native code for many platforms.
- [TcUnit](https://github.com/tcunit/TcUnit) - Unit testing framework in the xUnit style for Beckhoff TwinCAT 3 PLC code.
- [Twinpack](https://github.com/Zeugwerk/Twinpack) - Package manager for TwinCAT libraries with IDE integration, using its own server or any NuGet feed as package source.
- [vscode-st](https://github.com/Serhioromano/vscode-st) - Visual Studio Code extension with syntax highlighting, snippets and a beta formatter for IEC 61131-3 structured text.

### Motion, CNC and Robotics

- [FANUC ROS 2 Driver](https://github.com/FANUC-CORPORATION/fanuc_driver) - Official ROS 2 driver from FANUC for controlling and monitoring FANUC industrial robots.
- [grblHAL](https://github.com/grblHAL/core) - G-code interpreter and CNC motion controller for 32-bit microcontrollers, with a hardware abstraction layer and plugin system.
- [KUKA ROS 2 Drivers](https://github.com/kroshu/kuka_drivers) - ROS 2 drivers for KUKA robots running KSS, iiQKA or Sunrise controllers.
- [LinuxCNC](https://github.com/LinuxCNC/linuxcnc) - Real-time machine controller for mills, lathes, plasma and laser cutters, robot arms and hexapods, running on Linux.
- [MotoROS2](https://github.com/Yaskawa-Global/motoros2) - ROS 2 interface that runs on Yaskawa Motoman robot controllers, built on micro-ROS.
- [MoveIt 2](https://github.com/moveit/moveit2) - Motion planning, manipulation and collision checking framework for robot arms on ROS 2.
- [Open-RMF](https://github.com/open-rmf/rmf) - Framework for coordinating fleets of mobile robots from different vendors with shared doors, lifts and traffic lanes.
- [OpenPnP](https://github.com/openpnp/openpnp) - Machine control software and hardware designs for SMT pick and place machines, with vision-based part alignment.
- [ROS-Industrial](https://rosindustrial.org/) - Open source project that extends ROS to industrial robots and manufacturing, with drivers, planners and training.
- [ros2_control](https://github.com/ros-controls/ros2_control) - Hardware abstraction and real-time controller framework for robots and actuators in ROS 2.
- [Ruckig](https://github.com/pantor/ruckig) - Real-time, jerk-limited, time-optimal trajectory generation library for robots and machines, in C++ and Python.
- [Tesseract](https://github.com/tesseract-robotics/tesseract) - Lightweight motion planning framework for industrial robot applications, with a ROS-agnostic core and Python bindings.
- [Universal Robots ROS 2 Driver](https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver) - Official ROS 2 driver for Universal Robots CB3 and e-Series collaborative arms.

## SCADA and HMI

_Supervisory control, operator screens and plant dashboards._

- [FlowFuse Dashboard](https://github.com/FlowFuse/node-red-dashboard) - Set of Node-RED nodes for building operator dashboards and data entry screens, also known as Node-RED Dashboard 2.0.
- [FUXA](https://github.com/frangoteam/FUXA) - Web-based process visualization and HMI editor with Modbus, OPC UA, Siemens S7, Ethernet/IP, BACnet and MQTT connectors.
- [Ignition](https://inductiveautomation.com/ignition/) `Commercial` - Industrial application platform for SCADA, HMI, alarming and historian, licensed per server with unlimited tags and clients.
- [PyScada](https://github.com/pyscada/PyScada) - Django-based SCADA system with an HTML5 HMI and plugins for Modbus, OPC UA, BACnet, VISA, 1-Wire and other data sources.
- [Rapid SCADA](https://github.com/RapidScada/scada-v6) - Modular .NET platform for monitoring and control systems, with drivers, archives, web-based operator interface and distributed nodes.
- [Scada-LTS](https://github.com/SCADA-LTS/Scada-LTS) - Web-based, multi-platform SCADA system in Java, continuing the ScadaBR and Mango lineage with data sources, alarms and graphical views.

### Dashboards and Visualization

- [ACE.SVG](https://github.com/ACE-IoT-Solutions/ace-svg-react) - Grafana panel that animates your own SVG drawings with live query data through scripted render functions, for plant schematics and mimics.
- [Business Charts](https://github.com/grafana/business-charts) - Grafana panel that renders Apache ECharts visualizations such as gauges, Sankey diagrams and custom charts from query data.
- [Business Forms](https://github.com/grafana/business-forms) - Grafana panel for writing values back to a database or API, useful for setpoints, manual entries and shift data.
- [draw.io](https://github.com/jgraph/drawio) - Diagram editor with built-in P&ID, electrical and process engineering shape libraries, usable offline or self-hosted.
- [Grafana](https://github.com/grafana/grafana) - Dashboard and alerting platform for time series data from historians and databases, with a Canvas panel for simple P&ID-style views.
- [JointJS](https://github.com/clientIO/joint) - SVG diagramming library for JavaScript, used to build interactive P&ID and SCADA/HMI views in web applications.
- [meta2d.js](https://github.com/le5le-com/meta2d.js) - Data-driven 2D engine for web SCADA mimics, process diagrams and control room displays.

## Manufacturing Operations

_Production management, OEE, maintenance and quality on the shop floor._

### MES and Production

- [Carbon](https://github.com/crbnos/carbon) - Manufacturing ERP, MRP, MES and QMS in one system, with quoting, shop floor execution, quality and lot and serial traceability.
- [ERPNext](https://github.com/frappe/erpnext) - Open source ERP whose manufacturing module covers bills of materials, work orders, job cards, production planning and subcontracting.
- [frePPLe](https://github.com/frePPLe/frepple) - Demand forecasting and advanced planning and scheduling tool for manufacturing companies.
- [InvenTree](https://github.com/inventree/InvenTree) - Inventory and parts management system with bills of materials, build orders, stock tracking and a plugin API.
- [Odoo Manufacturing](https://www.odoo.com/app/manufacturing) - Manufacturing app of the open source Odoo suite, with bills of materials, work orders, work centers and MRP.
- [OpenMES](https://github.com/Mes-Open/OpenMes) - Self-hosted MES for small and mid-sized discrete and batch manufacturers, with work orders, routings, material lots, downtime and tablet terminals.
- [Point85 OEE](https://github.com/point85/OEE-Designer) - OEE data collection and calculation applications that resolve OPC UA, OPC DA, MQTT, Modbus and database events into availability, performance and quality.
- [qcadoo MES](https://github.com/qcadoo/mes) - Web-based production management system for small and medium manufacturers, covering orders, technologies, planning and shop floor tracking.

### Maintenance

- [Atlas CMMS](https://github.com/Grashjs/cmms) - Self-hosted maintenance management system with web and mobile apps for work orders, preventive maintenance, assets and spare parts.
- [IBM Maximo](https://www.ibm.com/products/maximo) `Commercial` - Enterprise asset management suite for asset registers, work management, and preventive and condition-based maintenance.
- [Odoo Maintenance](https://www.odoo.com/app/maintenance) - Maintenance app of the open source Odoo suite, with equipment records, corrective and preventive requests and a maintenance calendar.
- [openMAINT](https://www.openmaint.org/) - Asset and maintenance management system for buildings, plants and infrastructure, built on the CMDBuild framework.

### Quality

- [Minitab](https://www.minitab.com/) `Commercial` - Statistical software for SPC, capability analysis, measurement system analysis and design of experiments.
- [OpenRegulatory Templates](https://github.com/openregulatory/templates) - Free document templates for a quality management system under ISO 13485, IEC 62304, ISO 14971 and IEC 62366.
- [qcc](https://github.com/luca-scr/qcc) - R package for statistical quality control charts, process capability analysis, and Pareto and cause-and-effect diagrams.
- [SENAITE](https://github.com/senaite/senaite.core) - Laboratory information management system for sample tracking, analyses and results, used in quality control labs.

## Industrial Data

_Storing, modeling and simulating plant data._

### Historians and Time Series Databases

- [Apache IoTDB](https://github.com/apache/iotdb) - Time series database for industrial devices with a tree-shaped data model, edge-to-cloud sync and compact storage.
- [AVEVA PI System](https://www.aveva.com/en/products/aveva-pi-system/) `Commercial` - Plant historian formerly known as OSIsoft PI, a common reference point for collecting and contextualizing process data.
- [CrateDB](https://github.com/crate/crate) - Distributed SQL database for large volumes of machine and sensor data, with full-text search and dynamic schemas.
- [InfluxDB](https://github.com/influxdata/influxdb) - Time series database for metrics and sensor data, often paired with Telegraf for collection from OPC UA, Modbus and MQTT.
- [openHistorian](https://github.com/GridProtectionAlliance/openHistorian) - Time series historian from the Grid Protection Alliance, used for high-rate synchrophasor and SCADA data in power systems.
- [QuestDB](https://github.com/questdb/questdb) - Column-oriented time series database with SQL, fast ingestion over the InfluxDB line protocol and PostgreSQL wire compatibility.
- [TDengine](https://github.com/taosdata/TDengine) - Time series database built for industrial IoT, with built-in caching, stream processing and data subscription.
- [TimescaleDB](https://github.com/timescale/timescaledb) - PostgreSQL extension for time series with compression, continuous aggregates and retention policies.

### Information Models

- [AASX Package Explorer](https://github.com/eclipse-aaspe/package-explorer) - Windows viewer and editor for AASX packages, the file format of the Asset Administration Shell.
- [AASX Server](https://github.com/eclipse-aaspe/server) - C# server that hosts AASX packages and exposes them over the Asset Administration Shell REST API.
- [B2MML](https://github.com/MESAInternational/B2MML-BatchML) - XML schemas from MESA International that implement the ISA-95 and ISA-88 models for exchanging data between ERP, MES and control systems.
- [Digital Twins Definition Language](https://github.com/Azure/opendigitaltwins-dtdl) - JSON-LD based language from Microsoft for describing the telemetry, properties and relationships of digital twins.
- [Eclipse BaSyx AAS Web UI](https://github.com/eclipse-basyx/basyx-aas-web-ui) - Web interface to browse, edit and visualize Asset Administration Shells on any server that implements the AAS API.
- [Eclipse BaSyx Go Components](https://github.com/eclipse-basyx/basyx-go-components) - Ready-to-run Go implementations of the Asset Administration Shell Part 2 API servers, shipped as Docker images.
- [Eclipse BaSyx Java Server SDK](https://github.com/eclipse-basyx/basyx-java-server-sdk) - Java server and client SDK for Asset Administration Shell V3 repositories, registries and submodel services.
- [Eclipse BaSyx Python SDK](https://github.com/eclipse-basyx/basyx-python-sdk) - Python library to create, serialize and serve Asset Administration Shells and submodels.
- [Eclipse Semantic Modeling Framework SDK](https://github.com/eclipse-esmf/esmf-sdk) - Java SDK and CLI for SAMM aspect models, generating code, JSON schemas, documentation and AAS submodels from them.
- [FA³ST Service](https://github.com/FraunhoferIOSB/FAAAST-Service) - Java implementation of an Asset Administration Shell server from Fraunhofer IOSB, with OPC UA and MQTT endpoints and asset connectors.
- [Manufacturing Ontologies](https://github.com/digitaltwinconsortium/ManufacturingOntologies) - ISA-95 manufacturing ontology expressed as W3C Web of Things descriptions, with a reference solution that feeds it from OPC UA.
- [UA Cloud Library](https://github.com/OPCFoundation/UA-CloudLibrary) - Reference implementation of the OPC Foundation service that stores and serves OPC UA information models through a REST interface.
- [UaModeler](https://www.unified-automation.com/products/development-tools/uamodeler.html) `Commercial` - Graphical editor for designing OPC UA information models and generating NodeSet2 XML and server code.

### Digital Twins and Simulation

- [diagslave](https://www.modbusdriver.com/diagslave.html) `Commercial` - Free command-line Modbus RTU, ASCII and TCP slave simulator for testing masters on Windows and Linux.
- [DWSIM](https://sourceforge.net/projects/dwsim/) - Steady-state and dynamic chemical process simulator with a CAPE-OPEN compliant flowsheet editor.
- [Eclipse Ditto](https://github.com/eclipse-ditto/ditto) - Framework that keeps a digital twin of each device in the cloud and exposes its state through HTTP, WebSocket, MQTT and AMQP APIs.
- [Factory I/O](https://factoryio.com/) `Commercial` - Simulated 3D factory with conveyors, sensors and actuators that connects to real or simulated PLCs for training and virtual commissioning.
- [FMPy](https://github.com/CATIA-Systems/FMPy) - Python library to simulate and validate Functional Mock-up Units exported from Modelica, Simulink and other tools.
- [IDAES](https://github.com/IDAES/idaes-pse) - Python process systems engineering framework for modeling, simulating and optimizing chemical and energy processes.
- [Modbus TCP Server](https://github.com/cybcon/modbus-server) - Configurable Modbus TCP server in a Docker image for simulating devices and debugging clients.
- [Modelica Standard Library](https://github.com/modelica/ModelicaStandardLibrary) - Free library of mechanical, electrical, thermal, fluid and control components for building Modelica plant models.
- [OpenModelica](https://github.com/OpenModelica/OpenModelica) - Modelica modeling and simulation environment for multi-domain physical systems such as machines, drives and process plants.
- [OpenTwins](https://github.com/ertis-research/opentwins) - Composable digital twin platform built on Eclipse Ditto, Grafana and other open components, from the University of Malaga.
- [Prosys OPC UA Simulation Server](https://www.prosysopc.com/products/opc-ua-simulation-server/) `Commercial` - Free OPC UA server that publishes simulated signals for testing clients without a real device.
- [SimPy](https://gitlab.com/team-simpy/simpy) - Discrete-event simulation library for Python, used to model production lines, buffers and resource use.

## Industrial AI

_Machine learning on machine data, AI agents that talk to the plant, and the datasets to train them._

### Predictive Maintenance and Anomaly Detection

- [Alibi Detect](https://github.com/SeldonIO/alibi-detect) - Outlier, adversarial and drift detection algorithms for tabular data, time series and images.
- [Anomalib](https://github.com/open-edge-platform/anomalib) - Deep learning library for visual anomaly detection, used to train and deploy surface defect inspection models.
- [Darts](https://github.com/unit8co/darts) - Python library for forecasting and anomaly detection on time series with statistical and deep learning models.
- [Orion](https://github.com/sintel-dev/Orion) - Unsupervised time series anomaly detection library from MIT with ready-made pipelines and a benchmark.
- [Predictive Maintenance Toolbox](https://www.mathworks.com/products/predictive-maintenance.html) `Commercial` - MATLAB toolbox for designing condition indicators, fault classifiers and remaining useful life models.
- [ProgPy](https://github.com/nasa/progpy) - NASA prognostics framework for physics-based and data-driven remaining useful life estimation.
- [PyOD](https://github.com/yzhao062/pyod) - Python library with dozens of outlier detection algorithms under one API, from isolation forests to deep autoencoders.
- [River](https://github.com/online-ml/river) - Online machine learning in Python that updates models one sample at a time, suited to streaming sensor data and drift.
- [sktime](https://github.com/sktime/sktime) - Unified scikit-learn style interface for time series classification, regression, forecasting and anomaly detection.
- [STUMPY](https://github.com/stumpy-dev/stumpy) - Matrix profile library for finding motifs, discords and regime changes in long sensor signals.
- [tsai](https://github.com/timeseriesAI/tsai) - PyTorch and fastai library of deep learning models for time series classification, regression and forecasting.
- [tsfresh](https://github.com/blue-yonder/tsfresh) - Extracts hundreds of time series features and keeps the relevant ones, a common first step for condition monitoring models.

### AI Agents and LLMs for OT

- [AssetOpsBench](https://github.com/IBM/AssetOpsBench) - IBM benchmark and framework for building and evaluating AI agents on industrial asset operations and maintenance tasks.
- [AutoPLC](https://github.com/cangkui/AutoPLC) - Research framework and benchmarks for generating vendor-specific IEC 61131-3 Structured Text with LLMs.
- [kukapay OPC UA MCP](https://github.com/kukapay/opcua-mcp) - Python MCP server with tools to read, write and browse nodes on an OPC UA server.
- [Modbus MCP Server](https://github.com/ezhuk/modbus-mcp) - Python MCP server that reads and writes Modbus registers and coils, with devices named by host, port and unit.
- [OPC UA MCP Server](https://github.com/IndustriAgents/OPCUA-MCP) - MCP server that lets AI agents browse, read and subscribe to OPC UA servers, read-only unless writes are explicitly allowed.
- [Proxus Industrial MCP Server](https://github.com/proxus-io/proxus-mcp) - Read-only Modbus TCP and OPC UA access for AI agents through MCP, shipped as a single Native AOT binary.
- [S7 MCP Bridge](https://github.com/cadugrillo/s7-mcp-bridge) - MCP server that connects AI agents to Siemens S7-1200 and S7-1500 PLCs through their web API.
- [TwinCAT MCP Server](https://github.com/eponce00/twincat-mcp) - MCP server for TwinCAT projects that builds, deploys, runs TcUnit tests and reads PLC data over ADS.

### Datasets

- [AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset) - Synthetic milling machine data with process conditions, tool wear and five labeled failure modes.
- [awesome-industrial-datasets](https://github.com/jonathanwvd/awesome-industrial-datasets) - Curated collection of public industrial datasets, grouped by domain and task.
- [CWRU Bearing Data Center](https://engineering.case.edu/bearingdatacenter) - Vibration data from healthy and seeded-fault ball bearings at Case Western Reserve University, a standard fault diagnosis benchmark.
- [MIMII](https://zenodo.org/records/3384388) - Sound recordings of normal and malfunctioning valves, pumps, fans and slide rails from Hitachi.
- [MVTec AD](https://www.mvtec.com/company/research/datasets/mvtec-ad) - Images of industrial objects and textures with pixel-level defect annotations for unsupervised anomaly detection.
- [NASA PCoE Data Set Repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/) - Run-to-failure prognostics data, including the C-MAPSS turbofan, bearing, battery and milling sets.
- [Paderborn Bearing DataCenter](https://mb.uni-paderborn.de/en/kat/research/bearing-datacenter) - Motor current and vibration data from bearings with artificial and real damage, recorded at Paderborn University.
- [SECOM](https://archive.ics.uci.edu/dataset/179/secom) - Semiconductor production line sensor readings labeled pass or fail, a common feature selection benchmark.
- [SKAB](https://github.com/waico/SKAB) - Skoltech Anomaly Benchmark of sensor data from a water circulation testbed with labeled faults and changepoints.
- [Tennessee Eastman Process Simulation Data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6C3JR1) - Large simulated runs of the Tennessee Eastman chemical process with normal operation and 20 fault types.
- [VisA](https://github.com/amazon-science/spot-diff) - Visual Anomaly dataset from Amazon with 12 object types such as PCBs and capsules, released with the SPot-the-Difference paper.

## Security

_A short set of widely used open source OT security tools. The two lists at the end go much deeper._

- [awesome-industrial-control-system-security](https://github.com/hslatman/awesome-industrial-control-system-security) - Curated list of ICS security tools, papers, conferences and datasets.
- [awesome-industrial-protocols](https://github.com/Orange-Cyberdefense/awesome-industrial-protocols) - Security-oriented reference of industrial protocols with specifications, tools, attacks and detection resources.
- [Caldera for OT](https://github.com/mitre/caldera-ot) - MITRE Caldera plugins that emulate adversary actions over Modbus, BACnet, DNP3, IEC 61850 and other OT protocols.
- [Conpot](https://github.com/mushorg/conpot) - Low-interaction ICS honeypot that emulates PLCs over Modbus, S7, BACnet, IPMI and other protocols.
- [CSET](https://github.com/cisagov/cset) - CISA Cyber Security Evaluation Tool that walks an organization through assessments against IEC 62443, NIST and other standards.
- [GRFICSv2](https://github.com/Fortiphyd/GRFICSv2) - Virtual ICS lab with a 3D chemical plant simulation, PLC, HMI and attacker machines for security training.
- [ICS-Security-Tools](https://github.com/ITI/ICS-Security-Tools) - Collection of tools, protocol references, PCAPs and tips for exploring ICS security, from the University of Illinois ITI.
- [ICSpector](https://github.com/microsoft/ics-forensics-tools) - Microsoft forensics framework that pulls project files and metadata from PLCs to look for anomalous logic.
- [Labshock](https://github.com/zakharb/labshock) - Docker-based OT cyber range with SCADA, PLC, engineering workstation and DMZ for practicing attacks and detection in isolation.
- [Malcolm](https://github.com/cisagov/Malcolm) - Network traffic analysis suite from CISA and Idaho National Laboratory that parses ICS protocols with Zeek and indexes them in OpenSearch.
- [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) - Knowledge base of adversary tactics and techniques observed against industrial control systems.
- [Zeek](https://github.com/zeek/zeek) - Network analysis framework that turns traffic into protocol logs, the base for the ICSNPP industrial protocol parsers.

## Learning and Community

_Standards, books, courses and the places where automation engineers talk shop._

### Standards

- [Asset Administration Shell Specifications](https://industrialdigitaltwin.org/en/content-hub/aasspecifications) - IDTA specifications for the Asset Administration Shell metamodel, API, packaging and security.
- [IEC 61131-3 at PLCopen](https://www.plcopen.org/iec-61131-3) - Overview of the PLC programming languages standard (ST, LD, FBD, SFC) and the PLCopen work built on it.
- [IEC 61499](https://webstore.iec.ch/en/publication/5506) - Function block architecture for distributed, event-driven control applications across many devices.
- [ISA-101](https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards) - Standard for designing, building and maintaining human-machine interfaces in process automation.
- [ISA-88](https://www.isa.org/standards-and-publications/isa-standards/isa-88-standards) - Batch control standard that defines the physical, procedural and recipe models used in batch process automation.
- [ISA-95](https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard) - Enterprise-control system integration standard (IEC 62264) that defines the levels and data models between ERP, MES and control.
- [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) - Series of standards for the security of industrial automation and control systems, from risk assessment to component requirements.
- [OPC UA Online Reference](https://reference.opcfoundation.org/) - Free browsable edition of the OPC UA specifications and companion specifications from the OPC Foundation.
- [Sparkplug Specification](https://sparkplug.eclipse.org/specification/) - Eclipse specification for MQTT topic namespace, payload encoding and state management in industrial systems.

### Books

- [Feedback Systems](https://fbswiki.org/) - Karl Johan Åström and Richard Murray's introduction to feedback control, free to read online (Princeton University Press).
- [IEC 61131-3: Programming Industrial Automation Systems](https://link.springer.com/book/10.1007/978-3-642-12015-2) - Karl-Heinz John and Michael Tiegelkamp explain the languages, data types and program organization of the PLC standard (Springer).
- [Industrial Cybersecurity](https://www.packtpub.com/en-us/product/industrial-cybersecurity-9781800202092) - Pascal Ackerman on monitoring and defending ICS environments, second edition (Packt).
- [Industrial Network Security](https://www.sciencedirect.com/book/9780124201149/industrial-network-security) - Eric Knapp and Joel Thomas Langill on securing networks for SCADA, smart grid and other control systems (Syngress).
- [Industrial Process Automation Systems](https://www.sciencedirect.com/book/9780128009390/industrial-process-automation-systems) - B. R. Mehta and Y. J. Reddy on the design and implementation of DCS, PLC and SCADA based process automation (Elsevier).
- [Industry 4.0: The Industrial Internet of Things](https://link.springer.com/book/10.1007/978-1-4842-2047-4) - Alasdair Gilchrist on IIoT architecture, protocols, middleware and security in manufacturing (Apress).
- [Modelling Control Systems Using IEC 61499](https://digital-library.theiet.org/content/books/ce/pbce095e) - Alois Zoitl and Robert Lewis introduce function blocks and distributed control design with IEC 61499 (IET).
- [OPC Unified Architecture](https://link.springer.com/book/10.1007/978-3-540-68899-0) - Wolfgang Mahnke, Stefan-Helmut Leitner and Matthias Damm cover the OPC UA address space, services and information modeling (Springer).
- [Practical Industrial Internet of Things Security](https://www.packtpub.com/en-us/product/practical-industrial-internet-of-things-security-9781788832687) - Sravani Bhattacharjee on securing connected industrial devices, networks and cloud platforms (Packt).
- [Practical SCADA for Industry](https://www.sciencedirect.com/book/9780750658058/practical-scada-for-industry) - David Bailey and Edwin Wright on SCADA architecture, telemetry, communications and system design (Newnes).

### Courses and Tutorials

- [CISA ICS Virtual Learning Portal](https://ics-training.inl.gov/) - Free online ICS cybersecurity courses from CISA and Idaho National Laboratory.
- [Control Bootcamp](https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m) - Steve Brunton's video lecture series on state-space control, LQR and Kalman filters.
- [Control Tutorials for MATLAB and Simulink](https://ctms.engin.umich.edu/CTMS/) - University of Michigan tutorials on modeling, PID, root locus, frequency and state-space design with worked examples.
- [Inductive University](https://inductiveuniversity.com/) - Free video courses on SCADA, HMI and MES development with Ignition.
- [MQTT Essentials](https://www.hivemq.com/mqtt/) - HiveMQ tutorial series on MQTT concepts, from publish and subscribe to QoS, retained messages and sessions.
- [Siemens Automation Cooperates with Education](https://www.siemens.com/sce) - Siemens education program with free learn and training documents for PLC, HMI and drive programming in TIA Portal.
- [Socratic Instrumentation](https://www.ibiblio.org/kuphaldt/socratic/sinst/) - Free instrumentation and process control course by Tony Kuphaldt, including the Lessons In Industrial Instrumentation textbook.

### YouTube Channels

- [4.0 Solutions](https://www.youtube.com/@4.0Solutions) - Walker Reynolds on Industry 4.0 architecture, the Unified Namespace and IIoT system design.
- [Electrical Automation Hands-On](https://www.youtube.com/@electricalautomation) - Hands-on projects with Siemens, Allen-Bradley, Omron and Beckhoff controllers.
- [Inductive Automation](https://www.youtube.com/@InductiveAutomation) - Ignition tutorials, webinars and conference talks on SCADA and IIoT projects.
- [PLC Professor](https://www.youtube.com/@PLCProfessor) - Lessons on industrial control systems, PLC programming and the electrical components around them.
- [RealPars](https://www.youtube.com/@RealPars) - Animated explainers on PLCs, SCADA, instrumentation and industrial networks.
- [Shane Welcher](https://www.youtube.com/@ShaneWelcher) - Allen-Bradley PLC and FactoryTalk HMI programming walkthroughs, including emulation without hardware.
- [SolisPLC](https://www.youtube.com/@SolisPLC) - PLC programming and automation tutorials for engineers and technicians.
- [Tim Wilborne](https://www.youtube.com/@TimWilborne) - PLC programming and electrical troubleshooting for maintenance technicians.

### Podcasts

- [Automation Ladies](https://automationladies.io/) - Interviews with people working in industrial automation, hosted by women in the field.
- [Industrial IoT Spotlight](https://podcasts.apple.com/us/podcast/industrial-iot-spotlight/id1228185407) - Erik Walenza of IoT ONE interviews practitioners about industrial IoT case studies.
- [Industrial Talk](https://industrialtalk.com/) - Scott MacKenzie interviews people across manufacturing, automation and industrial technology.
- [Manufacturing Happy Hour](https://podcasts.apple.com/us/podcast/manufacturing-happy-hour/id1484626862) - Conversations with manufacturing leaders about plant operations, technology and workforce.
- [The Automation Podcast](https://theautomationblog.com/podcast/) - Shawn Tierney's show with product demos and interviews about PLCs, HMIs and automation technology.
- [The Industrial Security Podcast](https://podcasts.apple.com/us/podcast/the-industrial-security-podcast/id1441395559) - Andrew Ginter and Nate Nelson of Waterfall Security on OT security incidents, standards and engineering.
- [Unsolicited Response](https://podcasts.apple.com/us/podcast/unsolicited-response/id1240062226) - Dale Peterson, founder of the S4 conference, on ICS security news and interviews.

### Communities

- [CODESYS Forge](https://forge.codesys.com/forge/talk/) - Community discussion forum for CODESYS PLC programming.
- [Control.com Forums](https://control.com/forums/) - Discussion forum on automation, process control, instrumentation and industrial networks.
- [Inductive Automation Forum](https://forum.inductiveautomation.com/) - Official community forum for Ignition users and developers.
- [MrPLC](https://forums.mrplc.com/) - Forum and download area for PLC and HMI programming, organized by vendor.
- [PLCtalk](https://www.plctalk.net/forums/) - Long-running forum on PLC programming, HMIs and industrial networking across vendors.
- [r/IndustrialMaintenance](https://www.reddit.com/r/IndustrialMaintenance/) - Subreddit for maintenance technicians on troubleshooting machines, drives and controls.
- [r/PLC](https://www.reddit.com/r/PLC/) - Large subreddit for PLC programmers, controls engineers and technicians.
- [r/SCADA](https://www.reddit.com/r/SCADA/) - Subreddit for SCADA, HMI and control system integration questions.

### Related Lists

- [awesome-digital-twins](https://github.com/edt-community/awesome-digital-twins) - Curated list of digital twin papers, platforms, standards and tools.
- [awesome-iot](https://github.com/HQarroum/awesome-iot) - Curated list of IoT projects, protocols, platforms and resources.
- [awesome-mqtt](https://github.com/awesome-mqtt/awesome-mqtt) - Curated list of MQTT brokers, clients, tools and resources.
- [awesome-opcua](https://github.com/iswunistuttgart/awesome-opcua) - Curated list of OPC UA SDKs, tools and resources from the University of Stuttgart ISW.
- [awesome-time-series](https://github.com/lmmentel/awesome-time-series) - Resources for time series analysis, forecasting, databases and visualization.
- [awesome-TS-anomaly-detection](https://github.com/rob-med/awesome-TS-anomaly-detection) - List of tools and datasets for anomaly detection on time series data.

## Contributing

Contributions are welcome. The quickest way is to
[suggest a resource](https://github.com/awesome-industrial/awesome-industrial-automation/issues/new?template=suggest.yml);
a bot turns it into a pull request. See the [contribution guidelines](contributing.md) for what belongs here.

## Footnotes

Maintained by [Proxus](https://proxus.io) and contributors.
