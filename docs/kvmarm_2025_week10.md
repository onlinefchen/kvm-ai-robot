# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 09:28:50

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 220
- **总 Thread 数**: 28
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 21 threads (192 邮件)
- **RFC**: 1 threads (3 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Other**: 5 threads (23 邮件)

---

## 📌 PATCH

共 21 个 thread

---

### Thread 1: [PATCH v7 01/45] KVM: Prepare for handling only shared mappings
 in mmu_notifier events

**📧 邮件数**: 36 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 3 Mar 2025 09:36:20 +1000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 的补丁系列，特别是第一个补丁（PATCH v7 01/45），旨在为处理仅共享映射的 mmu_notifier 事件做准备。该补丁的背景是，之前的讨论中提到新增的成员（only_private 和 only_shared）与 attr_filter 的成员重复，建议使用 attr_filter 作为替代。

在本周的新讨论中，参与者们对多个补丁进行了审查和反馈。Gavin Shan 对 Steven Price 的补丁进行了多次审阅，指出了一些代码中的细节问题和改进建议，例如在文档中更新 ioctl 命令的描述、合并 WARN_ON() 语句、以及对变量命名的建议等。此外，讨论中还涉及了对 RME（Realm Management Extensions）相关补丁的审查，强调了对文档和代码一致性的关注。

总体来看，本周的讨论集中在补丁的细节改进和代码审查上，参与者们积极提供反馈，以确保补丁的质量和功能的正确性。

#### 📝 邮件列表

1. **[03-03 09:36]** Re: [PATCH v7 01/45] KVM: Prepare for handling only shared mappings
 in mmu_notifier events
   - 发件人: Gavin Shan <gshan@redhat.com>
2. **[03-03 13:42]** Re: [PATCH v7 05/45] arm64: RME: Add wrappers for RMI calls
   - 发件人: Gavin Shan <gshan@redhat.com>
3. **[03-03 13:58]** Re: [PATCH v7 06/45] arm64: RME: Check for RME support at KVM init
   - 发件人: Gavin Shan <gshan@redhat.com>
4. **[03-03 14:10]** Re: [PATCH v7 07/45] arm64: RME: Define the user ABI
   - 发件人: Gavin Shan <gshan@redhat.com>
5. **[03-03 14:42]** Re: [PATCH v7 08/45] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Gavin Shan <gshan@redhat.com>
6. **[03-03 14:48]** Re: [PATCH v7 09/45] kvm: arm64: Expose debug HW register numbers for
 Realm
   - 发件人: Gavin Shan <gshan@redhat.com>
7. **[03-03 14:53]** Re: [PATCH v7 10/45] arm64: kvm: Allow passing machine type in KVM
 creation
   - 发件人: Gavin Shan <gshan@redhat.com>
8. **[03-03 16:25]** Re: [PATCH v7 11/45] arm64: RME: RTT tear down
   - 发件人: Gavin Shan <gshan@redhat.com>
9. **[03-03 17:08]** Re: [PATCH v7 12/45] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Gavin Shan <gshan@redhat.com>
10. **[03-03 15:05]** Re: [PATCH v7 01/45] KVM: Prepare for handling only shared mappings
 in mmu_notifier events
   - 发件人: Steven Price <steven.price@arm.com>
11. **[03-03 15:05]** Re: [PATCH v7 05/45] arm64: RME: Add wrappers for RMI calls
   - 发件人: Steven Price <steven.price@arm.com>
12. **[03-03 18:02]** Re: [PATCH v7 14/45] arm64: RME: Support for the VGIC in realms
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
13. **[03-04 10:45]** Re: [PATCH v7 16/45] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Gavin Shan <gshan@redhat.com>
14. **[03-04 11:03]** Re: [PATCH v7 17/45] arm64: RME: Handle realm enter/exit
   - 发件人: Gavin Shan <gshan@redhat.com>
15. **[03-04 14:35]** Re: [PATCH v7 18/45] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Gavin Shan <gshan@redhat.com>
16. **[03-04 14:52]** Re: [PATCH v7 19/45] KVM: arm64: Handle realm MMIO emulation
   - 发件人: Gavin Shan <gshan@redhat.com>
17. **[03-04 15:09]** Re: [PATCH v7 20/45] arm64: RME: Allow populating initial contents
   - 发件人: Gavin Shan <gshan@redhat.com>
18. **[03-04 15:15]** Re: [PATCH v7 22/45] KVM: arm64: Handle realm VCPU load
   - 发件人: Gavin Shan <gshan@redhat.com>
19. **[03-04 15:29]** Re: [PATCH v7 23/45] KVM: arm64: Validate register access for a Realm
 VM
   - 发件人: Gavin Shan <gshan@redhat.com>
20. **[03-04 15:38]** Re: [PATCH v7 24/45] KVM: arm64: Handle Realm PSCI requests
   - 发件人: Gavin Shan <gshan@redhat.com>
21. **[03-04 15:39]** Re: [PATCH v7 25/45] KVM: arm64: WARN on injected undef exceptions
   - 发件人: Gavin Shan <gshan@redhat.com>
22. **[03-04 15:42]** Re: [PATCH v7 26/45] arm64: Don't expose stolen time for realm guests
   - 发件人: Gavin Shan <gshan@redhat.com>
23. **[03-04 15:47]** Re: [PATCH v7 27/45] arm64: rme: allow userspace to inject aborts
   - 发件人: Gavin Shan <gshan@redhat.com>
24. **[03-04 16:01]** Re: [PATCH v7 28/45] arm64: rme: support RSI_HOST_CALL
   - 发件人: Gavin Shan <gshan@redhat.com>
25. **[03-04 16:02]** Re: [PATCH v7 29/45] arm64: rme: Allow checking SVE on VM instance
   - 发件人: Gavin Shan <gshan@redhat.com>
26. **[03-04 16:23]** Re: [PATCH v7 30/45] arm64: RME: Always use 4k pages for realms
   - 发件人: Gavin Shan <gshan@redhat.com>
27. **[03-04 16:27]** Re: [PATCH v7 31/45] arm64: rme: Prevent Device mappings for Realms
   - 发件人: Gavin Shan <gshan@redhat.com>
28. **[03-04 21:51]** Re: [PATCH v7 34/45] kvm: rme: Hide KVM_CAP_READONLY_MEM for realm
 guests
   - 发件人: Gavin Shan <gshan@redhat.com>
29. **[03-04 17:59]** Re: [PATCH v7 15/45] KVM: arm64: Support timers in realm RECs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
30. **[03-05 09:45]** Re: [PATCH v7 35/45] arm64: RME: Propagate number of breakpoints and
 watchpoints to userspace
   - 发件人: Gavin Shan <gshan@redhat.com>
31. **[03-05 09:46]** Re: [PATCH v7 36/45] arm64: RME: Set breakpoint parameters through
 SET_ONE_REG
   - 发件人: Gavin Shan <gshan@redhat.com>
32. **[03-05 10:15]** Re: [PATCH v7 05/45] arm64: RME: Add wrappers for RMI calls
   - 发件人: Gavin Shan <gshan@redhat.com>
33. **[03-05 13:53]** Re: [PATCH v7 00/45] arm64: Support for Arm CCA in KVM
   - 发件人: Gavin Shan <gshan@redhat.com>
34. **[03-05 16:25]** Re: [PATCH v7 09/45] kvm: arm64: Expose debug HW register numbers for
 Realm
   - 发件人: Steven Price <steven.price@arm.com>
35. **[03-06 09:31]** Re: [PATCH v7 09/45] kvm: arm64: Expose debug HW register numbers for
 Realm
   - 发件人: Gavin Shan <gshan@redhat.com>
36. **[03-07 15:43]** Re: [PATCH v7 12/45] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 2: [PATCH v2 0/4] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM

**📧 邮件数**: 31 | **👥 参与者**: 6 | **📅 开始时间**: Wed, 26 Feb 2025 21:55:16 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的修复补丁，主要集中在 HCRX_EL2 的初始化和其他陷阱的处理。

**原始补丁内容**：
Fuad Tabba 提出的补丁系列（[PATCH v2 0/4]）旨在修复 pKVM 中 HCRX_EL2 的初始化问题，并将相关逻辑重构为独立函数，以便在受保护和非受保护模式下共享。此外，补丁还涉及到 FF-A（Firmware Framework for Arm）缓冲区的初始化。

**之前讨论要点**：
在历史讨论中，参与者们讨论了补丁的细节和必要性，特别是如何将 FF-A 缓冲区的初始化与主机的调用路径分开，以确保在受保护模式下的正确性。同时，关于补丁是否适合在即将发布的 Linux 6.15 版本中合并也引发了讨论。

**本周新讨论与进展**：
本周的讨论主要围绕补丁的具体实现细节展开。Fuad 和 Will Deacon 讨论了如何使用 _ONCE 访问器来避免潜在的竞争条件，以及如何确保在虚拟机的首次运行之前正确初始化 vcpu 的处理。Sebastian Ene 提出了一些关于 FF-A 版本协商的观点，并强调了主机和虚拟机之间的区分，确保主机不会影响虚拟机的行为。最终，参与者们达成共识，认为补丁需要进一步的审查和调整，以确保其在 6.15 版本中的适用性。

#### 📝 邮件列表

1. **[02-26 21:55]** [PATCH v2 0/4] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[02-26 21:55]** [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[02-27 18:17]** [PATCH v2 0/4] KVM: arm64: Separate the hyp FF-A buffers init from
 the host
   - 发件人: Sebastian Ene <sebastianene@google.com>
4. **[02-27 18:17]** [PATCH v2 1/4] KVM: arm64: Use the static initializer for the vesion lock
   - 发件人: Sebastian Ene <sebastianene@google.com>
5. **[02-27 18:17]** [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to the
 ffa header
   - 发件人: Sebastian Ene <sebastianene@google.com>
6. **[02-27 18:17]** [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
7. **[02-27 18:17]** [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx buffer
 to Trustzone
   - 发件人: Sebastian Ene <sebastianene@google.com>
8. **[02-27 20:25]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
9. **[02-27 23:12]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Sebastian Ene <sebastianene@google.com>
10. **[02-28 10:09]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to the ffa header
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[02-28 19:44]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Quentin Perret <qperret@google.com>
12. **[03-03 07:57]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[03-03 19:18]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Will Deacon <will@kernel.org>
14. **[03-03 19:21]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[03-03 21:49]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Will Deacon <will@kernel.org>
16. **[03-03 23:43]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Will Deacon <will@kernel.org>
17. **[03-03 23:44]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Will Deacon <will@kernel.org>
18. **[03-04 00:38]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Sebastian Ene <sebastianene@google.com>
19. **[03-04 00:53]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
20. **[03-04 01:56]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Will Deacon <will@kernel.org>
21. **[03-04 09:54]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
22. **[03-04 09:57]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
23. **[03-04 12:33]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
24. **[03-04 17:38]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
25. **[03-05 00:38]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Will Deacon <will@kernel.org>
26. **[03-05 00:39]** Re: [PATCH v2 1/4] KVM: arm64: Use the static initializer for the
 vesion lock
   - 发件人: Will Deacon <will@kernel.org>
27. **[03-05 00:45]** Re: [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Will Deacon <will@kernel.org>
28. **[03-05 09:41]** Re: [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
29. **[03-05 18:36]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
30. **[03-05 19:34]** Re: [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Will Deacon <will@kernel.org>
31. **[03-06 09:40]** Re: [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>

---

### Thread 3: [PATCH hyperv-next v5 00/11] arm64: hyperv: Support Virtual Trust Level Boot

**📧 邮件数**: 15 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  7 Mar 2025 14:02:52 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM64 架构下支持 Hyper-V 的虚拟信任级别（VTL）启动的补丁集。Roman Kisel 提出了一个补丁系列，旨在使 Hyper-V 代码能够在 ARM64 上以 VTL 模式启动。VTL 是虚拟安全模式的一部分，具体细节可以参考 Microsoft 的文档。

在历史讨论中，补丁系列经历了多个版本的迭代，主要集中在如何通过 SMCCC（标准管理控制调用）检测 Hyper-V 的存在，优化代码结构，以及确保与 ACPI 和设备树（DeviceTree）的兼容性。补丁还涉及到对 VMBus 驱动程序的更新，以支持在 VTL 模式下的中断配置。

本周的新讨论中，Roman Kisel 提交了多个补丁，具体包括：
1. 引入 SMCCC API，以便 KVM/arm64 能够检测 Hyper-V 的存在。
2. 更新 Kconfig 以支持 ARM64 的 VTL 模式，移除对 ACPI 的强制依赖。
3. 提供一个架构中立的实现来获取系统启动时的 VTL。
4. 更新 VMBus 驱动程序以从设备树中获取中断配置，确保在 VTL 模式下的正常运行。

参与者 Arnd Bergmann 对部分补丁表示认可，并提出了一些代码优化建议。整体来看，这一系列补丁的目标是增强 ARM64 在 Hyper-V 环境下的兼容性和性能。

#### 📝 邮件列表

1. **[03-07 14:02]** [PATCH hyperv-next v5 00/11] arm64: hyperv: Support Virtual Trust Level Boot
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
2. **[03-07 14:02]** [PATCH hyperv-next v5 01/11] arm64: kvm, smccc: Introduce and use API for detectting hypervisor presence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
3. **[03-07 14:02]** [PATCH hyperv-next v5 02/11] arm64: hyperv: Use SMCCC to detect hypervisor presence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
4. **[03-07 14:02]** [PATCH hyperv-next v5 03/11] Drivers: hv: Enable VTL mode for arm64
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
5. **[03-07 14:02]** [PATCH hyperv-next v5 04/11] Drivers: hv: Provide arch-neutral implementation of get_vtl()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
6. **[03-07 14:02]** [PATCH hyperv-next v5 05/11] arm64: hyperv: Initialize the Virtual Trust Level field
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
7. **[03-07 14:02]** [PATCH hyperv-next v5 06/11] arm64, x86: hyperv: Report the VTL the system boots in
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
8. **[03-07 14:02]** [PATCH hyperv-next v5 07/11] dt-bindings: microsoft,vmbus: Add interrupts and DMA coherence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
9. **[03-07 14:03]** [PATCH hyperv-next v5 08/11] Drivers: hv: vmbus: Get the IRQ number from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
10. **[03-07 14:03]** [PATCH hyperv-next v5 09/11] Drivers: hv: vmbus: Introduce hv_get_vmbus_root_device()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
11. **[03-07 14:03]** [PATCH hyperv-next v5 10/11] ACPI: irq: Introduce acpi_get_gsi_dispatcher()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
12. **[03-07 14:03]** [PATCH hyperv-next v5 11/11] PCI: hv: Get vPCI MSI IRQ domain from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
13. **[03-08 22:05]** Re: [PATCH hyperv-next v5 03/11] Drivers: hv: Enable VTL mode for arm64
   - 发件人: Arnd Bergmann <arnd@arndb.de>
14. **[03-08 22:08]** Re: [PATCH hyperv-next v5 01/11] arm64: kvm, smccc: Introduce and use API for
 detectting hypervisor presence
   - 发件人: Arnd Bergmann <arnd@arndb.de>
15. **[03-08 22:11]** Re: [PATCH hyperv-next v5 08/11] Drivers: hv: vmbus: Get the IRQ number from
 DeviceTree
   - 发件人: Arnd Bergmann <arnd@arndb.de>

---

### Thread 4: [PATCH v3 00/14] KVM: arm64: FEAT_PMUv3 on Apple hardware

**📧 邮件数**: 15 | **👥 参与者**: 1 | **📅 开始时间**: Wed,  5 Mar 2025 12:26:27 -0800

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 Apple 硬件上实现 KVM 的 PMUv3 特性，涉及到的补丁（patch）共有14个，主要集中在如何在 Apple M 系列处理器上虚拟化 PMUv3 性能监控单元（PMU）。

历史讨论中，之前的版本（v1 和 v2）已经引入了一些基础功能，但本周的新讨论（v3）主要针对 Marc 的反馈进行了调整和改进。具体的补丁内容包括重构事件选择和过滤配置、支持主机和来宾事件过滤、计算 PMCEID、始终支持 SW_INCR PMU 事件等。

本周的进展包括：
1. **补丁重构**：对补丁进行了重排序和结构调整，增加了对 PMUv3 事件的映射支持。
2. **新功能实现**：实现了对来宾模式事件的支持，允许在 VHE 模式下配置来宾的事件过滤。
3. **PMCEID 计算**：补丁中引入了从 arm_pmu 的事件位图计算 PMCEID 的功能，方便在虚拟化时使用。
4. **事件映射**：为 Apple M 系列处理器提供了将 PMUv3 事件映射到硬件事件的帮助函数，确保在虚拟化环境中能够正确处理 PMU 事件。

整体而言，本周的讨论和补丁更新显著增强了 KVM 在 Apple 硬件上虚拟化 PMUv3 的能力，为未来的功能扩展奠定了基础。

#### 📝 邮件列表

1. **[03-05 12:26]** [PATCH v3 00/14] KVM: arm64: FEAT_PMUv3 on Apple hardware
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[03-05 12:26]** [PATCH v3 01/14] drivers/perf: apple_m1: Refactor event select/filter configuration
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[03-05 12:26]** [PATCH v3 02/14] drivers/perf: apple_m1: Support host/guest event filtering
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[03-05 12:26]** [PATCH v3 03/14] KVM: arm64: Compute PMCEID from arm_pmu's event bitmaps
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[03-05 12:26]** [PATCH v3 04/14] KVM: arm64: Always support SW_INCR PMU event
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[03-05 12:26]** [PATCH v3 05/14] KVM: arm64: Use a cpucap to determine if system supports FEAT_PMUv3
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[03-05 12:26]** [PATCH v3 06/14] KVM: arm64: Drop kvm_arm_pmu_available static key
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[03-05 12:26]** [PATCH v3 07/14] KVM: arm64: Use guard() to cleanup usage of arm_pmus_lock
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[03-05 12:26]** [PATCH v3 08/14] KVM: arm64: Move PMUVer filtering into KVM code
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[03-05 12:26]** [PATCH v3 09/14] KVM: arm64: Compute synthetic sysreg ESR for Apple PMUv3 traps
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[03-05 12:26]** [PATCH v3 10/14] KVM: arm64: Advertise PMUv3 if IMPDEF traps are present
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[03-05 12:26]** [PATCH v3 11/14] KVM: arm64: Remap PMUv3 events onto hardware
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[03-05 12:26]** [PATCH v3 12/14] drivers/perf: apple_m1: Provide helper for mapping PMUv3 events
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
14. **[03-05 12:30]** [PATCH v3 13/14] KVM: arm64: Provide 1 event counter on IMPDEF hardware
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
15. **[03-05 12:30]** [PATCH v3 14/14] arm64: Enable IMP DEF PMUv3 traps on Apple M*
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 5: [PATCH v2 00/14] arm: rework id register storage

**📧 邮件数**: 15 | **👥 参与者**: 1 | **📅 开始时间**: Wed,  5 Mar 2025 17:38:05 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM 架构的补丁系列，主要集中在重新设计 ID 寄存器的存储方式。该补丁系列的目标是改进 CPU 模型的支持，并为后续的 CPU 模型补丁提供基础。

1. **原始补丁内容**：补丁系列的主要内容是重新设计 ID 寄存器的存储方式，使用枚举类型进行索引，并更新寄存器描述生成脚本，以便从 Linux 的 sysregs 文件中提取信息。

2. **之前讨论要点**：在之前的讨论中，参与者提到需要将寄存器描述的生成从手动更新改为自动化，以减少错误并提高效率。此外，补丁还包括对 KVM 可写 ID 寄存器的处理。

3. **本周的新讨论和进展**：本周的讨论主要集中在补丁的具体实现和细节上。参与者 Cornelia Huck 提到已经对补丁进行了重构，修复了一些重复定义的问题，并且引入了新的脚本来自动生成寄存器定义。Eric Auger 也提交了多个补丁，涵盖了 ID 寄存器的存储和访问器的添加。最终，补丁系列的目标是简化和提高 ARM CPU 模型的可维护性和可扩展性。

总体而言，该补丁系列通过改进寄存器存储和访问的方式，旨在为 ARM 架构的虚拟化支持提供更好的基础。

#### 📝 邮件列表

1. **[03-05 17:38]** [PATCH v2 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[03-05 17:38]** [PATCH v2 01/14] arm/cpu: Add sysreg definitions in cpu-sysregs.h
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[03-05 17:38]** [PATCH v2 02/14] arm/kvm: add accessors for storing host features into idregs
   - 发件人: Cornelia Huck <cohuck@redhat.com>
4. **[03-05 17:38]** [PATCH v2 03/14] arm/cpu: Store aa64isar0/aa64zfr0 into the idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>
5. **[03-05 17:38]** [PATCH v2 04/14] arm/cpu: Store aa64isar1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
6. **[03-05 17:38]** [PATCH v2 05/14] arm/cpu: Store aa64pfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
7. **[03-05 17:38]** [PATCH v2 06/14] arm/cpu: Store aa64mmfr0-3 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
8. **[03-05 17:38]** [PATCH v2 07/14] arm/cpu: Store aa64dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
9. **[03-05 17:38]** [PATCH v2 08/14] arm/cpu: Store aa64smfr0 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
10. **[03-05 17:38]** [PATCH v2 09/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
11. **[03-05 17:38]** [PATCH v2 10/14] arm/cpu: Store id_pfr0/1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
12. **[03-05 17:38]** [PATCH v2 11/14] arm/cpu: Store id_dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
13. **[03-05 17:38]** [PATCH v2 12/14] arm/cpu: Store id_mmfr0-5 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
14. **[03-05 17:38]** [PATCH v2 13/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
15. **[03-05 17:38]** [PATCH v2 14/14] arm/cpu: Add generated files
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 6: [PATCH v2 0/3] Count pKVM stage-2 usage in secondary pagetable stat

**📧 邮件数**: 13 | **👥 参与者**: 4 | **📅 开始时间**: Tue,  4 Mar 2025 13:43:43 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 pKVM 中统计二级页表的内存使用情况。Vincent Donnefort 提出了一个补丁系列（PATCH v2 0/3），旨在通过在 `/proc/meminfo` 中的 `SecPageTables` 字段来计数与 pKVM 相关的二级内存使用情况。

在历史讨论中，补丁的初步版本（v1）已经提出，并进行了修改，主要包括为 `kvm_hyp_memcache` 添加标志、分离二级内存缓存以及对页全局目录（PGD）的统计。

本周的新讨论中，Vincent 提交了三个补丁：
1. **补丁 1/3**：为 `kvm_hyp_memcache` 添加标志，以便在内存分配和释放回调中进行统计。
2. **补丁 2/3**：在虚拟机拆解时使用独立的内存缓存，以便准确统计分配给二级页表的内存。
3. **补丁 3/3**：在二级页表统计中计数 pKVM 使用的页数，类似于 VHE 模式的处理。

参与者 Oliver Upton 和 Marc Zyngier 对补丁提出了一些小的建议和疑问，整体上对补丁的方向表示支持。此次讨论的进展表明，补丁系列正在逐步完善，并获得了积极的反馈。

#### 📝 邮件列表

1. **[03-04 13:43]** [PATCH v2 0/3] Count pKVM stage-2 usage in secondary pagetable stat
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[03-04 13:43]** [PATCH v2 1/3] KVM: arm64: Add flags to kvm_hyp_memcache
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[03-04 13:43]** [PATCH v2 2/3] KVM: arm64: Distinct pKVM teardown memcache for stage-2
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[03-04 13:43]** [PATCH v2 3/3] KVM: arm64: Count pKVM stage-2 usage in secondary
 pagetable stats
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[03-06 23:20]** Re: [PATCH v2 1/3] KVM: arm64: Add flags to kvm_hyp_memcache
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[03-07 19:55]** [PATCH v2 0/3] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
7. **[03-07 19:55]** [PATCH v2 1/3] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
8. **[03-07 19:55]** [PATCH v2 2/3] KVM: arm64: PMU: Reload when user modifies
 registers
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
9. **[03-07 19:55]** [PATCH v2 3/3] KVM: arm64: PMU: Set raw values from user to
 PM{C,I}NTEN{SET,CLR}, PMOVS{SET,CLR}
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
10. **[03-07 11:35]** Re: [PATCH v2 1/3] KVM: arm64: Add flags to kvm_hyp_memcache
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[03-09 18:40]** Re: [PATCH v2 1/3] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[03-09 18:50]** Re: [PATCH v2 2/3] KVM: arm64: PMU: Reload when user modifies registers
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[03-09 19:01]** Re: [PATCH v2 3/3] KVM: arm64: PMU: Set raw values from user to PM{C,I}NTEN{SET,CLR}, PMOVS{SET,CLR}
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 7: [PATCH v2 0/9] Stage-2 huge mappings for pKVM np-guests

**📧 邮件数**: 10 | **👥 参与者**: 1 | **📅 开始时间**: Thu,  6 Mar 2025 11:00:29 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 非特权虚拟机（np-guests）支持的阶段二（Stage-2）大页映射的补丁系列（PATCH v2 0/9）。该补丁旨在实现 PMD_SIZE 大小的映射，允许在 Stage-2 中安装 PMD 级别的映射，前提是 Stage-1 由 Hugetlbfs 或 THPs 支持。

在历史讨论中，补丁系列的背景和目标已被明确。补丁的主要内容包括对现有 KVM 代码的修改，以支持大页映射的处理、共享和取消共享等功能。参与者 Vincent Donnefort 和 Quentin Perret 提出了多个补丁，涉及对 KVM 相关函数的修改，确保在处理大页时能够正确管理内存。

本周的新讨论中，Vincent Donnefort 提交了多个补丁，逐步实现了对 np-guests 的大页支持。补丁包括对现有函数的扩展，增加了对 nr_pages 参数的支持，以便在共享和取消共享时能够处理大页映射。同时，Quentin Perret 提出了将 pkvm_mappings 转换为区间树的建议，以优化映射管理。最后，补丁系列的最后一部分引入了一个共享 PMD_SIZE fixmap，以提高在安装大页映射时的性能，显著降低了延迟。

总体而言，本周的讨论集中在实现和优化阶段二大页映射的具体细节上，确保 pKVM 在处理非特权虚拟机时的高效性和稳定性。

#### 📝 邮件列表

1. **[03-06 11:00]** [PATCH v2 0/9] Stage-2 huge mappings for pKVM np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[03-06 11:00]** [PATCH v2 1/9] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[03-06 11:00]** [PATCH v2 2/9] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[03-06 11:00]** [PATCH v2 3/9] KVM: arm64: Add a range to __pkvm_host_unshare_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[03-06 11:00]** [PATCH v2 4/9] KVM: arm64: Add a range to __pkvm_host_wrprotect_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[03-06 11:00]** [PATCH v2 5/9] KVM: arm64: Add a range to __pkvm_host_test_clear_young_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[03-06 11:00]** [PATCH v2 6/9] KVM: arm64: Convert pkvm_mappings to interval tree
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[03-06 11:00]** [PATCH v2 7/9] KVM: arm64: Add a range to pkvm_mappings
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[03-06 11:00]** [PATCH v2 8/9] KVM: arm64: Stage-2 huge mappings for np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[03-06 11:00]** [PATCH v2 9/9] KVM: arm64: np-guest CMOs with PMD_SIZE fixmap
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 8: [PATCH v4] arm64: Add basic MTE test

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 27 Feb 2025 15:22:40 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 arm64 架构的基本 MTE（Memory Tagging Extension）测试的补丁（PATCH v4），由 Vladimir Murzin 提出。该补丁旨在测试标签存储访问和不同 MTE 模式下的标签不匹配，涉及多个文件的修改。

在历史讨论中，Vladimir 提交了该补丁，并提供了详细的代码更改，包括新增的测试文件和对现有文件的修改。参与者对补丁的初步反馈是积极的，认为其结构良好。

在本周的新讨论中，Alexandru Elisei 对补丁表示认可，并给予了审核意见。Andrew Jones 提出了一些编译问题，指出在使用 Clang 编译时出现了与寄存器大小不匹配的错误，并建议修改内联汇编的约束。Alexandru 随后提供了修复建议，并讨论了如何在 Clang 中启用 MTE 支持。最终，Andrew Jones 确认了修复后的补丁能够正常工作，并表示已将修改应用到 arm/queue 分支。

总体来看，本周的讨论集中在补丁的编译问题和修复建议上，参与者积极协作，推动了补丁的完善和应用。

#### 📝 邮件列表

1. **[02-27 15:22]** [PATCH v4] arm64: Add basic MTE test
   - 发件人: Vladimir Murzin <vladimir.murzin@arm.com>
2. **[03-06 14:11]** Re: [PATCH v4] arm64: Add basic MTE test
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[03-06 14:25]** Re: [PATCH v4] arm64: Add basic MTE test
   - 发件人: Vladimir Murzin <vladimir.murzin@arm.com>
4. **[03-06 16:31]** Re: [PATCH v4] arm64: Add basic MTE test
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
5. **[03-06 16:45]** Re: [PATCH v4] arm64: Add basic MTE test
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
6. **[03-06 17:11]** Re: [PATCH v4] arm64: Add basic MTE test
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
7. **[03-07 09:24]** Re: [PATCH v4] arm64: Add basic MTE test
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
8. **[03-07 10:26]** Re: [PATCH v4] arm64: Add basic MTE test
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 9: [PATCH 0/3] KVM: arm64: Fixes for 'writable' ID registers in protected mode

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Wed,  5 Mar 2025 15:08:22 -0800

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构下的可写 ID 寄存器在保护模式中的修复，主要包含三个补丁。

首先，原始补丁的内容包括修复以下问题：在 FEAT_EVT 系统中，如果用户空间更改了来宾值，CTR_EL0 不会被捕获；当用户空间启用可写的实现 ID 寄存器时，VPIDR_EL2 被设置为 0；以及修复能力文档中的相关描述。

在之前的讨论中，参与者们关注了补丁的实现细节，特别是如何在保护模式下正确处理 CTR_EL0 和 MIDR_EL1 寄存器的值。Marc Zyngier 提出了将 CTR_EL0 的处理逻辑整合到 pkvm_init_features_from_host() 函数中的建议，以保持代码的整洁性。

本周的新讨论中，Oliver Upton 提交了三个补丁，分别是：将来宾的 CTR_EL0 值复制到 hyp VM、在 MIDR_EL1 可写时将其复制到 hyp VM，以及修复 KVM_CAP_ARM_WRITABLE_IMP_ID_REGS 的文档错误。Marc Zyngier 对前两个补丁表示认可，并给予了审核通过的反馈。最终，Oliver Upton 确认这些补丁已应用到下一个版本中。整体来看，本周的讨论推动了补丁的快速整合与实施。

#### 📝 邮件列表

1. **[03-05 15:08]** [PATCH 0/3] KVM: arm64: Fixes for 'writable' ID registers in protected mode
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[03-05 15:08]** [PATCH 1/3] KVM: arm64: Copy guest CTR_EL0 into hyp VM
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[03-05 15:08]** [PATCH 2/3] KVM: arm64: Copy MIDR_EL1 into hyp VM when it is writable
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[03-05 15:08]** [PATCH 3/3] KVM: arm64: Fix documentation for KVM_CAP_ARM_WRITABLE_IMP_ID_REGS
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[03-06 00:25]** Re: [PATCH 1/3] KVM: arm64: Copy guest CTR_EL0 into hyp VM
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[03-06 00:26]** Re: [PATCH 0/3] KVM: arm64: Fixes for 'writable' ID registers in protected mode
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[03-05 17:01]** Re: [PATCH 0/3] KVM: arm64: Fixes for 'writable' ID registers in protected mode
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[03-06 11:52]** Re: [PATCH 2/3] KVM: arm64: Copy MIDR_EL1 into hyp VM when it is
 writable
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 10: [PATCH 0/9] Stage-2 huge mappings for pKVM np-guests

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 28 Feb 2025 10:25:16 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 非特权虚拟机（np-guests）引入的阶段二大页映射（Stage-2 huge mappings）的补丁系列，共包含九个补丁。主要目标是支持在阶段二中安装 PMD 级别的映射，特别是在阶段一由 Hugetlbfs 或 THPs 支持的情况下。

在历史讨论中，Vincent Donnefort 提出了补丁的初步内容，重点在于如何处理大页映射的相关函数，如 `clean_dcache_guest_page()` 和 `invalidate_icache_guest_page()`，并对 `__pkvm_host_share_guest()` 超调用进行了必要的参数调整，以支持大页映射。Quentin Perret 对补丁提出了一些细节上的担忧，特别是关于地址对齐的问题。

在本周的新讨论中，Vincent 和 Quentin 继续探讨了之前讨论中的问题，Quentin 表达了对双重检查的遗憾，并考虑不再使用某个检查函数。此外，Quentin 提到 fixmap 不支持未对齐地址，并提出可能只需在代码中添加一个警告（WARN_ON()）来处理这一情况。这些讨论表明，开发者们在确保补丁的安全性和有效性方面仍在进行深入的交流与优化。

#### 📝 邮件列表

1. **[02-28 10:25]** [PATCH 0/9] Stage-2 huge mappings for pKVM np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[02-28 10:25]** [PATCH 1/9] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[02-28 10:25]** [PATCH 2/9] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[02-28 18:54]** Re: [PATCH 1/9] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Quentin Perret <qperret@google.com>
5. **[02-28 19:06]** Re: [PATCH 2/9] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Quentin Perret <qperret@google.com>
6. **[03-03 09:03]** Re: [PATCH 2/9] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[03-03 09:08]** Re: [PATCH 1/9] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 11: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling

**📧 邮件数**: 5 | **👥 参与者**: 5 | **📅 开始时间**: Tue, 18 Feb 2025 14:39:55 -0600

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 arm64 架构上启用分支栈采样的补丁系列（PATCH v20 00/11）。该补丁系列旨在通过一种名为分支记录缓冲扩展（BRBE）的架构特性来实现性能监控。补丁的前七个部分主要是一些清理和准备工作，之前已经在邮件列表中发布过。

在历史讨论中，Rob Herring 提到他从 Anshuman 接手了这个补丁系列，并与 Mark 一起对 v19 和 v20 版本进行了较大幅度的重构。Will Deacon 也确认了对清理补丁的应用，并表示感谢。

在本周的新讨论中，Rob Herring 指出没有对补丁 11 进行更改，可能是因为讨论较长，参与者选择跳过。Catalin Marinas 认为 Will Deacon 正在等待 Mark Rutland 对整个系列的审查。Mark Rutland 表示对补丁的结构感到满意，但对过滤逻辑仍有顾虑，认为其复杂性可能导致过滤不当。他承诺会尽快处理这个问题，整体上对补丁系列持积极态度。

总结而言，补丁系列的基础工作已完成，参与者对其整体结构表示认可，但仍需解决特定的过滤逻辑问题。

#### 📝 邮件列表

1. **[02-18 14:39]** [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
2. **[03-01 07:05]** Re: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Will Deacon <will@kernel.org>
3. **[03-03 10:44]** Re: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Rob Herring <robh@kernel.org>
4. **[03-04 11:25]** Re: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
5. **[03-04 16:25]** Re: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Mark Rutland <mark.rutland@arm.com>

---

### Thread 12: [PATCH v3 0/3] Count pKVM stage-2 usage in secondary pagetable stat

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  7 Mar 2025 11:34:08 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 pKVM 的补丁系列，主要目的是在使用 pKVM 时统计与 stage-2 相关的内存使用情况，并将该信息记录在 `/proc/meminfo` 的 `SecPageTables` 字段中。

**补丁内容**：
本次补丁系列包含三个主要部分：
1. 为 `kvm_hyp_memcache` 结构添加标志，以便在内存分配和释放回调中使用。
2. 在 VM 拆除时使用独立的内存缓存来专门处理 stage-2 页表的内存。
3. 统计 pKVM 在二级页表中使用的页面数量，类似于 VHE 模式的处理方式。

**历史讨论要点**：
在之前的讨论中，参与者对补丁的设计和实现进行了反馈，提出了对内存缓存标志的使用建议，以便更好地管理和统计内存使用情况。

**本周新讨论与进展**：
本周的讨论主要集中在补丁的具体实现上，Vincent Donnefort 提交了补丁的更新版本，详细描述了每个补丁的修改内容和目的。补丁通过对 `kvm_hyp_memcache` 结构的修改，确保了在内存分配和释放时能够正确统计 stage-2 页表的内存使用。此外，补丁还确保了在拆除 VM 时能够正确处理与 stage-2 相关的内存缓存。这些修改将有助于提升 pKVM 的内存管理效率。

#### 📝 邮件列表

1. **[03-07 11:34]** [PATCH v3 0/3] Count pKVM stage-2 usage in secondary pagetable stat
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[03-07 11:34]** [PATCH v3 1/3] KVM: arm64: Add flags to kvm_hyp_memcache
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[03-07 11:34]** [PATCH v3 2/3] KVM: arm64: Distinct pKVM teardown memcache for stage-2
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[03-07 11:34]** [PATCH v3 3/3] KVM: arm64: Count pKVM stage-2 usage in secondary
 pagetable stats
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 13: [PATCH 03/18] KVM: arm64: Handle trapping of FEAT_LS64* instructions

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 4 Mar 2025 14:36:19 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下处理 FEAT_LS64* 指令的陷阱。原始的 patch 提出了在 KVM 中实现对这些指令的捕获和处理，以确保虚拟机能够正确响应特定的指令。

在之前的讨论中，Marc Zyngier 和 Fuad Tabba 主要探讨了如何简化代码逻辑，建议使用一个 switch 语句来处理不同的状态（如允许和转发），并在此基础上进行指令注入。Fuad 提出了对代码的重构建议，认为当前的实现可能在处理 L1 客户机运行在 EL2 时存在脆弱性，因为 HCRX_EL2 只适用于 L2 客户机。

在本周的新讨论中，Marc 和 Fuad 继续深入探讨了代码的有效性和潜在问题，特别是关于 EL2 寄存器初始化的规则以及如何处理不同状态下的指令转发。Fuad 还提出了对代码进行进一步重构的想法，以提高其健壮性。

总体来看，本周的讨论集中在代码优化和潜在问题的识别上，双方达成了一致，认为需要对现有实现进行改进，以确保在不同虚拟化环境下的稳定性和可靠性。

#### 📝 邮件列表

1. **[03-04 14:36]** Re: [PATCH 03/18] KVM: arm64: Handle trapping of FEAT_LS64* instructions
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[03-04 15:25]** Re: [PATCH 03/18] KVM: arm64: Handle trapping of FEAT_LS64* instructions
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[03-04 15:47]** Re: [PATCH 03/18] KVM: arm64: Handle trapping of FEAT_LS64* instructions
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[03-04 16:55]** Re: [PATCH 07/18] KVM: arm64: Compute FGT masks from KVM's own FGT tables
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 14: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 21 Feb 2025 10:12:19 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于移除 `PXD_TABLE_BIT` 的补丁（PATCH V2 0/8），该补丁旨在通过依赖 `PXX_TYPE_MASK`、`PXX_TYPE_SECT` 和 `PXX_TYPE_TABLE` 来简化代码。这种抽象方法为即将到来的 D128 页表支持提供了便利，因为 D128 页表不再使用单一的页表位来区分表和块，而是使用跳过级别（SKL）字段。

在历史讨论中，Anshuman Khandual 提出了补丁的初衷，并得到了 Ryan Roberts 的认可，后者建议将所有相关的修改合并为一个补丁，以便于审查和理解。Ryan 认为，逐步移除 `PXX_TABLE_BIT` 的方法是合理的，并且每个补丁都应具备独立的合理性，以保持功能不变并提高代码可读性。

在本周的新讨论中，Anshuman 表示可以考虑将大部分补丁合并为一个，但他更倾向于保持当前的逐步系列方法。Ryan 则建议暂时保留现状，等待其他参与者的意见。这表明在补丁的合并方式上仍存在不同的看法，尚未达成共识。

#### 📝 邮件列表

1. **[02-21 10:12]** [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-28 15:32]** Re: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Ryan Roberts <ryan.roberts@arm.com>
3. **[03-03 10:32]** Re: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[03-03 10:23]** Re: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Ryan Roberts <ryan.roberts@arm.com>

---

### Thread 15: [PATCH 00/11] Tracefs support for pKVM

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 24 Feb 2025 12:13:42 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于为 pKVM 提供 Tracefs 支持的补丁系列，主要由 Vincent Donnefort 提出。该补丁系列的目的是为了增强在受保护模式下的虚拟机监控器的调试和分析能力，Tracefs 被认为是理想的工具，因为它易于使用并且支持多种工具。

在历史讨论中，Vincent 提出了第 2 个补丁，主要是将环形缓冲区相关的数据结构和时间戳编码函数移至公共的 `ring_buffer.h` 头文件，以便在 `ring_buffer.c` 之外进行写入。这一修改为后续的功能扩展奠定了基础。

在本周的新讨论中，Steven Rostedt 对 Vincent 的补丁提出了建议，指出在将内容移至 `include/linux` 目录时，需要添加前缀以避免命名空间冲突，具体提到的前缀包括 `RB_TS_SHIFT`、`RB_TS_MASK` 和 `RB_TS_DELTA_TEST`。这一反馈显示出对补丁的细致审查和对命名规范的关注。

#### 📝 邮件列表

1. **[02-24 12:13]** [PATCH 00/11] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[02-24 12:13]** [PATCH 02/11] ring-buffer: Expose buffer_data_page material
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[03-06 14:56]** Re: [PATCH 02/11] ring-buffer: Expose buffer_data_page material
   - 发件人: Steven Rostedt <rostedt@goodmis.org>

---

### Thread 16: [PATCH] KVM: arm64: Count pKVM stage-2 usage in secondary pagetable stats

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 28 Feb 2025 12:13:55 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，旨在统计 pKVM（Paravirtualized KVM）在二级页表中的使用情况，以便更好地反映内存统计数据。

**原始补丁内容**：
Vincent Donnefort 提出的补丁主要是为了在二级页表统计中计入 pKVM 使用的页面，类似于 VHE（Virtualization Host Extensions）模式的处理。这一补丁的目标是提升内存管理的准确性。

**之前讨论要点**：
在历史讨论中，Vincent 提出了补丁的初衷和实现细节，但并未收到其他参与者的反馈。

**本周的新讨论**：
在本周的讨论中，Oliver Upton 对补丁提出了疑问，指出在清理过程中可能不仅仅涉及到二级页表，还包括其他结构（如 vcpu 结构）。Vincent 随后承认了这一点，并表示他会基于 Android 分支的更改重新整理补丁版本。这表明参与者们正在积极探讨补丁的完善和潜在问题，推动了补丁的进一步发展。

#### 📝 邮件列表

1. **[02-28 12:13]** [PATCH] KVM: arm64: Count pKVM stage-2 usage in secondary pagetable stats
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[03-03 13:18]** Re: [PATCH] KVM: arm64: Count pKVM stage-2 usage in secondary
 pagetable stats
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[03-04 09:03]** Re: [PATCH] KVM: arm64: Count pKVM stage-2 usage in secondary
 pagetable stats
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 17: [PATCH 0/6] Move pKVM ownership state to hyp_vmemmap

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 27 Feb 2025 00:33:04 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于将 pKVM 所有权状态移动到 hyp_vmemmap 的补丁系列。历史讨论中，Quentin Perret 提出了这一补丁的主要目标，包括提高超管状态查找的效率，避免进行页表遍历，以及将超管状态与线性映射范围的存在解耦。这一变更将简化现有代码，并为未来引入其他特性（如超管追踪）奠定基础。

在本周的新讨论中，Vincent Donnefort 提出了一个问题，询问自从引入补丁“KVM: arm64: Don't map 'kvm_vgic_global_state' at EL2 with pKVM”后，SHARED_OWNED 和 SHARED_BORROWED 状态是否仍然相关。他指出，在设置过程中，似乎没有任何 !OWNED 的页面存在于 hyp 中。

总体来看，讨论围绕着补丁的有效性及其对现有状态的影响展开，参与者关注补丁实施后对超管状态管理的潜在变化。

#### 📝 邮件列表

1. **[02-27 00:33]** [PATCH 0/6] Move pKVM ownership state to hyp_vmemmap
   - 发件人: Quentin Perret <qperret@google.com>
2. **[02-27 00:33]** [PATCH 4/6] KVM: arm64: Move hyp state to hyp_vmemmap
   - 发件人: Quentin Perret <qperret@google.com>
3. **[03-03 09:47]** Re: [PATCH 4/6] KVM: arm64: Move hyp state to hyp_vmemmap
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 18: [PATCH] KVM: arm64: Writable TGRAN*_2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  6 Mar 2025 19:40:13 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在允许用户空间写入 ID_AA64MMFR0_EL1 寄存器中的 TGRAN*_2 字段。

**原始补丁内容**：
补丁的核心是允许用户空间设置 ID_AA64MMFR0_EL1.TGRAN*_2 的安全值，同时对于非虚拟化（NV）环境禁止修改这些字段，因为 KVM 提供了基于 PAGE_SIZE 的清理视图。此外，补丁还增加了相关字段到 set_id_regs 自测中。

**之前讨论要点**：
在历史讨论中并未提供具体内容，但可以推测该补丁是对 KVM arm64 相关功能的增强，旨在提升用户空间对特定寄存器的控制能力。

**本周的新讨论与进展**：
本周的讨论中，Sebastian Ott 提交了补丁，并详细描述了补丁的实现细节。Marc Zyngier 对该补丁表示认可，给予了“已确认”（Acked-by）的反馈。这表明补丁得到了积极的响应，可能会在未来的版本中合并。整体来看，本周的讨论主要集中在补丁的确认和认可上，未出现新的争议或问题。

#### 📝 邮件列表

1. **[03-06 19:40]** [PATCH] KVM: arm64: Writable TGRAN*_2
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[03-09 18:24]** Re: [PATCH] KVM: arm64: Writable TGRAN*_2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 19: [PATCH v8 0/6] KVM: arm64: Errata management for VM Live migration

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 21 Feb 2025 14:02:23 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的错误管理与虚拟机实时迁移的补丁（PATCH v8 0/6）。该补丁主要修复了与 CONFIG_CORESIGHT_SOURCE_ETM4X 相关的编译错误，并添加了 R-by 标签，旨在改进虚拟机迁移过程中的错误管理。

在之前的讨论中，Shameer Kolothum 提到该补丁的第八版相较于第七版进行了重要的修正，并提供了一个 QEMU 分支供测试。补丁的具体内容包括对 MIDR（主 ID 寄存器）和 REVIDR（修订 ID 寄存器）的内部读取修改、引入超调用支持以获取目标实现、以及基于实现 CPU 启用错误管理等功能。

在本周的新讨论中，Oliver Upton 确认了该补丁已被应用到下一步的开发中，并提供了各个补丁的具体链接，包括对 MIDR 函数的修改、引入新的超调用支持、以及自测试的添加等。这标志着该补丁的进展顺利，且为未来的开发奠定了基础。

#### 📝 邮件列表

1. **[02-21 14:02]** [PATCH v8 0/6] KVM: arm64: Errata management for VM Live migration
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
2. **[03-05 15:58]** Re: [PATCH v8 0/6] KVM: arm64: Errata management for VM Live migration
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 20: [PATCH v4 00/16] KVM: arm64: Add NV GICv3 support

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 25 Feb 2025 17:29:14 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于为 KVM（Kernel-based Virtual Machine）在 arm64 架构上添加 NV GICv3 支持的补丁（PATCH v4 00/16）。该补丁的目标是增强对 GICv3 的支持，提升虚拟化性能。

在历史讨论中，Marc Zyngier 提供了该补丁的更新版本，并指出补丁在整体上已准备好提交。他提到了一些关键的修改，包括对 IRQ 处理优先级的注释、基于 6.14-rc3 的重基以及修正了 MI INTID 的默认值等。补丁经过多次迭代，得到了社区成员的认可。

在本周的新讨论中，Oliver Upton 对补丁进行了简要的反馈，指出修复了一些拼写错误，并表示该补丁整体状态良好，已经应用到下一个版本中。Upton 的确认表明该补丁得到了积极的进展，且将继续推进。

总结而言，本次讨论围绕 KVM 在 arm64 上实现 NV GICv3 支持的补丁进行，历史讨论提供了补丁的背景和修改细节，而本周的讨论则确认了补丁的接受和进一步的实施。

#### 📝 邮件列表

1. **[02-25 17:29]** [PATCH v4 00/16] KVM: arm64: Add NV GICv3 support
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[03-03 22:27]** Re: [PATCH v4 00/16] KVM: arm64: Add NV GICv3 support
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 21: [PATCH] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sun, 02 Mar 2025 17:12:54 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的性能监控单元（PMU）相关的补丁，主要针对 vPMC（虚拟性能监控计数器）寄存器的 SET_ONE_REG 操作进行修复。

在历史讨论中，Akihiko Odaki 提出了一个补丁，旨在重置当前的性能事件，以确保在设置 vPMC 寄存器（如 PMCCNTR_EL0 和 PMEVCNTR<n>_EL0）时，能够正确反映当前的性能计数。这一补丁是对之前提交的修复（commit 9228b26194d1）的一种延续，后者是针对 GET_ONE_REG 的修复，确保了在某些情况下保存的 vPMC 寄存器值能够正确反映当前状态。

在本周的新讨论中，Oliver Upton 对补丁提出了一些疑虑，特别是关于在虚拟机启动后更改 PMC（性能监控计数器）可能引发的保存/恢复问题。他指出，PMU 的配置在 KVM_RUN 之前可能会发生变化，这可能导致在恢复 vCPU sysregs 后错误地分配性能事件。Upton 建议在 vCPU 已经运行过一次的情况下再调用 kvm_pmu_set_counter_value()，否则应更新寄存器的内存值，以确保性能事件与 vPMU 的最终配置相匹配。此外，他还提到可以简化 getter 和 setter 的手动解码过程。

总体来看，本周的讨论集中在补丁的潜在问题及其解决方案上，反映出对性能监控准确性和虚拟机状态一致性的关注。

#### 📝 邮件列表

1. **[03-02 17:12]** [PATCH] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
2. **[03-03 11:26]** Re: [PATCH] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of __ASSEMBLY__

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 21 Feb 2025 17:45:26 -0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 单元测试库的补丁提案，主题为将所有非 x86 的条件编译指令从 `__ASSEMBLY__` 替换为 `__ASSEMBLER__`。历史讨论中，Sean Christopherson 提出了这个补丁，指出 `__ASSEMBLY__` 是从 Linux 内核继承而来，需手动定义，而 `__ASSEMBLER__` 则由编译器自动定义，能提高代码的可移植性和可维护性。

在之前的讨论中，参与者们关注了补丁的必要性及其对代码的影响，特别是对非 x86 架构的适用性。Sean 还提到忽略 x86 架构，因为其不受此补丁影响。

在本周的新讨论中，Thomas Huth 表示已经应用了该补丁，并询问为何内核使用 `__ASSEMBLY__` 而非 `__ASSEMBLER__`。Sean 回应称，这主要是历史原因，并没有实质性的技术考量。整体来看，本周的讨论确认了补丁的应用，并探讨了其背后的历史背景。

#### 📝 邮件列表

1. **[02-21 17:45]** [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of __ASSEMBLY__
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[03-06 10:00]** Re: [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of
 __ASSEMBLY__
   - 发件人: Thomas Huth <thuth@redhat.com>
3. **[03-06 14:17]** Re: [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of __ASSEMBLY__
   - 发件人: Sean Christopherson <seanjc@google.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.14, take #4

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  7 Mar 2025 16:18:24 +0000

#### 🤖 AI 总结

本邮件主题为“KVM/arm64 fixes for 6.14, take #4”，主要讨论了针对 KVM/arm64 的修复补丁。Marc Zyngier 提交了两个补丁，旨在修复在 hVHE 模式下，pKVM 的 PSCI 中继未能正确设置 CPU 的问题。这一问题导致主机在 MMU 处于未知状态下进入，并且 EL2 模式错误。补丁的具体内容包括初始化 SCTLR_EL1 和 HCR_EL2.E2H，以确保系统正常运行。

在历史讨论中，虽然没有具体的邮件记录，但可以推测之前的讨论涉及到 KVM/arm64 的稳定性和性能问题，特别是在 hVHE 模式下的实现细节。

本周的新进展是，Marc Zyngier 提交的补丁已被 Paolo Bonzini 接受，表示感谢并确认处理完成。这表明修复工作得到了认可，并将纳入即将发布的 6.14 版本中。整体来看，此次讨论集中在修复关键的系统错误，以提升 KVM/arm64 的可靠性。

#### 📝 邮件列表

1. **[03-07 16:18]** [GIT PULL] KVM/arm64 fixes for 6.14, take #4
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[03-09 09:11]** Re: [GIT PULL] KVM/arm64 fixes for 6.14, take #4
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Other

共 5 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v1 0/7] arm64: support EL2

**📧 邮件数**: 13 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 20 Feb 2025 14:13:47 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 单元测试的补丁系列，旨在为 arm64 架构添加对 EL2 的支持。历史讨论中，Joey Gouly 提出了七个补丁，主要内容包括在 EL2 启动时降级到 EL1、在 EL2 使用虚拟化定时器以及在 EL2 计数周期等功能。这些补丁经过了初步测试，并计划未来扩展以支持嵌套虚拟化。

在之前的讨论中，Alexandru Elisei 对补丁中的一些细节提出了疑问和建议，例如对 EL2 寄存器初始化的可靠性、定时器断言的使用等。他对补丁的总体方向表示认可，并进行了代码审查。

本周的新讨论中，Joey 和 Alexandru 继续就补丁的细节进行交流。Joey 表示将会考虑对 EL2 寄存器的初始化进行改进，并对 PMU 计数的实现进行了反思，确认需要设置 NSH 位以允许在 EL2 计数事件。整体来看，补丁系列在逐步完善中，参与者对实现细节的讨论有助于提高代码的健壮性和可靠性。

#### 📝 邮件列表

1. **[02-20 14:13]** [kvm-unit-tests PATCH v1 0/7] arm64: support EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[02-20 14:13]** [kvm-unit-tests PATCH v1 1/7] arm64: drop to EL1 if booted at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
3. **[02-20 14:13]** [kvm-unit-tests PATCH v1 2/7] arm64: timer: use hypervisor timers when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
4. **[02-20 14:13]** [kvm-unit-tests PATCH v1 6/7] arm64: pmu: count EL2 cycles
   - 发件人: Joey Gouly <joey.gouly@arm.com>
5. **[02-27 16:53]** Re: [kvm-unit-tests PATCH v1 1/7] arm64: drop to EL1 if booted at EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[02-27 16:55]** Re: [kvm-unit-tests PATCH v1 2/7] arm64: timer: use hypervisor
 timers when at EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
7. **[02-27 17:01]** Re: [kvm-unit-tests PATCH v1 6/7] arm64: pmu: count EL2 cycles
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
8. **[03-04 16:56]** Re: [kvm-unit-tests PATCH v1 6/7] arm64: pmu: count EL2 cycles
   - 发件人: Joey Gouly <joey.gouly@arm.com>
9. **[03-04 17:02]** Re: [kvm-unit-tests PATCH v1 1/7] arm64: drop to EL1 if booted at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
10. **[03-04 17:05]** Re: [kvm-unit-tests PATCH v1 2/7] arm64: timer: use hypervisor
 timers when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
11. **[03-06 15:52]** Re: [kvm-unit-tests PATCH v1 1/7] arm64: drop to EL1 if booted at EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
12. **[03-06 15:52]** Re: [kvm-unit-tests PATCH v1 2/7] arm64: timer: use hypervisor
 timers when at EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
13. **[03-06 15:58]** Re: [kvm-unit-tests PATCH v1 6/7] arm64: pmu: count EL2 cycles
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 2: [kvm-unit-tests PATCH 0/2] riscv: Run with other QEMU models

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 21 Feb 2025 17:27:54 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 RISC-V 架构的 kvm-unit-tests 的补丁，主要目的是允许使用除 'virt' 之外的其他 QEMU 机器模型。历史讨论中，Andrew Jones 提出了两个补丁：第一个补丁（PATCH 0/2）旨在通过命令行覆盖 'virt' 模型，并允许为早期输出指定不同的 UART 地址；第二个补丁（PATCH 1/2）则是为了使所有架构都能使用 earlycon 功能，特别是 RISC-V。

在之前的讨论中，Andrew Jones 还提到将 earlycon 的检查移出 ARM 块，以便更快地应用于 RISC-V。补丁的具体内容包括对配置文件的修改，增加了对早期控制台的支持。

在本周的新讨论中，Andrew Jones 对补丁进行了更新，明确指出目前只有 ARM、ARM64 和 RISC-V32/RISC-V64 架构关注该参数，并表示补丁已被合并。这表明该功能的开发进展顺利，且已为后续的测试做好准备。

#### 📝 邮件列表

1. **[02-21 17:27]** [kvm-unit-tests PATCH 0/2] riscv: Run with other QEMU models
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
2. **[02-21 17:27]** [kvm-unit-tests PATCH 1/2] configure: Allow earlycon for all architectures
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
3. **[03-04 10:12]** Re: [kvm-unit-tests PATCH 1/2] configure: Allow earlycon for all
 architectures
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
4. **[03-04 10:31]** Re: [kvm-unit-tests PATCH 0/2] riscv: Run with other QEMU models
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 3: [kvm-unit-tests PATCH] Makefile: Use CFLAGS in cc-option

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  7 Mar 2025 09:39:53 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于对 kvm-unit-tests 的 Makefile 进行修改，以便在使用 clang 进行交叉编译时能够正确处理目标特定的选项。

**原始 patch/问题的内容**：
Andrew Jones 提出了一个补丁，建议在 Makefile 中的 cc-option 函数调用中加入 CFLAGS，以确保在交叉编译时能够正确识别目标特定的编译选项。补丁的具体修改是在 cc-option 的调用中添加了 CFLAGS。

**之前讨论要点**：
本邮件线程没有提供历史讨论的内容，因此无法总结之前的讨论要点。

**本周的新讨论、进展或结论**：
在本周的讨论中，Thomas Huth 对该补丁进行了审查并表示支持。然而，Andrew Jones 随后发现该补丁存在问题，导致 x86 构建失败，出现了递归变量引用的错误。他表示将会修正该问题并计划提交一个新的版本（v2）。

#### 📝 邮件列表

1. **[03-07 09:39]** [kvm-unit-tests PATCH] Makefile: Use CFLAGS in cc-option
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
2. **[03-07 09:42]** Re: [kvm-unit-tests PATCH] Makefile: Use CFLAGS in cc-option
   - 发件人: Thomas Huth <thuth@redhat.com>
3. **[03-07 09:45]** Re: [kvm-unit-tests PATCH] Makefile: Use CFLAGS in cc-option
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 4: writable ID_AA64MMFR0_EL1.TGRAN*_2 ?

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 28 Feb 2025 16:19:06 +0100 (CET)

#### 🤖 AI 总结

在本邮件讨论中，Sebastian Ott 提出了一个关于可写性的问题，涉及到 ID_AA64MMFR0_EL1.TGRAN*_2 寄存器的迁移，特别是在两个 Graviton 主机之间的迁移。Sebastian 指出，这两个主机在 S2 的支持大小上存在差异，且当前 TGRAN*_2 寄存器尚不可写。他建议可以考虑将这些寄存器的客人视图设置为 NI（不可写），或者允许在两种值之间转换，并可能允许写入 NI。

在本周的新讨论中，Marc Zyngier 对此进行了回复。他表示支持在非 NV（非虚拟化）上下文中允许对 TGRAN*_2 寄存器写入任何值，但在 NV 上下文中则需要严格限制，确保 NI 是该特性的最低限制，不能允许写入 0。

总结来看，历史讨论中提出了寄存器可写性的问题及其潜在解决方案，而本周的讨论则进一步明确了在不同上下文中对寄存器写入的限制和要求。

#### 📝 邮件列表

1. **[02-28 16:19]** writable ID_AA64MMFR0_EL1.TGRAN*_2 ?
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[03-03 19:39]** Re: writable ID_AA64MMFR0_EL1.TGRAN*_2 ?
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 5: [kvm-unit-tests PATCH v2] Makefile: Use CFLAGS in cc-option

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  7 Mar 2025 10:18:29 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 单元测试的 Makefile 修改，主要由 Andrew Jones 提出。原始的 patch 旨在解决在使用 Clang 进行交叉编译时，CFLAGS 中未指定目标导致 cc-option 无法识别特定选项的问题。为此，patch 增加了 CFLAGS 到 CC 调用中，并引入了 realmode_bits 变量，以避免在构建 x86 时因 CFLAGS 自我引用而导致的构建失败。

在之前的讨论中，虽然没有具体的邮件记录，但可以推测出该问题的背景涉及到 KVM 单元测试的构建过程，特别是在不同编译器和目标架构下的兼容性问题。

在本周的新讨论中，Andrew Jones 提出了 v2 版本的 patch，修复了 x86 构建中与 realmode_bits 变量相关的问题。此次修改涉及两个文件的更新，确保了在不同环境下的构建能够顺利进行。整体来看，本周的进展主要集中在完善和修复之前 patch 的问题，以提高 KVM 单元测试的构建稳定性。

#### 📝 邮件列表

1. **[03-07 10:18]** [kvm-unit-tests PATCH v2] Makefile: Use CFLAGS in cc-option
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

