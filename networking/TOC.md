

---

### The Complete Network Engineering Handbook: From Fundamentals to Automation

**Subtitle:** *A Progressive Guide to Modern Networking, Aligning with Industry Standards (CompTIA, Cisco, IEEE, IETF)*

---

### Part I: Foundations – How Data Begins Its Journey

*This section assumes no prior knowledge and builds the essential mental model of how communication works.*

### [Chapter 1: The What and Why of Networks](1.%20foundations_how_data_begins_its_journey/1.%20the_what_and_why_of_networks.ipynb)
    - 1.1 Defining a Network: Beyond Just Computers
    - 1.2 The Core Purpose: Sharing Resources and Information
    - 1.3 Types of Networks by Scale: PAN, LAN, CAN, MAN, WAN
    - 1.4 Network Topologies: Bus, Star, Ring, Mesh, Hybrid (Advantages/Disadvantages)
    - 1.5 Introduction to Network Architectures: Client-Server vs. Peer-to-Peer

### [Chapter 2: The Universal Language: Understanding Protocols](1.%20foundations_how_data_begins_its_journey/2.%20the_universal_language_understanding_protocols.ipynb)
    - 2.1 What is a Protocol? The Analogy of Human Language
    - 2.2 The Need for Standardization: The Role of IEEE, IETF, and W3C
    - 2.3 An Introduction to the Internet Protocol (IP)
    - 2.4 An Introduction to Ethernet

### [Chapter 3: The Rulebook: The OSI and TCP/IP Models](1.%20foundations_how_data_begins_its_journey/3.%20the_rulebook_the_osi_and_tcpip_models.ipynb)
    - 3.1 The Problem: Why We Need Layered Models
    - 3.2 The OSI Model (Layer 1 to 7): A Conceptual Framework
        - Physical, Data Link, Network, Transport, Session, Presentation, Application
    - 3.3 The TCP/IP Model (Link, Internet, Transport, Application): The Practical Model of the Internet
    - 3.4 Encapsulation and De-encapsulation: The Data Journey (PDUs: Bits, Frames, Packets, Segments)
    - 3.5 A Side-by-Side Comparison of OSI and TCP/IP

---

### Part II: The Physical and Data Link Layers – The Hardware and Local Delivery

*This section focuses on the tangible parts of the network and how devices on the same local network communicate.*

### [Chapter 4: The Physical Layer (L1): Cables, Connectors, and Signals](2.%20the_physical_and_data_link_layers_the_hardware_and_local_delivery/4.%20the_physical_layer_cables_connectors_and_signals.ipynb)
    - 4.1 Copper Cabling: Unshielded Twisted Pair (UTP) and Shielded Twisted Pair (STP)
        - Categories (Cat5e, Cat6, Cat6a, Cat8) and Their Applications
        - Straight-through vs. Crossover Cables
    - 4.2 Fiber Optic Cabling: Single-mode vs. Multi-mode, Connectors (LC, SC, ST)
    - 4.3 Ethernet over Coaxial (Legacy) and other media
    - 4.4 Wireless Physics: Frequencies (2.4GHz, 5GHz, 6GHz), Channels, and Signal Strength
    - 4.5 Understanding Ethernet Standards (e.g., 1000BASE-T, 10GBASE-SR)

### [Chapter 5: The Data Link Layer (L2): The NIC, Switching, and the MAC Address](2.%20the_physical_and_data_link_layers_the_hardware_and_local_delivery/5.%20the_data_link_layer_the_nic_switching_and_the_mac_address.ipynb)
    - 5.1 The Role of the Data Link Layer: Node-to-Node Delivery
    - 5.2 The Network Interface Card (NIC) and the MAC Address: Structure and Uniqueness
    - 5.3 Introduction to Ethernet Frames: Structure and Fields
    - 5.4 The Switch: The Core L2 Device
        - MAC Address Tables: How Switches Learn
        - Forward/Filter Decisions
    - 5.5 CSMA/CD: The Legacy of Half-Duplex and Collisions
    - 5.6 ARP (Address Resolution Protocol): Finding the MAC address for a known IP
    - 5.7 VLANs (Virtual LANs): Logically Segmenting a Switch
        - Trunking and 802.1Q Tagging
        - The Native VLAN

---

### Part III: The Network and Transport Layers – Addressing, Routing, and Reliable Delivery

*This is the core of the book, covering IP addressing, subnetting, and the protocols that govern internetwork communication.*

### [Chapter 6: The Network Layer (L3): IP Addressing (IPv4)](3.%20the_network_and_transport_layers_addressing_routing_and_reliable_delivery/6.%20the_network_layer_ip_addressing.ipynb)
    - 6.1 The Purpose of the Network Layer: End-to-End Delivery
    - 6.2 The IPv4 Address Structure: 32-bit Dotted Decimal Notation
    - 6.3 The Subnet Mask: Separating Network and Host
    - 6.4 The Default Gateway: The Exit from the LAN
    - 6.5 Public vs. Private IP Addresses (RFC 1918)
    - 6.6 Introduction to Network Address Translation (NAT): Conserving Public IPs
    - 6.7 Special Addresses: Loopback (127.0.0.1), Broadcast, Network Address

### [Chapter 7: The Art of Subnetting and CIDR](3.%20the_network_and_transport_layers_addressing_routing_and_reliable_delivery/7.%20the_art_of_subnetting_and_cidr.ipynb)
    - 7.1 Why Subnet? Efficient IP Address Management
    - 7.2 Classful Addressing (A, B, C) and Its Limitations
    - 7.3 Classless Inter-Domain Routing (CIDR): The `/` Notation
    - 7.4 Subnetting a Network: Borrowing Bits
    - 7.5 Calculating Subnets, Hosts, and Ranges (with Step-by-Step Exercises)
    - 7.6 VLSM (Variable Length Subnet Masks): Subnetting a Subnet for Maximum Efficiency
    - 7.7 Supernetting and Route Summarization

### [Chapter 8: Life Without IPv4: IPv6 Fundamentals](3.%20the_network_and_transport_layers_addressing_routing_and_reliable_delivery/8.%20life_without_ipv4_ipv6_fundamentals.ipynb)
    - 8.1 The Motivation for IPv6: Address Exhaustion
    - 8.2 The IPv6 Address Structure: 128-bit Hexadecimal Notation
    - 8.3 Shortening IPv6 Addresses (Rules)
    - 8.4 IPv6 Address Types: Unicast (Global, Link-Local, Unique Local), Multicast, Anycast
    - 8.5 Neighbor Discovery Protocol (NDP): The IPv6 Replacement for ARP
    - 8.6 Stateless Address Autoconfiguration (SLAAC)
    - 8.7 IPv6 and DNS

### [Chapter 9: The Router and the Routing Table](3.%20the_network_and_transport_layers_addressing_routing_and_reliable_delivery/9.%20the_router_and_the_routing_table.ipynb)
    - 9.1 The Router: The Core L3 Device for Interconnecting Networks
    - 9.2 Anatomy of a Routing Table
        - Directly Connected Networks
        - Static Routes
        - Dynamic Routes (Introduction)
    - 9.3 The Path Selection Process: Longest Prefix Match
    - 9.4 Administrative Distance and Metrics: Choosing the Best Route
    - 9.5 The Internet Control Message Protocol (ICMP): Ping and Traceroute

### [Chapter 10: Dynamic Routing Protocols (IGPs)](3.%20the_network_and_transport_layers_addressing_routing_and_reliable_delivery/10.%20dynamic_routing_protocols.ipynb)
    - 10.1 Why Dynamic Routing? The Failure of Static Routing at Scale
    - 10.2 Autonomous Systems (AS)
    - 10.3 Distance Vector vs. Link-State Routing Protocols
    - 10.4 RIP (Routing Information Protocol): The Legacy Distance Vector
    - 10.5 OSPF (Open Shortest Path First): The Popular Link-State Protocol
        - Areas (Backbone Area 0, Standard Areas), LSAs, SPF Algorithm
    - 10.6 IS-IS: Another Link-State Protocol (Brief Overview)
    - 10.7 EIGRP (Enhanced Interior Gateway Routing Protocol): Cisco's Advanced Distance Vector

### [Chapter 11: The Transport Layer (L4): The Conductor of Communication](3.%20the_network_and_transport_layers_addressing_routing_and_reliable_delivery/11.%20the_transport_layer_the_conductor_of_communication.ipynb)
    - 11.1 The Role of the Transport Layer: Service-to-Service Delivery
    - 11.2 Port Numbers: Identifying the Application (Well-Known, Registered, Ephemeral)
    - 11.3 TCP (Transmission Control Protocol): Connection-Oriented and Reliable
        - The TCP 3-Way Handshake
        - Flow Control (Sliding Windows)
        - Error Recovery and Sequencing
        - TCP Segment Structure
    - 11.4 UDP (User Datagram Protocol): Connectionless and Fast
        - UDP Datagram Structure
        - Common Uses: DNS, VoIP, Video Streaming
    - 11.5 A Detailed Comparison: TCP vs. UDP

---

### Part IV: Essential Services and Application Layer

*This section connects the lower layers to the applications users actually interact with.*

### [Chapter 12: Name Resolution: The Domain Name System (DNS)](4.%20essential_services_and_application_layer/12.%20name_resolution_the_domain_name_system.ipynb)
    - 12.1 The Problem: Remembering IP Addresses
    - 12.2 The DNS Hierarchy: Root, TLDs (`.com`, `.org`), and Authoritative Servers
    - 12.3 How DNS Resolution Works: Recursive and Iterative Queries
    - 12.4 DNS Record Types: A, AAAA, CNAME, MX, TXT, NS, PTR
    - 12.5 `nslookup` and `dig`: Command-Line DNS Tools

### [Chapter 13: Automatic Configuration: The Dynamic Host Configuration Protocol (DHCP)](4.%20essential_services_and_application_layer/13.%20automatic_configuration_the_dynamic_host_configuration_protocol.ipynb)
    - 13.1 Manual vs. Automatic IP Assignment
    - 13.2 The DHCP DORA Process: Discover, Offer, Request, Acknowledge
    - 13.3 DHCP Scope, Lease Time, and Reservations
    - 13.4 DHCP Relay Agents: Helping Clients Across Subnets

### [Chapter 14: Key Application Layer Protocols and Services](4.%20essential_services_and_application_layer/14.%20key_application_layer_protocols_and_services.ipynb)
    - 14.1 HTTP/HTTPS: The Web (Status Codes, Methods, TLS/SSL)
    - 14.2 SMTP, POP3, IMAP: Email Transmission and Retrieval
    - 14.3 FTP and TFTP: File Transfer Protocols
    - 14.4 SNMP (Simple Network Management Protocol): Monitoring Network Devices
    - 14.5 Syslog: Centralized Logging
    - 14.6 NTP (Network Time Protocol): Synchronizing Clocks

---

### Part V: Network Scale and Management

*This section expands the scope to larger networks, introducing WAN technologies, redundancy, and critical management concepts.*

### [Chapter 15: Wide Area Networks (WANs) and Access Technologies](5.%20network_scale_and_management/15.%20wide_area_networks_and_access_technologies.ipynb)
    - 15.1 Leased Lines, MPLS, and Metro Ethernet
    - 15.2 Digital Subscriber Line (DSL) and Cable Modem Technology
    - 15.3 Fiber-to-the-Home (FTTH)
    - 15.4 VPNs (Virtual Private Networks): Site-to-Site and Remote Access (IPsec, SSL VPN)
    - 15.5 SD-WAN (Software-Defined WAN): The Modern Approach

### [Chapter 16: Redundancy and High Availability](5.%20network_scale_and_management/16.%20redundancy_and_high_availability.ipynb)
    - 16.1 The Need for Redundancy: Eliminating Single Points of Failure
    - 16.2 Spanning Tree Protocol (STP): Preventing Loops at Layer 2
        - Root Bridge, BPDUs, Port States (Blocking, Listening, Learning, Forwarding)
        - Rapid Spanning Tree Protocol (RSTP)
    - 16.3 Link Aggregation (EtherChannel / LACP): Combining Links for Bandwidth and Redundancy
    - 16.4 First Hop Redundancy Protocols (FHRP): HSRP, VRRP, GLBP

### [Chapter 17: Network Management and Documentation](5.%20network_scale_and_management/17.%20network_management_and_documentation.ipynb)
    - 17.1 The Importance of Network Documentation
    - 17.2 Logical and Physical Network Diagrams
    - 17.3 Inventory Management (IP Address Management / IPAM)
    - 17.4 Performance Monitoring: CPU, Memory, Bandwidth, Latency, Jitter, Packet Loss
    - 17.5 Capacity Planning

---

### Part VI: Network Security

*A critical, layered approach to protecting the network infrastructure and data.*

### [Chapter 18: Security Fundamentals and Threat Landscape](6.%20network_security/18.%20security_fundamentals_and_threat_landscape.ipynb)
    - 18.1 The CIA Triad: Confidentiality, Integrity, Availability
    - 18.2 Common Threats: Malware, Phishing, DoS/DDoS, Man-in-the-Middle
    - 18.3 Vulnerability, Exploit, and Risk

### [Chapter 19: Network Security Technologies](6.%20network_security/19.%20network_security_technologies.ipynb)
    - 19.1 Firewalls: Stateless (Packet Filtering) vs. Stateful
    - 19.2 Next-Generation Firewalls (NGFW) and Unified Threat Management (UTM)
    - 19.3 Intrusion Detection and Prevention Systems (IDS/IPS)
    - 19.4 Access Control Lists (ACLs): Filtering Traffic on Routers and Switches
    - 19.5 Virtual Private Networks (VPNs) - In-depth
    - 19.6 Network Access Control (NAC): 802.1X

### [Chapter 20: Securing the Network Infrastructure](6.%20network_security/20.%20securing_the_network_infrastructure.ipynb)
    - 20.1 Secure Device Management (SSH vs. Telnet, HTTPS)
    - 20.2 AAA (Authentication, Authorization, Accounting): RADIUS and TACACS+
    - 20.3 Port Security on Switches
    - 20.4 DHCP Snooping and Dynamic ARP Inspection (DAI)
    - 20.5 Control Plane Policing (CoPP)

---

### Part VII: Advanced Topics and Modern Networking

*This section explores cutting-edge technologies and concepts for the advanced learner.*

### [Chapter 21: Network Virtualization and Cloud Networking](7.%20advanced_topics_and_modern_networking/21.%20network_virtualization_and_cloud_networking.ipynb)
    - 21.1 Virtual Switches (vSwitches)
    - 21.2 Network Functions Virtualization (NFV): Virtual Routers, Firewalls
    - 21.3 Overlay Networks: VXLAN (Virtual Extensible LAN)
    - 21.4 Introduction to Cloud Networking: AWS VPC, Azure VNet
    - 21.5 The Challenges of Networking in the Cloud

### [Chapter 22: Software-Defined Networking (SDN) and Network Automation](7.%20advanced_topics_and_modern_networking/22.%20software_defined_networking_and_network_automation.ipynb)
    - 22.1 The Control Plane and Data Plane Separation
    - 22.2 The SDN Architecture (Application, Control, Infrastructure Layers)
    - 22.3 Introduction to Network Automation Tools
        - Why Automate? (Configuration Management, Speed, Consistency)
        - Introduction to Ansible, Python, and NETCONF/RESTCONF
    - 22.4 Infrastructure as Code (IaC) for Networks

### [Chapter 23: Advanced Wireless and Mobility](7.%20advanced_topics_and_modern_networking/23.%20advanced_wireless_and_mobility.ipynb)
    - 23.1 Wireless LAN Controllers (WLCs) and Lightweight APs (CAPWAP)
    - 23.2 Roaming (Layer 2 and Layer 3)
    - 23.3 RF Site Surveys and Design
    - 23.4 Wi-Fi 6 (802.11ax) and Wi-Fi 7: Key Features
    - 23.5 Cellular Networking (4G/LTE, 5G) as WAN Connectivity

### [Chapter 24: Network Troubleshooting Methodology](7.%20advanced_topics_and_modern_networking/24.%20network_troubleshooting_methodology.ipynb)
    - 24.1 The Layered Troubleshooting Approach (Start at L1 or L7?)
    - 24.2 A Structured Methodology: Identify Problem, Establish Theory, Test, Execute, Verify, Document
    - 24.3 Essential Troubleshooting Toolkit:
        - `ping`, `traceroute`, `telnet`, `ssh`
        - `ipconfig/ifconfig`, `arp`, `netstat`, `nslookup`
        - `wireshark` (Packet Analysis)
        - `iperf` (Throughput Testing)

---

### Appendices

- **Appendix A: The Command Line Crash Course** (Essential CLI commands for Windows, Linux/macOS)
- **Appendix B: Binary, Decimal, and Hexadecimal Conversion** (Detailed guide and practice problems)
- **Appendix C: Well-Known Port Number Reference**
- **Appendix D: IEEE 802 Standards Reference**
- **Appendix E: Glossary of Networking Terms**
- **Appendix F: Practice Questions and Scenarios** (for self-testing)